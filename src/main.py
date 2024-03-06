import tkinter as tk
import tkinter.filedialog as tkf
import tkinter.messagebox as tkm
import random
import datetime


def opening():
    global menu_arr
    try:
        menu_arr.clear()
        with open(tkf.askopenfilename(), "r", encoding="UTF-8") as fin:
            for line in fin.readlines():
                menu_arr.append(line.strip())
    except IOError:
        tkm.showinfo("今晚吃啥", "未指定文件！")
    except UnicodeError:
        tkm.showwarning("今晚吃啥", "不支持的文件格式/编码！")
    except Exception:
        tkm.showerror("今晚吃啥", "未知错误！")
    else:
        tkm.showinfo("今晚吃啥", "读取成功！")


def selecting():
    global dinner_str, menu_arr
    if len(menu_arr) == 0:
        return
    idx = random.randint(0, len(menu_arr) - 1)
    dinner_str.set(menu_arr[idx])


def saving():
    global dinner_str
    try:
        with open(tkf.askopenfilename(), "a", encoding="UTF-8") as fout:
            fout.write(datetime.date.today().strftime("%Y-%m-%d") + " 吃了 " + dinner_str.get() + "\n")
    except IOError:
        tkm.showinfo("今晚吃啥", "未指定文件！")
    except Exception:
        tkm.showerror("今晚吃啥", "未知错误！")
    else:
        tkm.showinfo("今晚吃啥", "记录成功！")


root = tk.Tk()
root.title("今晚吃啥")
menu_arr = []
dinner_str = tk.StringVar()
dinner_str.set("?")
tk.Label(root, font=("隶书", 20), textvariable=dinner_str).grid(column=0, columnspan=3, row=0)
tk.Button(root, text="读取菜单", command=opening).grid(column=0, row=1, ipadx=10)
tk.Button(root, text="今晚吃啥", command=selecting).grid(column=1, row=1, ipadx=10)
tk.Button(root, text="写进日志", command=saving).grid(column=2, row=1, ipadx=10)
root.mainloop()
