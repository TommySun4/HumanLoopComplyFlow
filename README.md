# LoopLedger

**Oversight that proves itself. — 会自证的人工监督。**

Synoptix Responsible AI Hackathon 项目，结合 **HumanLoop（AI 人工监督）** 与 **ComplyFlow（合规证据整理）**。项目以贷款审批分类器为演示场景，计划将高风险或低置信度的 AI 决策交给人工审核，记录审核过程，并生成可追溯的证据报告。

## 当前状态

仓库已建立项目目录、依赖清单和模块占位文件。**Python 业务逻辑尚未实现，目前不能运行完整的审批流程。**

| 内容 | 状态 |
| --- | --- |
| 项目方案、执行计划与接口契约 | 已写入文档 |
| Python 包、Streamlit 页面、报告模板与脚本 | 已创建文件骨架 |
| HTML 交互原型 | 已有模拟数据原型，尚未接入 Python 模块 |
| 模型训练、风险闸门、数据库与审计链 | 待实现 |
| 人工审批、监督质量指标与证据导出 | 待实现 |
| 端到端验证与演示 | 待完成 |

## 计划实现的流程

1. **生成预测**：使用 German Credit 数据集训练贷款审批分类器，输出决策、置信度和 SHAP 特征贡献。
2. **风险分流**：由风险闸门检查预测，将需要人工判断的申请送入审批队列。
3. **人工审核**：展示申请信息和 AI 建议，记录审核员的操作、理由与审阅时长。
4. **记录证据**：使用 SQLite 保存业务状态与哈希链审计日志，并提供链完整性检查。
5. **观察监督质量**：计算审阅时长、推翻 AI 的比例、短理由比例和金标准题检出率，辅助识别监督异常。
6. **导出报告**：汇总事件、指标与项目文档中的法规映射，生成 Markdown / JSON 证据包；PDF 为可选扩展。

## 技术方案

实现以 [PLAN.md](./PLAN.md) 中的决策和接口契约为准。

| 部分 | 计划采用的技术 |
| --- | --- |
| 界面与应用入口 | Streamlit，直接调用 Python 模块，不单独启动 API 服务 |
| 模型与解释 | scikit-learn、XGBoost、SHAP |
| 数据集 | German Credit，通过 `fetch_openml("credit-g")` 获取 |
| 持久化 | SQLite 单文件 `loopledger.db`，数据库待实现 |
| 数据处理与图表 | pandas、Plotly |
| 报告模板 | Jinja2 |

## 项目结构

```text
HumanLoopComplyFlow/
├── README.md
├── LoopLedger.md                   # 项目方案与演示构想
├── PLAN.md                         # 分工、接口契约与验收要求
├── requirements.txt
├── app.py                          # Streamlit 入口
├── loopledger/
│   ├── __init__.py
│   ├── schemas.py                  # 共享数据结构
│   ├── model.py                    # 训练、预测与 SHAP
│   ├── gate.py                     # 风险闸门
│   ├── gold.py                     # 金标准测试题
│   ├── ledger.py                   # SQLite 与哈希链日志
│   ├── metrics.py                  # 监督质量指标
│   └── evidence.py                 # 证据包生成
├── pages/
│   ├── 1_Run_Batch.py              # 批量提交申请
│   ├── 2_Review_Queue.py           # 人工审批
│   ├── 3_Oversight_Dashboard.py    # 监督质量面板
│   └── 4_Compliance.py             # 证据导出与篡改检测
├── templates/
│   └── evidence_report.md.j2       # 证据报告模板
├── scripts/
│   └── demo_reset.py              # Demo 数据重置脚本
└── prototype/
    └── index.html                 # 使用模拟数据的交互原型
```

## 开发环境准备

需要 Python 3、Git，以及访问 GitHub 和 Python 包源的网络连接。以下为 macOS / Linux 命令：

```bash
git clone git@github.com:joyce0101/HumanLoopComplyFlow.git
cd HumanLoopComplyFlow
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

SSH 克隆需要 GitHub SSH 密钥配置。也可使用 HTTPS 地址：

```bash
git clone https://github.com/joyce0101/HumanLoopComplyFlow.git
```

首次通过 OpenML 获取数据集时需要网络；本仓库尚未提供数据缓存与模型训练实现。

### 查看界面原型

用浏览器打开 [prototype/index.html](./prototype/index.html)。原型包含批量运行、审批队列、监督面板和证据页面，使用模拟数据；其中的统计、导出和链校验结果用于展示界面交互。页面样式依赖外部脚本，加载样式需要网络。

### 后续启动应用

在 `app.py` 和对应模块实现后，从仓库根目录运行：

```bash
python -m streamlit run app.py
```

当前入口和页面仅有占位说明，上述命令尚不能展示业务功能。`scripts/demo_reset.py` 也尚未实现数据重置。

## 团队分工与协作

| 角色 | 负责内容 | 主要文件 |
| --- | --- | --- |
| A：ML 工程师 | 模型、解释、风险闸门、金标准题 | `model.py`、`gate.py`、`gold.py` |
| B：后端 / 数据工程师 | 数据库、哈希链、监督指标、数据重置 | `ledger.py`、`metrics.py`、`scripts/demo_reset.py` |
| C：前端工程师 | Streamlit 入口与全部页面 | `app.py`、`pages/` |
| D：合规 / 产品 / Pitch | 证据报告、法规映射、海报与演示 | `evidence.py`、`templates/` |

每人在独立分支开发，在计划检查点合并到 `main`。开发前先阅读 [PLAN.md](./PLAN.md) 第 3 节，按共享数据结构和函数签名实现；共享契约的改动需要全队确认。

## 文档

- [LoopLedger.md](./LoopLedger.md)：项目背景、目标流程、监督指标与演示构想。
- [PLAN.md](./PLAN.md)：技术决策、四人分工、接口契约、数据库设计与验收检查点。
