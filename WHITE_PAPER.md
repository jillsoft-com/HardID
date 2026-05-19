# HardID Technical Whitepaper / 技术白皮书 (v1.0)

[English](#english) | [简体中文](#简体中文)

---

<a name="english"></a>
## English Version

### 1. Architecture Overview
The HardID architecture breaks the classic Client-Server model. It consists of three structural layers:
* **Hardware Sovereign Layer (HSL):** Utilizes hardware-level Secure Enclaves to store root private keys and execute local ZK (Zero-Knowledge) proofs.
* **Local Data Bus (LDB):** A sandbox data pipeline running within the OS that allows local cross-app collaboration (e.g., Input Method feeding into LLM) while strictly blocking unauthorized outbound traffic.
* **Delay-Tolerant Onion Relay (DTOR):** Solves the offline dilemma. When the receiver is offline, encrypted packets are routed via decentralized DHTs using onion-routing. The relay nodes have zero knowledge of the sender, receiver, or content.

### 2. Cryptographic Handshake & P2P Routing
Every HardID node generates an Ed25519 key pair. Friendship establishment is a reciprocal exchange of public keys. Communication sessions utilize the Double Ratchet Algorithm for end-to-end forward secrecy.

---

<a name="简体中文"></a>
## 简体中文版

### 1. 架构概述
HardID 架构彻底打破了传统的 C/S（客户端-服务器）模式。它由三个结构层组成：
* **硬件主权层 (HSL)：** 利用硬件级安全加密芯片存储根私钥，并执行本地零知识（ZK）证明。
* **本地数据总线 (LDB)：** 运行在系统内部的沙盒数据管道，允许本地跨应用协同（例如：输入法与大模型联动），同时严格阻断未经授权的数据外流。
* **时空延迟容忍洋葱中继 (DTOR)：** 解决离线传输难题。当接收方离线时，加密数据包通过分布式 DHT（哈希表）以洋葱路由形式中转。中继节点对发送者、接收者和内容完全“零知识”。

### 2. 密码学握手与 P2P 路由
每个 HardID 节点生成一对 Ed25519 密钥对。建立好友关系即互换公钥。通讯会话采用双棘轮算法（Double Ratchet Algorithm），确保端到端的向前安全性。
