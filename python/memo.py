import tkinter as tk
from tkinter import messagebox
import json

# メモを格納するリスト
memos = []

# メモを保存するファイル名
SAVE_FILE = "scouter_memo.json"

def save_memos():
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(memos, f, ensure_ascii=False, indent=4)

def load_memos():
    global memos
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            memos = json.load(f)
            update_list()
    except FileNotFoundError:
        memos = []

def add_memo():
    text = memo_entry.get()
    power = power_entry.get()
    if text and power.isdigit():
        memos.append((text, int(power)))
        update_list()
        save_memos()
        memo_entry.delete(0, tk.END)
        power_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("入力エラー", "メモと戦闘力(数値)を入力してください！")

def delete_memo():
    selected = memo_list.curselection()
    if selected:
        index = selected[0]
        del memos[index]
        update_list()
        save_memos()
    else:
        messagebox.showwarning("削除エラー", "削除するメモを選択してください！")

def update_list():
    memo_list.delete(0, tk.END)
    for text, power in sorted(memos, key=lambda x: x[1], reverse=True):
        memo_list.insert(tk.END, f"戦闘力 {power}: {text}")

# GUIのセットアップ
root = tk.Tk()
root.title("スカウター風メモアプリ")
root.geometry("550x500")
root.configure(bg="#002200")  # 背景を暗めの緑色に設定

# スカウター風の枠線を最背面に配置
canvas = tk.Canvas(root, width=550, height=500, bg="#002200", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_rectangle(10, 10, 540, 490, outline="#00FF00", width=2)  # 外枠

# ヘッダー
header_label = tk.Label(root, text="SCOUTER SYSTEM", fg="#00FF00", bg="#002200", font=("Courier", 16, "bold"))
header_label.place(x=180, y=10)

# 入力用フレーム
frame = tk.Frame(root, bg="#002200")
frame.place(x=50, y=50)

memo_label = tk.Label(frame, text="メモ:", fg="#00FF00", bg="#002200", font=("Courier", 12))
memo_label.grid(row=0, column=0, padx=5)

memo_entry = tk.Entry(frame, width=30, bg="#003300", fg="#00FF00", insertbackground="#00FF00", font=("Courier", 12))
memo_entry.grid(row=0, column=1, padx=5)

power_label = tk.Label(frame, text="戦闘力:", fg="#00FF00", bg="#002200", font=("Courier", 12))
power_label.grid(row=1, column=0, padx=5)

power_entry = tk.Entry(frame, width=5, bg="#003300", fg="#00FF00", insertbackground="#00FF00", font=("Courier", 12))
power_entry.grid(row=1, column=1, padx=5)

add_button = tk.Button(frame, text="追加", command=add_memo, bg="#006600", fg="#00FF00", font=("Courier", 12, "bold"), relief=tk.FLAT, borderwidth=0)
add_button.grid(row=1, column=2, padx=5)

# 削除ボタン
delete_button = tk.Button(root, text="選択したメモを削除", command=delete_memo, bg="#660000", fg="#FF0000", font=("Courier", 12, "bold"), relief=tk.FLAT, borderwidth=0)
delete_button.place(x=185, y=110)

# メモリストボックス
memo_list = tk.Listbox(root, width=49, height=15, bg="#001100", fg="#00FF00", font=("Courier", 12), selectbackground="#004400", selectforeground="#FFFFFF", relief=tk.FLAT, borderwidth=2, highlightbackground="#00FF00", highlightthickness=1)
memo_list.place(x=30, y=150)

# メモの読み込み
load_memos()

root.mainloop()
