# 💻 VSCode (Markdown Preview Enhanced) 主题配置

本目录包含了适配 VSCode **Markdown Preview Enhanced (MPE)** 插件的 Tokyonight Storm (暗色) 预览主题。

---

## 📂 文件说明

*   `style.less` — 主题样式源码，采用 LESS 编写。包含霓虹灯发光特效、✦ 星芒分割线、以及专门针对 MPE 优化的 markdown 样式。

---

## ⚙️ 启用与安装步骤

请按照以下步骤在 VSCode 的 Markdown Preview Enhanced 中配置并使用该主题：

1. **打开自定义样式配置文件**：
   * 在 VSCode 中，按 `Ctrl+Shift+P` (Windows) 或 `Cmd+Shift+P` (Mac) 打开命令面板。
   * 输入 `Markdown Preview Enhanced: Customize CSS`，在下拉选项中务必勾选或选择带有 **"(Global)" 全局** 标志的项（中文显示为 `MPE:自定义样式 (全局)`）。该命令会直接打开一个全局共享的 `style.less` 文件。
   * **MPE 全局配置文件夹路径参考**：
       * Windows: `~/.crossnote/`
       * Linux / WSL: `~/.local/state/crossnote/`

2. **替换样式内容**：
   * 复制本目录下 `style.less` 的全部内容，直接粘贴并覆盖到上一步打开的全局 `style.less` 文件中即可。

3. **预览**：
   * 在 VSCode 中打开任何 Markdown 文件。
   * 点击右上角的 MPE 预览按钮即可享受高对比度的 Tokyonight 风格预览。
