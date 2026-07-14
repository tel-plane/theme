# 🍒 Cherry Studio 主题配置 (Cherry Studio Theme Config)

本目录包含了适配 Cherry Studio 客户端的 Tokyonight 主题样式，支持暗色和浅色模式的自动切换。

---

## 🎨 开发与引用说明

*   `Tokyonight.css` — **本项目唯一完全原创开发的主题样式文件**。它完美移植了 Obsidian 主题的高级 Markdown 渲染特效（包括双栏标题修饰、✦ 星芒分割线、卡片 hover、KaTeX 公式微调等）。
*   其他 `.css` 文件（如 `Claude.css`、`Miku-more.css`、`Modern_Workspace.css` 等）— **均为只读的第三方参考文件**。它们作为开发时的优秀样式灵感来源得以保留，请勿修改或直接使用。

---

## ⚙️ 启用与安装步骤

要在 Cherry Studio 中启用 `Tokyonight` 主题，请按照以下步骤操作：

1. **获取代码**：
   打开本目录下的 `Tokyonight.css`，复制里面的全部内容。
2. **在 Cherry Studio 中配置**：
   * 打开 Cherry Studio 客户端。
   * 进入 **设置 (Settings)** -> **显示设置 (Display Settings)**。
   * 滚到最下面找到 **自定义 CSS (Custom CSS)** 输入框。
   * 将复制的 CSS 代码粘贴进去。
3. **保存并应用**：
   * 点击保存，Cherry Studio 会立即重新加载样式。
   * 当你在 Cherry Studio 中切换系统主题（深色/浅色）时，`Tokyonight` 也会自动在 **Tokyonight Storm (暗色)** 与 **Tokyonight Day (亮色)** 之间智能切换。
