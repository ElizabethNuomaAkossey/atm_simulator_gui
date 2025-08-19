import tkinter as tk
from commands import check_balance

# Create the main window
root = tk.Tk()

# add the title to the main window
root.title("ATM Simulator")
# specify the main window size
root.geometry("500x400")

# Account number Entry

account_number_entry = tk.Entry(root, width=50)
account_number_entry.pack(side="top")

# Add check balance button
check_balance_btn = tk.Button(root, text="Check Balance", command=lambda: check_balance(account_number=account_number_entry.get()))
check_balance_btn.pack(side="top")

# Add Deposit button
deposit_btn = tk.Button(root, text="Deposit")
deposit_btn.pack(side="top")
# open the main window
root.mainloop()