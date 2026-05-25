# SESSION_LOG — 2026-05-09

## V3.2 全站设计系统（2026-05-09，会话"portfolio做瀑布屏"）
- **Hero**: "AI 驱动，/ 系统落地。" / "AI drives it. / Systems deliver."，stats 底对齐
- **Gallery**: 视频墙 CSS animation 自动滚动，21:9 叠层→1:1→16:9，品牌色光波背景，底部羽化
- **Glass**: oklch 多层阴影方案，亮/暗双模式
- **配色**: 卡片蓝统一 #1d4ed8，R 角 28px，iframe 懒加载
- **文案**: Apple 风格全站收紧，中英对仗，nowrap 防孤行
- **CI**: Cloudflare API Token 修复，wrangler-action@v3
- **版本**: v3.0→v3.1→v3.2，命名规则 v{major}.{minor}_{feature}.html
- **沉淀**: memory/portfolio-v3-full-design-system.md + modules/domains/coding.md 前端迭代章节

---

# SESSION_LOG — 2026-05-08

## 2026-05-08 | V3 Portrait Hero MVP
- **新建**: `index-v3_PortraitHero.html` → localhost:8087
- **Hero 改动**: 肖像左 + 文字右，demo card 移到 marquee 下方独立 section
- **肖像处理**: 1:1 裁切 + 圆角 16px + 三层阴影(border+暗影+蓝色微光) + hover 发光增强
- **保留全部 V1 功能**: 主题切换、中英双语、光标特效、光轨 canvas、marquee、flow modal、portfolio reel
- **背景**: grid 网格 + 肖像后方蓝色 radial glow
- **响应式**: 移动端肖像居中置顶，文字在下
- **待定**: 用户浏览器验收 → 调尺寸/位置/光影

## V3 Hero Video MVP (2026-05-08)
- **参考**: cantovisual.co.uk — 全屏视频 Hero + 暗色叠加层 dim effect
- **新建**: `index-v3_HeroVideo.html` → localhost:8087
- **Hero 结构**: `<video>` 全视口背景 + 三层 dim overlay → 居中大字
- **待办**: 上传 hero showreel MP4 到 R2

---

# SESSION_LOG — 2026-05-06

## 2026-05-06 | AI 自主学习 + Chewfun 营销调研启动
- **做了什么：**
  1. AI 自主学习 30 分钟——通读 7 个项目的核心代码：BuMemo 知识管线（947 行 Python）、badminton-review CV 全链路（YOLO→HMM→FCPXML）、Project_M Agent 编排管线、sensero-leads B2B 战略、Portfolio 液态玻璃 CSS 系统
  2. 安装 Playwright MCP 浏览器 server（`claude mcp add playwright`），用于后续直接浏览 Instagram/小红书抓数据
  3. 启动 Chewfun × 刘小超胡辣汤 AI-boosted marketing 策略——搭了 5 条产线框架（食品摄影批量/短视频快剪/文案多平台改写/周更内容日历/UGC 二创复用）
- **卡在哪：** WebFetch 全网被封（IG/小红书登录墙、Google consent wall、Bing 返回垃圾结果）。Playwright MCP 已装好，重启会话后可用浏览器直接登录抓数据
- **下次从哪开始：** 重启会话 → browser_navigate 到 Chewfun IG + 小红书 → 抓全物料 → 基于真实内容出优化方案
- **关键决策：** 先搭框架再用浏览器验证，不清谈；食品图 ROI 最高优先用 Vertex AI Imagen

---

# SESSION_LOG — 2026-05-05 (压缩版)

## 三个活跃版本

| 文件 | 端口 | 内容 | 状态 |
|------|------|------|:---:|
| `index.html` | 8080 | 生产版 (V1) | ✅ 线上 miantai.li |
| `index-v2.1_GalleryMVP.html` | 8081 | Gallery + Codex 审美优化 | 🟡 待推送 |
| `index-v2A_PolaroidHero.html` | 8082 | 拍立得 Hero 支线 | 🧪 实验 |
| `index-v2B_LiquidGlass.html` | 8083 | 液态玻璃全站 + Codex 审查 | 🟡 待用户验收 |
| `index-v2B-Bento.html` | 8084 | Bento Grid 画廊变体 | 🧪 MVP |
| `index-v2B-Masonry.html` | 8085 | Masonry 瀑布流 + hover 预览 | 🧪 MVP |
| `index-v2C_Refined.html` | 8086 | 参考图复刻：等高一排 + 极简悬浮 | 🟡 待用户验收 |

## V2C Refined：Codex + Qwen3-VL 双路 cross-ref (2026-05-05)
- **双模型分析**：Qwen3-VL:4b 本地提取设计特征 + Codex GPT-5.3 xhigh 像素级测量（卡宽 310/131/185/156/220px）
- **关键发现**：等高一排、宽度按比例变化（非统一网格），无边框（Qwen）或 1px 微光边框（Codex），极浅双层阴影
- **Dark**: card bg=bg-2, border `rgba(148,163,184,.12)`, shadow `0 2px 8px rgba(0,0,0,.35)` 
- **Light**: card bg=`#fbfcfd`, border `rgba(15,23,42,.08)`, shadow `0 1px 2px rgba(15,23,42,.04)`
- **Hover**: translateY(-2px) + blue border + blue glow（Codex 精确测量）
- **多模态能力** 已写入 CLAUDE.md

## V2B Gallery 变体 (2026-05-05)
- **Bento (8084)**: CSS Grid 3 列 `grid-auto-rows:280px`，21:9 宽银幕 `bento-wide`（span 2 cols），9:16 竖屏 `bento-tall`（span 2 rows），`object-fit:cover` 填充
- **Masonry (8085)**: CSS `columns:3` 瀑布流，每卡保留原生 `aspect-ratio`（16:9/9:16/21:9/4:3/1:1），hover 自动嵌入静音 YouTube iframe 预览
- 两个变体都保留了液态玻璃卡片质感 + Logo 风格展开按钮
- Gallery 数据已更新：Nicholas (x2FYUWng9TM)、Yitta (E-Cr20jSNsI)
- Hero AI Demo 视频 (v2R1_mZJQbg)

## V2.1_GalleryMVP 已完成

从 V1 提取已验证修复后重建：
- 静音 bug 修（iframe `muted` 属性 + JS 每次切换后 `setAttribute('muted','')`）
- 时间线配色对调（Warwick 紫、日期蓝、dot 蓝）
- 新增 03.5 Gallery：9 个占位卡片（3 微电影 + 2 纪录片 + 6 商业），4 个 filter pill（全部/影视审美/剪辑执行/商业制作）
- 竖屏/1:1 自动 `.is-portrait`，4:5 容器
- 默认显 6 张，渐变遮罩 + "展开全部" 按钮
- 性能优化：canvas 点数 120→60、blur 18px→8px、GPU 加速
- Codex 5.3 xhigh 审美审查 → 5 条 CSS 全落地
- Agent emoji→数字、Hero kicker "案例轮播"、stat#4 缩短、"联系我" 按钮简洁化

## V2A_PolaroidHero 支线

Hero 首屏拍立得风格：
- 头像用米色 Polaroid 边框 + 4 层立体阴影 + -2° 微旋转
- 名字换 clip-path 撕纸便签
- 案例卡微旋转 0.5°，hover 回正
- Hero 背景加 3px 颗粒噪点纹理
- 只用了 Codex 的多层阴影 + clip-path（克制，不加胶带）

## 基础架构

- **视觉栈**：macOS Vision OCR (`.mac-ocr.py`) + Qwen3-VL 4B (Ollama 本地) + DeepSeek V4 Pro[1m] 主力
- **视频**：海外 YouTube Unlisted，国内 B 站（待验证），R2 国内不通
- **域名**：miantai.li (CF Pages) + dl-studio.ltd (阿里云，等实名过审)
- **Codex 协作**：CLAUDE.md 软链到 `.codex/AGENTS.md` 和 `Documents/Codex_Projects/AGENTS.md`，用 `codex exec --skip-git-repo-check` 调 GPT-5.3 xhigh 做多模态设计审查
- **边界**：`/Users/a1/AI-HOME/Claude-code/` = 我家，`/Users/a1/Documents/Codex_Projects/` = Codex 家，不越界

## 规则 (CLAUDE.md level)
1. 文件不删 → 移入 `to-be-deleted/` 文件夹
2. 新建前 `ls` 查重，重名加 `_v2` 后缀
3. 每次输出后更新 SESSION_LOG
4. 版本命名：`v{major}.{minor}_{feature}.html`

## 网站结构 (7 sections)
hero → marquee → about (01 简介) → system (02 系统) → work (03 作品) → gallery (03.5 作品库) → agents (04 Agent Stack) → contact (05 联系)

## 用户设计偏好
- 紫色学历 (#a78bfa/亮色 #7c3aed)、蓝色时间线
- 标题力量感（得意黑 Oblique 自托管）、系统区数字 01-06 非 emoji
- 卡片 hover 浮起 (`translateY(-6px)` + 发光阴影 + `scale(1.01)`)
- 联系方式右对齐、居中布局
- IG 官方 SVG 图标
- 中英双语 + B 站/YouTube 双视频源切换
- 深/亮双主题

## V2B_LiquidGlass 已完成 (2026-05-05)
- 全站液态玻璃设计系统：`--glass-blur`、`--glass-highlight`、`--glass-edge` CSS tokens
- Nav 毛玻璃 backdrop-filter + 镜面高光伪元素
- 所有卡片 (profile/project/agent/gallery/demo/contact) 覆盖玻璃质感
- Gallery 展开按钮：Logo 蓝色调 + 圆形 icon + 液态玻璃 pill + hover 发光
- 按钮 (btn-primary/secondary) 渐变 + 玻璃处理
- Flow modal 强毛玻璃 overlay
- Body 背景 SVG 噪点纹理
- Codex 5.3 xhigh 审查（4 条反馈 → 全部修复）：Gallery 卡片玻璃感增强、展开按钮布局修正、响应式补回、z-index 修复
- `color-mix()` 兼容性替换为 rgba fallback
- `-webkit-backdrop-filter` 补齐

## 待执行
- [ ] V2B 用户浏览器验收（localhost:8083）
- [ ] V2.1 推上线（等用户确认）
- [ ] V2A 完善 + 用户 feedback
- [ ] Gallery 占位符 → 真实视频 ID（等用户上传 YouTube/B 站后提供）
- [ ] `dl-studio.ltd` 阿里云实名过审 → Cloudflare Pages 绑域名
- [ ] B 站私密视频嵌入验证
