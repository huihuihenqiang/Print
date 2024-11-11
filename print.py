import time
import threading
from tkinter import Tk, Label, Entry, Button, Checkbutton, BooleanVar, filedialog, messagebox, StringVar, DoubleVar
from pynput.keyboard import Controller
import pyautogui
import keyboard

# 初始化键盘控制器
keyboard_controller = Controller()

# 全局变量，用于控制输入过程的停止
stop_typing = False


def switch_to_english_input():
    # 按下 Alt + Shift 或 Win + Space 以切换输入法
    pyautogui.hotkey('alt', 'shift')  # 或者使用 'win', 'space'


def type_text_slowly(text, char_delay=0.2):
    global stop_typing
    for char in text:
        if stop_typing:
            break
        keyboard_controller.type(char)
        time.sleep(char_delay)


def start_typing(file_path, char_delay):
    global stop_typing
    stop_typing = False  # 重置停止标志

    # 根据用户选择来切换输入法
    if need_switch.get():
        switch_to_english_input()

    # 从txt文件中读取内容
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_to_type = file.read()
    except FileNotFoundError:
        messagebox.showerror("错误", f"未找到文件：{file_path}")
        return

    # 固定5秒的准备时间
    response = messagebox.askokcancel("准备", "请点击确认后，在5秒内切换到目标输入框。")
    if response:
        time.sleep(5)  # 等待5秒
        type_text_slowly(text_to_type, char_delay)
    else:
        messagebox.showinfo("取消", "操作已取消。")


def start_typing_thread():
    file_path = file_path_var.get()
    char_delay = delay_var.get()
    if not file_path:
        messagebox.showerror("错误", "请选择一个文件")
        return
    threading.Thread(target=start_typing, args=(file_path, char_delay)).start()


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        file_path_var.set(file_path)


def stop_typing_action():
    global stop_typing
    stop_typing = True
    messagebox.showinfo("停止", "输入已停止。")


# 注册停止输入的快捷键
keyboard.add_hotkey('ctrl+shift+s', stop_typing_action)


# 创建 GUI 窗口
root = Tk()
root.title("自动文本输入器")

# 文件路径选择
file_path_var = StringVar()
Label(root, text="选择文件:").grid(row=0, column=0, padx=10, pady=10)
file_entry = Entry(root, textvariable=file_path_var, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=10)
Button(root, text="浏览", command=select_file).grid(row=0, column=2, padx=10, pady=10)

# 字符间隔时间设置
delay_var = DoubleVar(value=0.2)
Label(root, text="字符间隔时间 (秒):").grid(row=1, column=0, padx=10, pady=10)
delay_entry = Entry(root, textvariable=delay_var, width=10)
delay_entry.grid(row=1, column=1, padx=10, pady=10)

# 输入法切换选项
need_switch = BooleanVar()
Checkbutton(root, text="输入法非英文时请勾选", variable=need_switch).grid(row=2, column=0, padx=10, pady=10)

# 操作说明
instructions = (
    "说明：\n"
    "- 输入文件必须为 .txt 格式。\n"
    "- 开始输入后请勿随意移动鼠标和按键。\n"
    "- 若输入法为中文，请勾选切换输入法选项。\n"
    "- 停止输入快捷键：Ctrl + Shift + S"
)
Label(root, text=instructions, justify="left", fg="blue").grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# 开始按钮
start_button = Button(root, text="开始输入", command=start_typing_thread)
start_button.grid(row=4, column=1, pady=10)

# 运行 GUI 主循环
root.mainloop()
