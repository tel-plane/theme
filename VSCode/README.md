# 💻 VSCode (Markdown Preview Enhanced) 主题配置

本目录包含了适配 VSCode **Markdown Preview Enhanced (MPE)** 插件的 Tokyonight Storm (暗色) 预览主题。

---

## 📂 文件说明

*   `style.less` — 主题样式源码，采用 LESS 编写。包含霓虹灯发光特效、✦ 星芒分割线、以及专门针对 MPE 优化的 markdown 样式。
*   `config.js` — MPE 预览中 KaTeX、MathJax 及 Mermaid 图表的配置脚本。
*   `parser.js` — MPE 渲染生命周期钩子（onWillParseMarkdown / onDidParseMarkdown）。
*   `head.html` — 注入到预览 HTML `<head>` 里的头部文件。

---

## ⚙️ 启用与安装步骤

请按照以下步骤在 VSCode 的 Markdown Preview Enhanced 中配置并使用该主题：

1. **打开 MPE 配置目录**：
   * 在 VSCode 中，按 `Ctrl+Shift+P` (Windows) 或 `Cmd+Shift+P` (Mac) 打开命令面板。
   * 输入 `Markdown Preview Enhanced: Customize CSS` 并回车，这会打开 MPE 的全局 `style.less`。
   * 或者，你可以直接打开 MPE 的全局配置文件夹（通常位于 `~/.mpe/`）。
2. **替换样式与配置**：
   * 将本目录 `style.less` 里的内容复制，粘贴并覆盖到 MPE 开启的 `style.less` 中。
   * 将 `config.js`、`parser.js`、`head.html` 的内容对应复制到 MPE 配置文件夹中（或按 MPE 指引合并配置）。
3. **享受预览**：
   * 在 VSCode 中打开任何 Markdown 文件。
   * 点击右上角的 MPE 预览按钮即可享受高对比度的 Tokyonight 风格预览。
