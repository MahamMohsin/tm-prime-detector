#gui.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from toafinal import is_prime_tm  #Importing the function from the logic file

def check_prime():
    try:
        num = int(entry.get())
        if is_prime_tm(num):
            result_label.config(text=f"{num} is a Prime Number ✅", fg="green")
        else:
            result_label.config(text=f"{num} is NOT a Prime Number ❌", fg="red")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def on_focus_in(event):
    """Clear the entry box when user clicks/focuses on it."""
    if entry.get() == "enter number":
        entry.delete(0, tk.END)  #Clear the current text

def on_focus_out(event):
    """Restore the placeholder text if the user leaves the entry box empty."""
    if entry.get() == "":
        entry.insert(0, "enter number") 
        
#GUI Setup
root = tk.Tk()
root.title("Prime Checker (Turing Machine)")
root.configure(bg='#3c3c83')  #Dark blue background
root.geometry("600x300")

#Title
title = tk.Label(root, text="PRIME NUMBER CHECKER", font=("Comic Sans MS", 28, "bold"), bg='#3c3c83', fg='white')
title.pack(pady=40)

#Input Frame
frame = tk.Frame(root, bg='#3c3c83')
frame.pack()

#Entry widget with placeholder
entry = tk.Entry(frame, font=("Courier", 16), width=25, justify='center', bg='#b4b4fc')
entry.insert(0, "enter number")  # Default text as placeholder
entry.pack(side=tk.LEFT, padx=10, ipady=5)

#Bind events for focus-in and focus-out
entry.bind("<FocusIn>", on_focus_in)  #When the user clicks in the entry box
entry.bind("<FocusOut>", on_focus_out)  #When the user clicks outside the entry box

#Loading the arrow icon
arrow_img = Image.open("arrow.png")
arrow_img = arrow_img.resize((40, 40), Image.Resampling.LANCZOS)
arrow_icon = ImageTk.PhotoImage(arrow_img)

#Button with icon
submit_btn = tk.Button(frame, image=arrow_icon, command=check_prime, bg="#bebaff", borderwidth=0)
submit_btn.pack(side=tk.LEFT)


#Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg='#3c3c83', fg='white')
result_label.pack(pady=10)

#Footer
footer = tk.Label(root, text="a project by:   zunaira ali    maham mohsin    nehdia shah", font=("Courier", 10),
                  bg="#bebaff", fg="#3b3486")
footer.pack(side=tk.BOTTOM, fill=tk.X)
root.mainloop()