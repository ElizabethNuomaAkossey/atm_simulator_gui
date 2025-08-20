import tkinter as tk

def _show_deposit_ui(root):
    frame = tk.Frame(root, padx=10, pady =10)
    frame.grid(row=0, column=0, sticky="nsw")

    label = tk.Label(frame, text="Please enter deposit amount")
    label.grid(column=1, row=1)

    entry = tk.Entry(frame, width=50)
    entry.grid(column=1, row=2)

    button = tk.Button(frame, text="Proceed")
    button.grid(column=2, row=2)

    frame.tkraise()