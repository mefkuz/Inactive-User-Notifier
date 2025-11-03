import argparse, tkinter as tk
from tkinter import messagebox
from config import load_config, save_config

def gui():
    cfg = load_config()
    root = tk.Tk()
    root.title("Inactive User Notifier")
    root.geometry("400x400")

    tk.Label(root, text="Inactivity threshold (days)").pack()
    days = tk.StringVar(value=str(cfg["threshold_days"]))
    tk.Entry(root, textvariable=days).pack()

    tk.Label(root, text="Notification message").pack()
    msg = tk.Text(root, height=4)
    msg.insert("1.0", cfg["message"])
    msg.pack(fill="x", padx=10)

    tk.Label(root, text="Recipients (comma-separated)").pack()
    contacts_var = tk.StringVar(value=", ".join(cfg.get("contacts", [])))
    tk.Entry(root, textvariable=contacts_var).pack(fill="x", padx=10)

    def save():
        cfg["threshold_days"] = int(days.get())
        cfg["message"] = msg.get("1.0", "end").strip()
        cfg["contacts"] = [x.strip() for x in contacts_var.get().split(",") if x.strip()]
        save_config(cfg)
        messagebox.showinfo("Saved", "Settings saved successfully.")

    tk.Button(root, text="Save", command=save).pack(pady=10)
    root.mainloop()

def cli():
    cfg = load_config()
    print(f"Current threshold: {cfg['threshold_days']} days")
    new_days = input("New threshold (Enter to skip): ")
    if new_days.strip():
        cfg["threshold_days"] = int(new_days)
    new_msg = input("New message (Enter to skip): ")
    if new_msg.strip():
        cfg["message"] = new_msg
    save_config(cfg)
    print("Config updated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gui", action="store_true")
    parser.add_argument("--cli", action="store_true")
    args = parser.parse_args()

    if args.gui:
        gui()
    elif args.cli:
        cli()
    else:
        print("Use --gui or --cli")
