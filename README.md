# 🖥️ Inactive User Notifier

A lightweight Python app that monitors when the user last logged in to their computer.
If the user hasn’t logged in for a specified number of days, it automatically sends a prewritten email message to selected contacts.

## ✨ Features
✅ Tracks the last login timestamp  
✅ Custom inactivity threshold (e.g., 40 days)  
✅ GUI (Tkinter) and CLI setup options  
✅ Automatic email sending via SMTP  
✅ GitHub Actions support for daily automated checks

## ⚙️ Installation
```bash
git clone https://github.com/mefkuz/inactive-user-notifier.git
cd inactive-user-notifier
pip install -r requirements.txt
```

## 🧰 Usage

### GUI
```bash
python src/app.py --gui
```

### CLI
```bash
python src/app.py --cli
```

### Record login
```bash
python src/heartbeat.py
```

### Check inactivity
```bash
python src/checker.py
```

## 🧱 License

MIT License
