# Daniel Portfolio

个人作品集网站。

## 当前状态

- 文件：HTML + dist/
- 下一步：review

## 多模态能力 (2026-05-05)

本地部署了两套视觉分析工具，**每次涉及图像/设计审查时优先使用**：

| 工具 | 模型 | 用途 | 命令 |
|------|------|------|------|
| Qwen3-VL | 4B (Ollama 本地) | 图像分析、设计参考提取、UI 对比 | `http://localhost:11434` API |
| macOS OCR | Apple Vision | 截图文字提取、中英日 OCR | `python3 .mac-ocr.py <image>` |

**使用策略：**
- 设计参考图分析 → Qwen3-VL 本地先跑（免费、离线），Codex 闭源模型做 cross-reference（复杂项目）
- UI 文字提取 → macOS OCR（零成本、离线）
- 简单设计问答 → Qwen3-VL 本地
- 复杂美学判断 → Codex (GPT-5.x xhigh) 多模态

## 项目规则

- 全局编码规范、红线、Agent Team 从父级 `CLAUDE.md` 继承
