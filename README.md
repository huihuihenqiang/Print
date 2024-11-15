# Print - Automated Text Typing Tool 🖥️
我之前一直思考，复制一段文字给程序，然后控制键盘自动打字这样的python包到底有什么用，这不是自娱自乐？直到我遇到了不能复制文字的输入框（科技写作实训作业）···
Print 是一个 Python 图形界面工具，可以从 `.txt` 文件中自动读取文本，并按设定的速度逐字输入到目标应用中。该工具特别适用于需要模拟缓慢或精确控制文本输入的场景。
## 打包好的软件在 Releases 中下载。
![图片](https://github.com/user-attachments/assets/9a299704-ebf6-4b06-a14a-82b212e22d21)

## 🎉 功能特点

- 📂 从 `.txt` 文件读取文本内容，并逐字输入到目标输入框中。（首先你要把自己想打的字复制到txt里面）
- ⏱️ 支持设置每个字符的输入间隔，输入速度可自定义。
- 🌐 支持自动切换到英文输入模式（用户可以选择启用）。
- 🛑 可通过快捷键 (`Ctrl + Shift + S`) 停止输入，方便控制。
- 💡 简单易用的图形界面，并提供友好的使用说明。

## 🛠️ 安装

Print 需要 Python 3 及以下几个库：

### 1. 下包运行

```bash
pip install pyautogui pynput keyboard
```
```bash
python print.py

```
🙌 贡献

欢迎提交 issues 和 pull requests，为项目改进和增加新功能！

💡 提示：本工具仅用于学习和合法用途，请勿用于任何违反平台或系统政策的操作。
