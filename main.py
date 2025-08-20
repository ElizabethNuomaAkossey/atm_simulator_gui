import tkinter as tk
from commands import check_balance
from deposit import _show_deposit_ui

# Create the main window
root = tk.Tk()

# add the title to the main window
root.title("ATM Simulator")
# create a tk frame for main window
frame = tk.Frame(root, padx=50, pady=50)
frame.grid(row=0, column=0, sticky="nsew")

# frame.grid_propagate(0)

# account number entry label
label = tk.Label(frame,text="Account Number")
label.grid(column=1,row=1)

# Account number Entry
account_number_entry = tk.Entry(frame, width=50)
account_number_entry.grid(column=2, row=1, padx=50)

# Add check balance button
check_balance_btn = tk.Button(frame, text="Check Balance", command=lambda: check_balance(account_number=account_number_entry.get()))
check_balance_btn.grid(column=2, row=2)

# Add Deposit button
deposit_btn = tk.Button(frame, 
                        text="Deposit",
                        command=lambda: _show_deposit_ui(root))
deposit_btn.grid(column=2, row=3)
# deposit_btn.pack(side="top")
# open the main window
root.mainloop()