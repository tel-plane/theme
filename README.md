# 🎨 多平台主题集合 (Multi-Platform Theme Collection)

本仓库提供了一套统一设计语言的 Tokyonight 与 GitHub 调色板主题，适配了三种不同的编辑器与预览界面：

1. **Obsidian** — `Telcat` 玻璃拟态主题 (CSS + Style Settings 配置)。
2. **VSCode (Markdown Preview Enhanced)** — `Tokyonight Storm` 预览主题 (LESS)。
3. **Cherry Studio** — 支持浅色/暗色自动切换的 `Tokyonight` 主题 (CSS)。

---

## 📂 目录结构

*   `obsidian/` — Obsidian 的 `Telcat` 主题源码及构建脚本。
*   `VSCode/Tokyonight_storm/` — VSCode Markdown Preview Enhanced 插件的主题配置。
*   `cherry_studio/` — Cherry Studio 客户端的主题配置文件。
*   `markdown元素对照/` — Markdown 渲染效果测试样例与对照参考文档。

---

## 🛠️ 构建与开发

Obsidian 主题的调色板和样式使用 Python 构建脚本统一管理。修改 `obsidian/theme-origin.css` 后，可以通过以下命令重新生成发布版本：

```bash
python obsidian/build_theme.py
```

其他平台的主题为手动适配版本，无需编译。

---

## 🙏 致谢 (Acknowledgments)

本项目的 Obsidian `Telcat` 主题基于 [Phycat Theme](https://github.com/sumruler/obsidian-theme-phycat) (作者: sumruler) 进行二次开发与定制，感谢原作者优秀的开源工作。
