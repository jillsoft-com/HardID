# HardID Protocol Development Roadmap / 产品路线图 🗺️

> **"A grand vision starts with explicit engineering steps. Choose your battlefield and build data sovereignty with us."**
> **“宏大的愿景始于清晰的工程步骤。选择你的战场，与我们一同构建数据主权。”**

[English](#english) | [简体中文](#简体中文)

---

<a name="english"></a>
## English Version

We are actively seeking global contributors, maintainers, and core architects. If you are interested in any of the tasks below, please open an Issue with the title `[Contribute] Phase X - Task Name` to claim your piece of history!

### 🎯 Phase 1: Protocol & Core IM (Months 0-6) — *Focus: Foundation*
*   **[Core] Protocol Specifications v1.0**
    *   [ ] Define standardized Handshake, P2P discovery, and E2E encrypted relay logic.
    *   *Status:* `[Design Phase]` | *Contributor:* `[jillsoft-com]`
*   **[Networking] NAT Traversal & Hole Punching**
    *   [ ] Implement STUN/TURN or libp2p hole-punching for reliable connections under symmetric NATs.
    *   *Status:* `[Help Wanted 🆘]` | *Contributor:* **[Waiting for You! 🫵]**
*   **[Security] Hardware TPM 2.0 / Enclave Bindings**
    *   [ ] Write native cryptographic wrappers to securely bind/verify identities via hardware chips.
    *   *Status:* `[Help Wanted 🆘]` | *Contributor:* **[Waiting for You! 🫵]**
*   **[Application] HardID-IM (Alpha Prototype)**
    *   [ ] Build a minimal CLI/Desktop viable tool for direct P2P encrypted chat using PCs as nodes.
    *   *Status:* `[Coding]` | *Contributor:* `[jillsoft-com]`

### 🎯 Phase 2: Eco-System & Local AI (Months 6-12) — *Focus: Experience*
*   **[AI] HardID-LLM (Local Digital Twin)**
    *   [ ] Integration with open-source edge models (Llama-3/Qwen) running 100% locally via the Local Data Bus.
    *   *Status:* `[Planned]` | *Contributor:* **[Open for Claim]**
*   **[Utility] HardID-Input (Privacy-First IME)**
    *   [ ] Fully local input method component with a localized vector-association engine.
    *   *Status:* `[Planned]` | *Contributor:* **[Open for Claim]**
*   **[Communication] HardID-Mail (Serverless Email)**
    *   [ ] A serverless, asymmetric encrypted email system supporting decentralized large-attachment relays.
    *   *Status:* `[Planned]` | *Contributor:* **[Open for Claim]**

### 🎯 Phase 3: Hardware Standards & Mass Adoption (Months 12+) — *Focus: Ecology*
*   **[Hardware] Open-Source Hardware Reference Designs**
    *   [ ] Release schematics and reference designs for **Nexus Pod** (Data Sovereign Center) and **Nexus Node** (Edge Compute Device).
*   **[Community] Global Supply & Crowd-Funding**
    *   [ ] Partner with indie hardware manufacturers (Pine64, Raspberry Pi community) or launch a Kickstarter campaign.

---

<a name="简体中文"></a>
## 简体中文版

我们正在全力寻找全球贡献者、维护者以及核心架构师。如果你对以下任何任务感兴趣，请提交一个 Issue，标题为 `[Contribute] 阶段X - 任务名称` 来认领你的代码战场！

### 🎯 第一阶段：协议定义与核心 IM（0 - 6个月）— *核心：打牢地基*
*   **【核心】协议规范 v1.0 定义**
    *   [ ] 确立标准的握手、P2P 节点发现机制及端到端加密中继逻辑。
    *   *当前状态：* `[设计中]` | *认领人：* `[jillsoft-com]`
*   **【网络】NAT 穿透与打洞（Hole Punching）**
    *   [ ] 基于 libp2p 或自定义套接字，解决对称型 NAT 下的纯 P2P 稳定连接问题。
    *   *当前状态：* `[急需帮助 🆘]` | *认领人：* **[等待虚位以待 🫵]**
*   **【安全】硬件 TPM 2.0 / Enclave 安全芯片绑定**
    *   [ ] 编写底层加密封装接口，实现非对称私钥在硬件芯片内的安全调用与身份验证。
    *   *当前状态：* `[急需帮助 🆘]` | *认领人：* **[等待虚位以待 🫵]**
*   **【应用】HardID-IM (Alpha 原型开发)**
    *   [ ] 完善极简的命令行/桌面端工具，将电脑虚拟化为本地节点，跑通纯 P2P 加密聊天。
    *   *当前状态：* `[代码编写中]` | *认领人：* `[jillsoft-com]`

### 🎯 第二阶段：生态衍生与本地 AI（6 - 12个月）— *核心：丰富应用*
*   **【人工智能】HardID-LLM（本地数字孪生 AI）**
    *   [ ] 接入开源端侧大模型（如 Llama-3/Qwen），通过本地数据总线实现 100% 纯本地 AI 助理。
    *   *当前状态：* `[规划中]` | *认领人：* **[欢迎认领]**
*   **【生产力】HardID-Input（隐私第一输入法）**
    *   [ ] 纯本地运行的隐私输入法组件，内置完全本地化的向量联想与记忆引擎。
    *   *当前状态：* `[规划中]` | *认领人：* **[欢迎认领]**
*   **【通信】HardID-Mail（无服务器主权邮件）**
    *   [ ] 无服务器的、支持大附件的非对称加密邮件系统，利用 P2P 网络实现离线投递中继。
    *   *当前状态：* `[规划中]` | *认领人：* **[欢迎认领]**

### 🎯 第三阶段：硬件标准与商业落地（12个月以上）— *核心：硬件生态*
*   **【硬件】开源硬件参考设计**
    *   [ ] 正式发布 **Nexus Pod**（个人数据主权中心）与 **Nexus Node**（物理算力设备）的开源硬件原理图与参考设计。
*   **【社区】全球供应链与众筹落地**
    *   [ ] 联合全球小众开源硬件厂商（如 Pine64、树莓派社区），或通过 Kickstarter 发起全球硬件主权众筹。
