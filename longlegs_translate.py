import tkinter as tk
from tkinter import messagebox

# Dictionary and Function of Longlegs to ENG
def translate_to_english(text):
    custom_to_english = {
        '•': 'A', 
        '//': 'B', 
        'V': 'C', 
        '⊂': 'D', 
        '—': 'E', 
        'ᒕ': 'F', 
        '\\\\': 'G', 
        'Ո': 'H', 
        '：': 'I', 
        '⊓': 'J', 
        '⅂': 'K', 
        'Ↄ': 'L', 
        'ꇓ': 'M', 
        '⊥': 'N', 
        'L': 'O', 
        '⨪': 'P', 
        '///': 'Q', 
        'Ω': 'R', 
        'ᘰ': 'S', 
        '⨀': 'T', 
        '⏁': 'U', 
        '⊘': 'V', 
        '⊔': 'W', 
        '⨲': 'X', 
        '∴': 'Y', 
        '＋': 'Z'
    }
    
    # Sort the dictionary by key length in descending order to match longer symbols first
    sorted_custom_to_english = dict(sorted(custom_to_english.items(), key=lambda item: len(item[0]), reverse=True))

    translated_text = text
    for symbol, letter in sorted_custom_to_english.items():
        translated_text = translated_text.replace(symbol, letter)
    
    return translated_text

# Dictionary and Function of ENG to Longlegs
def translate_to_custom(text):
    english_to_custom = {
        'A': '•', 
        'B': '//', 
        'C': 'V', 
        'D': '⊂', 
        'E': '—', 
        'F': 'ᒕ', 
        'G': '\\\\', 
        'H': 'Ո', 
        'I': '：', 
        'J': '⊓', 
        'K': '⅂', 
        'L': 'Ↄ', 
        'M': 'ꇓ', 
        'N': '⊥', 
        'O': 'L', 
        'P': '⨪', 
        'Q': '///', 
        'R': 'Ω', 
        'S': 'ᘰ', 
        'T': '⨀', 
        'U': '⏁', 
        'V': '⊘', 
        'W': '⊔', 
        'X': '⨲', 
        'Y': '∴', 
        'Z': '＋'
    }
    
    translated_text = text
    for letter, symbol in english_to_custom.items():
        translated_text = translated_text.replace(letter, symbol)

    return translated_text

# Functions for button actions
def translate_longlegs_to_english():
    custom_text = input_text.get("1.0", "end-1c")
    translated_text = translate_to_english(custom_text)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated_text)
    output_text.config(state=tk.DISABLED)

def translate_english_to_longlegs():
    english_text = input_text.get("1.0", "end-1c").upper()
    translated_text = translate_to_custom(english_text)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated_text)
    output_text.config(state=tk.DISABLED)

def close_program():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Long Legs Translate")
window.geometry("600x400")

# Create and place the input text widget
input_label = tk.Label(window, text="Input:")
input_label.pack()
input_text = tk.Text(window, height=10)
input_text.pack()

# Create and place the output text widget
output_label = tk.Label(window, text="Output:")
output_label.pack()
output_text = tk.Text(window, height=10, state=tk.DISABLED)
output_text.pack()

# Create and place the buttons
button_frame = tk.Frame(window)
button_frame.pack()

translate_longlegs_button = tk.Button(button_frame, text="LongLegs > English", command=translate_longlegs_to_english)
translate_longlegs_button.pack(side=tk.LEFT, padx=10, pady=10)

translate_english_button = tk.Button(button_frame, text="English > LongLegs", command=translate_english_to_longlegs)
translate_english_button.pack(side=tk.LEFT, padx=10, pady=10)

close_button = tk.Button(button_frame, text="Close", command=close_program)
close_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
