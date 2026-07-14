# -*- coding: utf-8 -*-
"""
Telcat Theme Builder
Generates theme.css from theme-origin.css with unified color schemes and formatting.
All four schemes share the same key set (37 keys) and ordering for consistency.
"""

import re
import os

# Unified key order shared by all four schemes
UNIFIED_KEYS = [
    "bg-color", "text-color", "text-color-secondary", "border-color",
    "primary-color", "secondary-color", "accent-color",
    "light-deep", "light-light", "light-lighter", "light-pale",
    "glow-color", "hover-background-color", "select-text-bg-color",
    "link-color", "link-hover-color",
    "h1-underline-color", "h2-bg-image", "h2-bg-image-hover",
    "h2-bg-gradient", "h2-shadow-color", "h2-shadow-hover",
    "text-bold",
    "code-block-bg", "code-block-header-bg", "code-normal",
    "code-keyword", "code-function", "code-string", "code-comment",
    "code-property", "code-value", "code-punctuation",
    "code-tag", "code-operator", "code-important",
    "list-hover-color",
]

# Define color schemes — all share the same 37 keys in UNIFIED_KEYS order
SCHEMES = {
    "tokyonight-storm": {
        "bg-color": "#24283b",
        "text-color": "#c0caf5",
        "text-color-secondary": "#a9b1d6",
        "border-color": "#3b4261",
        "primary-color": "#7aa2f7",
        "secondary-color": "#bb9af3",
        "accent-color": "#7dcfff",
        "light-deep": "var(--text-color)",
        "light-light": "var(--accent-color)",
        "light-lighter": "var(--accent-color)",
        "light-pale": "var(--bg-color)",
        "glow-color": "rgba(122, 162, 247, 0.6)",
        "hover-background-color": "rgb(122, 162, 247)",
        "select-text-bg-color": "rgba(122, 162, 247, 0.3)",
        "link-color": "#ff9e64",
        "link-hover-color": "#7dcfff",
        "h1-underline-color": "var(--primary-color)",
        "h2-bg-image": "radial-gradient(ellipse at center bottom, rgba(122, 162, 247, 0.15), transparent 70%)",
        "h2-bg-image-hover": "radial-gradient(ellipse at center bottom, rgba(122, 162, 247, 0.25), transparent 60%)",
        "h2-bg-gradient": "linear-gradient(to right, var(--light-light), var(--primary-color), var(--light-light))",
        "h2-shadow-color": "rgba(122, 162, 247, 0.15)",
        "h2-shadow-hover": "rgba(122, 162, 247, 0.35)",
        "text-bold": "var(--light-deep)",
        "code-block-bg": "#1f2335",
        "code-block-header-bg": "color-mix(in srgb, var(--primary-color), transparent 92%)",
        "code-normal": "var(--text-color)",
        "code-keyword": "#bb9af3",
        "code-function": "#7aa2f7",
        "code-string": "#9ece6a",
        "code-comment": "#565f89",
        "code-property": "#7dcfff",
        "code-value": "#ff9e64",
        "code-punctuation": "#c0caf5",
        "code-tag": "#f7768e",
        "code-operator": "#89ddff",
        "code-important": "#bb9af3",
        "list-hover-color": "#7dcfff",
    },
    "github-dark": {
        "bg-color": "#0d1117",
        "text-color": "#c9d1d9",
        "text-color-secondary": "#8b949e",
        "border-color": "#30363d",
        "primary-color": "#58a6ff",
        "secondary-color": "#bc8cff",
        "accent-color": "#1f6feb",
        "light-deep": "var(--text-color)",
        "light-light": "var(--accent-color)",
        "light-lighter": "var(--accent-color)",
        "light-pale": "var(--bg-color)",
        "glow-color": "rgba(88, 166, 255, 0.4)",
        "hover-background-color": "rgb(88, 166, 255)",
        "select-text-bg-color": "rgba(88, 166, 255, 0.25)",
        "link-color": "#58a6ff",
        "link-hover-color": "#79c0ff",
        "h1-underline-color": "var(--primary-color)",
        "h2-bg-image": "radial-gradient(ellipse at center bottom, rgba(88, 166, 255, 0.15), transparent 70%)",
        "h2-bg-image-hover": "radial-gradient(ellipse at center bottom, rgba(88, 166, 255, 0.25), transparent 60%)",
        "h2-bg-gradient": "linear-gradient(to right, var(--light-light), var(--primary-color), var(--light-light))",
        "h2-shadow-color": "rgba(88, 166, 255, 0.15)",
        "h2-shadow-hover": "rgba(88, 166, 255, 0.35)",
        "text-bold": "var(--light-deep)",
        "code-block-bg": "#161b22",
        "code-block-header-bg": "color-mix(in srgb, var(--primary-color), transparent 92%)",
        "code-normal": "var(--text-color)",
        "code-keyword": "#ff7b72",
        "code-function": "#d2a8ff",
        "code-string": "#a5d6ff",
        "code-comment": "#8b949e",
        "code-property": "#79c0ff",
        "code-value": "#79c0ff",
        "code-punctuation": "#c9d1d9",
        "code-tag": "#7ee787",
        "code-operator": "#ff7b72",
        "code-important": "#d2a8ff",
        "list-hover-color": "#7ee787",
    },
    "tokyonight-day": {
        "bg-color": "#e1e2e7",
        "text-color": "#343b58",
        "text-color-secondary": "#687089",
        "border-color": "color-mix(in srgb, var(--primary-color), transparent 60%)",
        "primary-color": "#385ef2",
        "secondary-color": "#9854f1",
        "accent-color": "#007197",
        "light-deep": "#1f3eac",
        "light-light": "#7aa2f7",
        "light-lighter": "#b4f9f8",
        "light-pale": "#e9eaf0",
        "glow-color": "rgba(56, 94, 242, 0.5)",
        "hover-background-color": "rgb(56, 94, 242)",
        "select-text-bg-color": "rgba(56, 94, 242, 0.25)",
        "link-color": "#b15c00",
        "link-hover-color": "#007197",
        "h1-underline-color": "var(--primary-color)",
        "h2-bg-image": "radial-gradient(ellipse at center bottom, rgba(56, 94, 242, 0.15), transparent 70%)",
        "h2-bg-image-hover": "radial-gradient(ellipse at center bottom, rgba(56, 94, 242, 0.25), transparent 60%)",
        "h2-bg-gradient": "linear-gradient(to right, var(--light-light), var(--primary-color), var(--light-light))",
        "h2-shadow-color": "rgba(56, 94, 242, 0.15)",
        "h2-shadow-hover": "rgba(56, 94, 242, 0.35)",
        "text-bold": "var(--light-deep)",
        "code-block-bg": "#e9eaf0",
        "code-block-header-bg": "color-mix(in srgb, var(--primary-color), transparent 92%)",
        "code-normal": "#343b58",
        "code-keyword": "#9854f1",
        "code-function": "#385ef2",
        "code-string": "#587539",
        "code-comment": "#848cb5",
        "code-property": "#385ef2",
        "code-value": "#b15c00",
        "code-punctuation": "#343b58",
        "code-tag": "#f52a65",
        "code-operator": "#007197",
        "code-important": "#9854f1",
        "list-hover-color": "#1689a0",
    },
    "github-light": {
        "bg-color": "#ffffff",
        "text-color": "#24292f",
        "text-color-secondary": "#57606a",
        "border-color": "color-mix(in srgb, var(--primary-color), transparent 70%)",
        "primary-color": "#0969da",
        "secondary-color": "#8250df",
        "accent-color": "#0969da",
        "light-deep": "#1a1f26",
        "light-light": "#58a6ff",
        "light-lighter": "#ddf4ff",
        "light-pale": "#f6f8fa",
        "glow-color": "rgba(9, 105, 218, 0.4)",
        "hover-background-color": "rgb(9, 105, 218)",
        "select-text-bg-color": "rgba(9, 105, 218, 0.2)",
        "link-color": "#0969da",
        "link-hover-color": "#0a3069",
        "h1-underline-color": "var(--primary-color)",
        "h2-bg-image": "radial-gradient(ellipse at center bottom, rgba(9, 105, 218, 0.15), transparent 70%)",
        "h2-bg-image-hover": "radial-gradient(ellipse at center bottom, rgba(9, 105, 218, 0.25), transparent 60%)",
        "h2-bg-gradient": "linear-gradient(to right, var(--light-light), var(--primary-color), var(--light-light))",
        "h2-shadow-color": "rgba(9, 105, 218, 0.15)",
        "h2-shadow-hover": "rgba(9, 105, 218, 0.35)",
        "text-bold": "var(--light-deep)",
        "code-block-bg": "#f6f8fa",
        "code-block-header-bg": "color-mix(in srgb, var(--primary-color), transparent 94%)",
        "code-normal": "#24292f",
        "code-keyword": "#cf222e",
        "code-function": "#8250df",
        "code-string": "#0a3069",
        "code-comment": "#6e7781",
        "code-property": "#0550ae",
        "code-value": "#0550ae",
        "code-punctuation": "#24292f",
        "code-tag": "#116329",
        "code-operator": "#cf222e",
        "code-important": "#8250df",
        "list-hover-color": "#116329",
    },
}


def format_variables(vars_dict):
    """Formats a dictionary into aligned CSS custom properties following UNIFIED_KEYS order."""
    lines = []
    max_len = max(len(k) for k in UNIFIED_KEYS)
    for k in UNIFIED_KEYS:
        padding = " " * (max_len - len(k))
        lines.append(f"  --{k}:{padding} {vars_dict[k]};")
    # Remove trailing semicolon from last line to match the original convention
    lines[-1] = lines[-1].rstrip(";")
    return "\n".join(lines)


def build_theme():
    origin_path = "obsidian/theme-origin.css"
    dest_path = "obsidian/theme.css"

    if not os.path.exists(origin_path):
        print(f"Error: {origin_path} does not exist.")
        return

    with open(origin_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Define the replacement selectors and their corresponding scheme configuration
    replacements = [
        (
            r"(/\* Tokyonight Storm \(Default Dark Mode\) \*/\s*body\.theme-dark\.theme-dark-tokyonight,\s*body\.theme-dark:not\(\.theme-dark-github\)\s*\{)([^}]*?)(\})",
            SCHEMES["tokyonight-storm"]
        ),
        (
            r"(/\* GitHub Dark \*/\s*body\.theme-dark\.theme-dark-github\s*\{)([^}]*?)(\})",
            SCHEMES["github-dark"]
        ),
        (
            r"(/\* Tokyonight Day \(Default Light Mode\) \*/\s*body\.theme-light\.theme-light-tokyonight,\s*body\.theme-light:not\(\.theme-light-github\)\s*\{)([^}]*?)(\})",
            SCHEMES["tokyonight-day"]
        ),
        (
            r"(/\* GitHub Light \*/\s*body\.theme-light\.theme-light-github\s*\{)([^}]*?)(\})",
            SCHEMES["github-light"]
        )
    ]

    new_content = content
    for pattern, scheme_vars in replacements:
        formatted = format_variables(scheme_vars)

        def repl(match):
            header = match.group(1)
            footer = match.group(3)
            return f"{header}\n{formatted}\n{footer}"

        new_content = re.sub(pattern, repl, new_content, flags=re.DOTALL)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Successfully generated {dest_path} with updated and formatted schemes.")


if __name__ == "__main__":
    build_theme()
