# 🧠 Turing Machine Prime Checker

A Python-based simulation of a Turing Machine that checks whether a number is prime — complete with a user-friendly graphical interface built using Tkinter.

---
## 🎯 Objective

To simulate the working of a Turing Machine that checks whether a number is prime using unary representation, and to provide a visual and interactive interface for users.

---

## 🛠 Technologies Used

- Python 3.x  
- Tkinter (for GUI)  
- Pillow (PIL) for image handling  
- `defaultdict` for simulating the Turing Machine tape

---

## 📁 File Structure

- `toafinal.py` – Core logic that simulates the Turing Machine  
- `gui.py` – Tkinter-based GUI module  
- `arrow.png` – Arrow icon used in GUI  
- `__pycache__/` – Auto-generated compiled files

---

## ⚙️ How It Works

1. The number is converted into unary (e.g., `5 → 11111`)
2. A simulated Turing Machine tries dividing it by integers from 2 to n-1
3. If divisible → Not Prime  
   If not divisible → Prime
4. GUI displays the result with color-coded feedback

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- Install Pillow:
  ```bash
  pip install pillow
### ▶️ Launch GUI
```bash
  python gui.py
