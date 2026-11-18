# -*- coding: utf-8 -*-
"""
自転車交通安全アプリ用 画像リネームツール

使い方：
1. このPythonファイルを実行
2. 「危険な場面」と「想定される危険」の画像を順番に選択
3. 自動的に
   assets/safety/01_signal.jpg
   assets/safety/01_signal_result.jpg
   ...
   assets/safety/18_insurance.jpg
   assets/safety/18_insurance_result.jpg
   の名前で保存されます。

画像は JPG / JPEG / PNG / WEBP に対応。
元画像は変更せず、保存先にコピーします。
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import shutil

ITEMS = [
    ("signal", "信号無視"),
    ("stop", "一時停止"),
    ("left", "右側通行・逆走"),
    ("sidewalk", "歩道での速度"),
    ("right_turn", "二段階右折"),
    ("smartphone", "スマホながら運転"),
    ("umbrella", "傘さし運転"),
    ("earphone", "イヤホン"),
    ("two_people", "二人乗り"),
    ("drinking", "飲酒運転"),
    ("parallel", "並進"),
    ("brake", "ブレーキ点検"),
    ("light", "夜間ライト"),
    ("luggage", "荷物の固定"),
    ("clothes", "服装・フットウェア"),
    ("helmet", "ヘルメット"),
    ("accident", "事故対応"),
    ("insurance", "自転車保険"),
]

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "assets" / "safety"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

selected = [None] * 36


def choose_image(slot):
    path = filedialog.askopenfilename(
        title="画像を選択してください",
        filetypes=[
            ("画像ファイル", "*.jpg *.jpeg *.png *.webp"),
            ("すべてのファイル", "*.*"),
        ],
    )
    if path:
        selected[slot] = Path(path)
        update_labels()


def update_labels():
    for i, label in enumerate(labels):
        p = selected[i]
        label.config(text=p.name if p else "未選択")


def output_name(index, result=False):
    num = index + 1
    key = ITEMS[index][0]
    return f"{num:02d}_{key}{'_result' if result else ''}.jpg"


def save_all():
    missing = []
    for i in range(18):
        if selected[i * 2] is None:
            missing.append(f"{i+1}. {ITEMS[i][1]}：危険な場面")
        if selected[i * 2 + 1] is None:
            missing.append(f"{i+1}. {ITEMS[i][1]}：想定される危険")

    if missing:
        messagebox.showwarning(
            "画像が足りません",
            "未選択の画像があります。\n\n" + "\n".join(missing[:10])
            + ("\n…" if len(missing) > 10 else "")
        )
        return

    for i in range(18):
        danger = selected[i * 2]
        result = selected[i * 2 + 1]

        # JPGとして保存。元画像がPNG等でも、ここでは拡張子だけを変えず
        # shutil.copy2でそのままコピーし、ファイル名を.jpgにする。
        # 画像形式までJPGへ変換したい場合はPillow版を使ってください。
        shutil.copy2(danger, OUTPUT_DIR / output_name(i, False))
        shutil.copy2(result, OUTPUT_DIR / output_name(i, True))

    messagebox.showinfo(
        "完了",
        f"18項目・36枚の画像を保存しました。\n\n保存先：\n{OUTPUT_DIR}"
    )


root = tk.Tk()
root.title("自転車交通安全｜画像ファイル名自動作成")
root.geometry("900x760")

title = tk.Label(
    root,
    text="自転車交通安全アプリ｜画像ファイル名自動作成",
    font=("Arial", 18, "bold"),
)
title.pack(pady=(15, 5))

desc = tk.Label(
    root,
    text="各項目について「危険な場面」→「想定される危険」の順に画像を選択してください。",
    font=("Arial", 11),
)
desc.pack(pady=(0, 12))

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=15)

headers = ["No.", "項目", "危険な場面", "想定される危険"]
for c, h in enumerate(headers):
    tk.Label(frame, text=h, font=("Arial", 10, "bold")).grid(
        row=0, column=c, padx=6, pady=5, sticky="w"
    )

labels = []

for i, (key, name) in enumerate(ITEMS):
    r = i + 1

    tk.Label(frame, text=f"{i+1:02d}").grid(row=r, column=0, padx=6, pady=4)
    tk.Label(frame, text=name, anchor="w", width=20).grid(
        row=r, column=1, padx=6, pady=4, sticky="w"
    )

    l1 = tk.Label(frame, text="未選択", width=25, anchor="w", fg="#666")
    l1.grid(row=r, column=2, padx=6, pady=4)
    labels.append(l1)

    tk.Button(
        frame,
        text="画像を選択",
        command=lambda slot=i * 2: choose_image(slot),
    ).grid(row=r, column=2, padx=6, pady=4, sticky="e")

    l2 = tk.Label(frame, text="未選択", width=25, anchor="w", fg="#666")
    l2.grid(row=r, column=3, padx=6, pady=4)
    labels.append(l2)

    tk.Button(
        frame,
        text="画像を選択",
        command=lambda slot=i * 2 + 1: choose_image(slot),
    ).grid(row=r, column=3, padx=6, pady=4, sticky="e")

bottom = tk.Frame(root)
bottom.pack(pady=15)

tk.Button(
    bottom,
    text="36枚を自動保存",
    command=save_all,
    font=("Arial", 13, "bold"),
    padx=25,
    pady=10,
).pack(side="left", padx=8)

tk.Button(
    bottom,
    text="閉じる",
    command=root.destroy,
    padx=20,
    pady=10,
).pack(side="left", padx=8)

root.mainloop()
