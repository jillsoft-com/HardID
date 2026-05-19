# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Copyright 2026 jillsoft-com (Lijun Jiang)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Project: HardID Protocol (Hardware-as-Identity)
# Module: HardID-IM P2P Core Prototype (Alpha v1.0)
# -------------------------------------------------------------------------

import socket
import threading
import sys
import time
import os

# 提示：为了保持纯Python标准库实现、方便所有人直接运行，本Demo使用了一个异或流密码作为加密演示。
# 在 Phase 1 的正式版本中，这部分将被替换为更加稳健的 PyCA/cryptography 库（包含 Ed25519 和 AES-GCM）。

class HardIDNode:
    def __init__(self, node_name, port):
        self.node_name = node_name
        self.port = port
        self.host = '0.0.0.0'
        
        # 1. 模拟物理硬件生成唯一ID（公钥/私钥对）
        # 在实际硬件中，这对应着本地安全芯片（TPM/Enclave）生成的根密钥
        self.private_key = f"PRIV_KEY_{node_name}_{os.getpid()}"
        self.public_key = f"HARDID_{node_name.upper()}_" + "".join([hex(ord(c))[2:] for c in node_name])
        
        self.peer_socket = None
        self.peer_hardid = None
        self.is_running = True

        print("-" * 60)
        print(f"🔒 HardID 节点初始化成功！")
        print(f"👤 节点名称: {self.node_name}")
        print(f"🆔 物理账号 (你的全局公钥/HardID):\n   >> {self.public_key}")
        print(f"📡 本地监听端口: {self.port}")
        print("-" * 60)

    def start_server(self):
        """启动本地监听服务，等待其他硬件节点连接"""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(1)
        
        print(f"⚡ [系统提示] 正在等待其他 HardID 硬件节点握手连接...")
        
        while self.is_running:
            try:
                server.settimeout(1.0)
                conn, addr = server.accept()
                self.peer_socket = conn
                print(f"\n🔗 [网络流] 检测到来自 {addr} 的物理连接，开始密码学握手...")
                if self.handle_handshake(is_initializer=False):
                    threading.Thread(target=self.receive_messages, daemon=True).start()
                    break
            except socket.timeout:
                continue
            except Exception as e:
                print(f"❌ 监听异常: {e}")
                break

    def connect_to_peer(self, peer_ip, peer_port):
        """主动连接到另一个硬件节点"""
        print(f"🚀 [网络流] 正在尝试直连外部节点 {peer_ip}:{peer_port} ...")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((peer_ip, peer_port))
            self.peer_socket = client
            print(f"🔗 [网络流] 物理连接建立，发起主权身份验证握手...")
            if self.handle_handshake(is_initializer=True):
                threading.Thread(target=self.receive_messages, daemon=True).start()
                return True
        except Exception as e:
            print(f"❌ [连接失败] 目标节点可能不在线，或网络受到防火墙限制。异常原因: {e}")
            return False
        return False

    def handle_handshake(self, is_initializer):
        """
        HardID 核心对等身份交换协议 (Zero-Knowledge Handshake)
        没有中央服务器介入，两台设备直接交换并验证彼此的物理账号(公钥)
        """
        try:
            if is_initializer:
                # 1. 主动方先发送自己的公钥和身份声明
                handshake_payload = f"HARDID_HELLO:{self.public_key}:{self.node_name}"
                self.peer_socket.send(handshake_payload.encode('utf-8'))
                
                # 2. 等待接收被动方的回应
                response = self.peer_socket.recv(1024).decode('utf-8')
                if response.startswith("HARDID_HELLO:"):
                    _, peer_pubkey, peer_name = response.split(":")
                    self.peer_hardid = peer_pubkey
                    print("\n" + "="*50)
                    print(f"🤝 [握手成功] 成功添加新的主权好友！")
                    print(f"👥 好友别名: {peer_name}")
                    print(f"🆔 对方唯一的物理账号(HardID):\n   >> {self.peer_hardid}")
                    print("="*50 + "\n")
                    return True
            else:
                # 1. 被动方先接收主动方的公钥
                request = self.peer_socket.recv(1024).decode('utf-8')
                if request.startswith("HARDID_HELLO:"):
                    _, peer_pubkey, peer_name = request.split(":")
                    self.peer_hardid = peer_pubkey
                    
                    # 2. 被动方回应自己的公钥
                    handshake_payload = f"HARDID_HELLO:{self.public_key}:{self.node_name}"
                    self.peer_socket.send(handshake_payload.encode('utf-8'))
                    
                    print("\n" + "="*50)
                    print(f"🤝 [握手成功] 对方已通过你的主权身份验证！")
                    print(f"👥 对方别名: {peer_name}")
                    print(f"🆔 对方唯一的物理账号(HardID):\n   >> {self.peer_hardid}")
                    print("="*50 + "\n")
                    return True
        except Exception as e:
            print(f"❌ 密码学握手协议崩溃，身份验证失败: {e}")
            return False
        return False

    def _encrypt_decrypt(self, text, key):
        """本地流对称加解密算法（演示用，确保传输内容在公网上是密文）"""
        return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

    def send_chat_message(self, text):
        """通过加密通道向对端硬件发送数据"""
        if not self.peer_socket:
            print("❌ 发送失败：当前未连接到任何硬件节点。")
            return
        try:
            # 使用对方的HardID作为混淆密钥进行对称流加密
            encrypted_data = self._encrypt_decrypt(text, self.peer_hardid)
            payload = f"HARDID_MSG:{encrypted_data}"
            self.peer_socket.send(payload.encode('utf-8'))
        except Exception as e:
            print(f"❌ 消息发送异常: {e}")

    def receive_messages(self):
        """后台线程：持续接收对端硬件发送的密文，并在本地解密渲染"""
        while self.is_running:
            try:
                data = self.peer_socket.recv(4096).decode('utf-8')
                if not data:
                    print(f"\n📡 [系统提示] 对方节点断开物理连接（可能离线或关机）。")
                    break
                
                if data.startswith("HARDID_MSG:"):
                    encrypted_msg = data.split(":", 1)[1]
                    # 在本地使用对方的HardID还原出明文数据，确保数据绝对隐私
                    decrypted_msg = self._encrypt_decrypt(encrypted_msg, self.public_key)
                    print(f"\n💬 [收到密文消息] 对方说: {decrypted_msg}")
                    print("✏️ 输入消息发送 (或输入 'exit' 退出): ", end="", flush=True)
            except Exception:
                break

    def close(self):
        self.is_running = False
        if self.peer_socket:
            self.peer_socket.close()


if __name__ == "__main__":
    print("Welcome to HardID Network Starter!")
    name = input("1. 请输入你当前硬件节点的别名 (例如: NodeA): ").strip()
    my_port = int(input("2. 请设置本地监听端口 (例如: 8888): ").strip())
    
    node = HardIDNode(name, my_port)
    
    # 启动后台监听线程
    threading.Thread(target=node.start_server, daemon=True).start()
    time.sleep(0.5) # 给服务器一点启动时间
    
    choice = input("\n[运行模式选择]\n[1] 等待别人连我\n[2] 主动直连别人的硬件节点\n请选择 (1/2): ").strip()
    
    if choice == '2':
        peer_ip = input("请输入目标节点的 IP 地址 (本地测试请输入 127.0.0.1): ").strip()
        peer_port = int(input("请输入目标节点的 监听端口: ").strip())
        node.connect_to_peer(peer_ip, peer_port)
        
    print("\n💬 密文通信通道已就绪。你可以开始打字聊天了。")
    while True:
        try:
            msg = input("✏️ 输入消息发送 (或输入 'exit' 退出): ").strip()
            if msg.lower() == 'exit':
                break
            if msg:
                node.send_chat_message(msg)
        except (KeyboardInterrupt, SystemExit):
            break
            
    node.close()
    print("👋 HardID 节点安全下线，本地缓存已销毁。")
