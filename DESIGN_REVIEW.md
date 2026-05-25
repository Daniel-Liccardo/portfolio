# Daniel Portfolio — 设计审查文档

> 给多模态模型做视觉审查用的上下文梳理。

## 线上地址

- Production: `https://miantai.li` (Cloudflare Pages, SSL 可能还在签发中)
- GitHub: `https://github.com/Daniel-Liccardo/daniel-portfolio`
- 本地: `python3 -m http.server 8080`

## 页面结构（6 sections）

| # | Section ID | 导航标签 | 内容 |
|---|-----------|---------|------|
| 1 | hero | — | 首屏 + 个人介绍 + YouTube 作品轮播 + stats |
| 2 | about | 关于 | 2 段文字 + logo strip + 紫色教育时间线（左栏）/ 头像照片卡片（右栏） |
| 3 | system | 系统 | 14 节点 AI 生产系统图 + 3 stat cards |
| 4 | work | 作品 | 4 张 project card |
| 5 | agents | Agents | 6 张 Agent 卡片 |
| 6 | contact | 联系 | Email / Phone / Instagram |

## 设计决策记录

### 已完成
- 字体：标题用 **得意黑 Smiley Sans Oblique**（自托管 woff2），正文 Noto Sans SC fallback
- 暗/亮双主题（跟随系统 + 手动切换）
- 中英双语切换（data-i18n 系统）
- Cursor: 自定义光标（mix-blend-mode: difference 蓝点 + 跟随环）
- Portfolio reel: YouTube iframe 自动轮播 3 个作品
- About: Logo strip 左栏, 学历时间线紫色 (#a78bfa), Profile card 上提 -70px 对齐标题
- Contact: 图标+标签左 / 数值右对齐, 紧凑间距
- IG 图标: 官方 SVG
- Credentials section 已删除, 内容合入 About

### 用户曾反馈但未完全解决的问题

1. **"统" 字渲染不全** — system section 标题 "生产操作系统" 中 "统" 字在 得意黑 Oblique 字体下右边缘被裁切。尝试过加 line-height、padding-right、letter-spacing 但效果有限。

2. **光标在 dist 版正常，但之前多次修改导致卡死/不可见** — 最终回退到 dist 版原装 cursor 代码解决。mix-blend-mode: difference 在某些页面背景下可能导致不可见。

3. **About 左右栏视觉平衡** — Profile card 已通过 -70px 上提，但用户曾反馈左边内容偏少、不够匀称。

4. **System section 14 节点** — 用户曾表示内容偏多，考虑精简为 pipeline flow。

5. **Contact section 太长** — 已紧凑化（padding 3.5rem → 2.5rem），但用户可能在宽屏下仍觉偏长。

6. **得意黑字体** — 用户从霞鹜文楷换到得意黑追求"标题力量感"，但 oblique 斜体设计可能导致中文字符边缘裁切。

### 用户的设计偏好（从对话中提取）

- "标题的力量感" — 字体需要粗重、有冲击力
- "左右视觉平衡" — 两栏布局要匀称
- "不要太长/太空" — 内容要紧凑
- 紫色用于学历板块 (#a78bfa)
- IG 用官方 SVG 而非 emoji
- 联系方式数值右对齐

### 已知技术问题

- SSL 证书刚签发（Google CA），可能有几分钟的 HTTPS 不可用
- 得意黑 Oblique 字体文件 ~1.1MB，首次加载需时间
- System section 包含 14 个 node-card + 3 个 stat-card，移动端可能密集

## 文件信息

- index.html: 1926 行
- 自托管资源: SmileySans-Oblique.otf.woff2 (1.4MB), 头像照片, hero-bg.png, logos/
