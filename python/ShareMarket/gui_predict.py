import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_analysis():
    # Retrieve values from entry widgets
    values = [float(entry.get()) for entry in entry_widgets]

    # Calculate moving averages
    k = np.mean(values)
    l = np.mean(values[:2])
    m = np.mean(values[:3])
    n = np.mean(values[:4])
    o = np.mean(values[:5])
    p = np.mean(values[:6])
    q = np.mean(values[:7])
    r = np.mean(values[:8])
    s = np.mean(values[:9])
    t = np.mean(values[:10])

    # Calculate max and min
    max_val = np.max([k, l, m, n, o, p, q, r, s, t])
    min_val = np.min([k, l, m, n, o, p, q, r, s, t])

    # Calculate Bollinger Bands
    window = 10
    sma = np.mean(values[-window:])
    std_dev = np.std(values[-window:])
    upper_band_factor_2 = sma + (2 * std_dev)
    lower_band_factor_2 = sma - (2 * std_dev)

    # Calculate Stochastic Oscillator
    highest_high = np.max(values)
    lowest_low = np.min(values)
    stochastic_k = ((values[-1] - lowest_low) / (highest_high - lowest_low)) * 100

    # Show analysis results in message box
    result_text = f"Moving Averages:\nK: {k:.5f}\nL: {l:.5f}\nM: {m:.5f}\nN: {n:.5f}\nO: {o:.5f}\n" \
                  f"P: {p:.5f}\nQ: {q:.5f}\nR: {r:.5f}\nS: {s:.5f}\nT: {t:.5f}\n\n" \
                  f"Max Value: {max_val:.5f}\nMin Value: {min_val:.5f}\n\n" \
                  f"Bollinger Bands:\nUpper Band: {upper_band_factor_2:.5f}\nLower Band: {lower_band_factor_2:.5f}\n\n" \
                  f"Stochastic Oscillator: {stochastic_k:.2f}"
    messagebox.showinfo("Stock Analysis Result", result_text)

root = tk.Tk()
root.title("Stock Analysis")
root.geometry("400x400")

label = tk.Label(root, text="Enter 10 Stock Prices:", font=("Arial", 12))
label.pack(pady=10)

# Entry widgets for user input
entry_widgets = []
for i in range(10):
    entry_label = tk.Label(root, text=f"Price {i+1}:")
    entry_label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entry_widgets.append(entry)

# Button to calculate analysis
calculate_button = tk.Button(root, text="Calculate Analysis", command=calculate_analysis)
calculate_button.pack(pady=10)

root.mainloop()
