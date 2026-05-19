# HardID Protocol Development Roadmap / 产品路线图 🗺️

> **"I have ignited the spark of hardware sovereignty. The keyboard is now yours. We are looking for Lead Architects and Technical Co-founders to write the very first line of specification."**
> **“我已点燃硬件主权的火种，现在键盘交给你。我们正在寻找核心架构师与技术联合创始人，来写下第一行协议规范。”**

[English](#english) | [简体中文](#简体中文)

---

<a name="english"></a>
## English Version

**HardID is currently in the "Vision & Concept" stage.** The founder has laid down the immutable philosophy (Apache-2.0, TPM-bound, 100% Local-First). We are now looking for **Lead Maintainers / Core Architects** to take over the codebase and drive the engineering implementation. 

If you want to lead this movement, open an Issue or submit a PR to claim your role as a Co-founder!

### 🎯 Phase 1: Protocol Foundation & Core IM — *Focus: Infrastructure*
*   **[Protocol] Specification v1.0 Draft**
    *   [ ] Design the standardized Handshake, P2P node discovery, and E2E encrypted relay specifications.
    *   *Status:* `[Help Wanted 🆘]` | *Contributor:* **[Waiting for Lead Architect! 🫵]**
*   **[Networking] NAT Traversal Engine**
    *   [ ] Implement STUN/TURN or libp2p hole-punching for reliable node communication.
    *   *Status:* `[Help Wanted 🆘]` | *Contributor:* **[Open for Claim]**
*   **[Security] TPM 2.0 & Secure Enclave Hardware Binding**
    *   [ ] Create native cryptographic wrappers to extract/verify identities securely via hardware security chips.
    *   *Status:* `[Help Wanted 🆘]` | *Contributor:* **[Open for Claim]**
*   **[Application] HardID-IM (Alpha Core Prototype)**
    *   [ ] Build the very first minimal CLI/Desktop viable tool for peer-to-peer encrypted chat.
    *   *Status:* `[Help Wanted 🆘]` | *Contributor:* **[Open for Claim]**

### 🎯 Phase 2: Eco-System & Local AI — *Focus: Experience*
*   **[AI] HardID-LLM (Local Digital Twin)**
    *   [ ] Integrate open-source edge models (Llama-3/Qwen) running 100% locally via Local Data Bus.
    *   *Status:* `[Planned]` | *Contributor:* **[Open for Claim]**
*   **[Utility] HardID-Input (Privacy-First IME)**
    *   [ ] Fully local input method with a localized vector-association engine.
    *   *Status:* `[Planned]` | *Contributor:* **[Open for Claim]**
*   **[Communication] HardID-Mail (Serverless Email)**
    *   [ ] A serverless, asymmetric encrypted email system using P2P relays.
    *   *Status:* `[Planned]` | *Contributor:* **[Open for Claim]**

### 🎯 Phase 3: Hardware Standards & Mass Adoption — *Focus: Ecology*
*   **[Hardware] Open-Source Hardware Reference Designs**
    *   [ ] Release schematics for **Nexus Pod** (Data Sovereign Center) and **Nexus Node** (Edge Compute Device).
*   **[Community] Global Supply & Crowd-Funding**
    *   [ ] Partner with indie hardware manufacturers (Pine64, Raspberry Pi community) or launch a Kickstarter campaign.

---

<a name="简体中文"></a>
## 简体中文版

**HardID 目前处于“愿景与概念验证”阶段。** 发起人已经锁定了坚不可摧的底层哲学（Apache-2.0 专利保护、硬件私钥绑定、100%本地优先）。我们现在正面向全球寻找**核心维护者与技术架构师**来接管代码库，主导后续的工程落地。

如果你想成为这场主权计算运动的技术引领者，请提交 Issue 或 PR 认领你的联合创始人席位！

### 🎯 第一阶段：协议地基与核心 IM — *核心：技术破局*
*   **【协议】规范 v1.0 草案确立**
    *   [ ] 设计标准的握手、P2P 节点发现机制及端到端加密中继逻辑。
    *   *当前状态：* `[急需大牛 🆘]` | *认领人：* **[寻找核心架构师！🫵]**
*   **【网络】NAT 穿透与打洞引擎**
    *   [ ] 基于 libp2p 或自定义套接字，解决复杂网络环境下的纯 P2P 稳定连接。
    *   *当前状态：* `[急需帮助 🆘]` | *认领人：* **[虚位以待]**
*   **【安全】硬件 TPM 2.0 / Enclave 安全芯片绑定**
    *   [ ] 编写底层加密封装接口，实现非对称私钥在硬件芯片内的安全调用。
    *   *当前状态：* `[急需帮助 🆘]` | *认领人：* **[虚位以待]**
*   **【应用】HardID-IM (Alpha 原型开发)**
    *   [ ] 打造首个极简的命令行/桌面端工具，跑通最核心的纯 P2P 加密聊天应用。
    *   *当前状态：* `[急需帮助 🆘]` | *认领人：* **[虚位以待]**

### 🎯 第二阶段：生态衍生与本地 AI — *核心：丰富应用*
*   **【人工智能】HardID-LLM（本地数字孪生 AI）**
    *   [ ] 接入开源端侧大模型（如 Llama-3/Qwen），实现 100% 纯本地 AI 助理。
    *   *当前状态：* `[规划中]` | *认领人：* **[欢迎认领]**
*   **【生产力】HardID-Input（隐私第一输入法）**
    *   [ ] 纯本地运行的隐私输入法组件，内置完全本地化的向量联想与记忆引擎。
    *   *当前状态：* `[规划中]` | *认领人：* **[欢迎认领]**
*   **【通信】HardID-Mail（无服务器主权邮件）**
    *   [ ] 无服务器的、支持大附件的非对称加密邮件系统。
    *   *当前状态：* `[规划中]` | *认领人：* **[欢迎认领]**

### 🎯 第三阶段：硬件标准与商业落地 — *核心：硬件生态*
*   **【硬件】开源硬件参考设计**
    *   [ ] 正式发布 **Nexus Pod**（个人数据主权中心）与 **Nexus Node**（物理算力设备）的开源硬件原理图。
*   **【社区】全球供应链与众筹落地**
    *   [ ] 联合全球小众开源硬件厂商，或通过 Kickstarter 发起全球硬件主权众筹。
