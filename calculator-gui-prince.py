#Calculator using Tkinter
# Created a modern, colorful calculator with a sleek design.

import tkinter as tk

def press(key):
    """Appends the pressed key to the input field."""
    entry.insert(tk.END, key)

def clear():
    """Clears the entire input field."""
    entry.delete(0, tk.END)

def backspace():
    """Deletes the last character from the input field."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    """Evaluates the expression and shows the result, handles errors."""
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
btn_colors = {
    'C': '#ff4c4c',  
    '⌫': '#ff9900',
    '=': '#33cc33',      
    '/': '#cc99ff', '*': '#cc99ff', '-': '#cc99ff', '+': '#cc99ff',
    '%': '#cc99ff', '(': '#cc99ff', ')': '#cc99ff'
}

window = tk.Tk()
window.title("🎨 Calculator")
window.geometry("360x500")
window.config(bg="#1e1e1e") 


entry = tk.Entry(window, font=("Segoe UI", 22), bg="#2d2d2d",
                 fg="white", bd=0, justify='right')
entry.pack(padx=20, pady=20, fill='both')

buttons = [
    ['C', '⌫', '(', ')'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# --- Button rendering ---
for row_values in buttons:
    row = tk.Frame(window, bg="#1e1e1e")
    row.pack(expand=True, fill='both', padx=5, pady=3)
    for btn_text in row_values:
        action = (
            clear if btn_text == 'C' else
            backspace if btn_text == '⌫' else
            calculate if btn_text == '=' else
            lambda val=btn_text: press(val)
        )

        bg_color = btn_colors.get(btn_text, "#cccccc")  
        fg_color = "#1e1e1e" if btn_text not in ['C', '⌫', '='] else "white"

        btn = tk.Button(
            row, text=btn_text, font=("Segoe UI", 16),
            bg=bg_color, fg=fg_color, relief='flat',
            activebackground="#aaaaaa",
            padx=10, pady=15, command=action
        )
        btn.pack(side='left', expand=True, fill='both', padx=4, pady=4)

# --- Run the app ---
window.mainloop()

