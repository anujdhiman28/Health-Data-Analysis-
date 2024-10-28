import tkinter as tk
from tkinter import filedialog, messagebox, Frame, Label
import pandas as pd
import matplotlib.pyplot as plt

class HealthDataAnalyzer:
    def __init__(self, master):
        self.master = master
        self.master.title("Health Data Analyzer")
        self.master.geometry("400x300")
        self.master.config(bg="#f0f0f0")  # Light gray background

        # Frame for buttons
        self.frame = Frame(master, bg="#f0f0f0")
        self.frame.pack(pady=20)

        # Title Label
        self.title_label = Label(master, text="Health Data Analyzer", font=("Helvetica", 16), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Upload button
        self.upload_button = tk.Button(self.frame, text="Upload CSV", command=self.upload_data, width=20, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.upload_button.pack(pady=10)

        # Statistics button
        self.stats_button = tk.Button(self.frame, text="Show Statistics", command=self.show_statistics, width=20, bg="#2196F3", fg="white", font=("Helvetica", 12))
        self.stats_button.pack(pady=10)

        # Visualize button
        self.visualize_button = tk.Button(self.frame, text="Visualize Data", command=self.visualize_data, width=20, bg="#FF5722", fg="white", font=("Helvetica", 12))
        self.visualize_button.pack(pady=10)

        self.data = None

    def upload_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                messagebox.showinfo("Success", "Data uploaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to upload data: {e}")

    def show_statistics(self):
        if self.data is not None:
            stats = self.data.describe()
            messagebox.showinfo("Statistics", stats.to_string())
        else:
            messagebox.showwarning("Warning", "No data uploaded!")

    def visualize_data(self):
        if self.data is not None:
            if 'age' in self.data.columns:
                plt.figure(figsize=(8, 6))
                plt.hist(self.data['age'], bins=10, edgecolor='black')
                plt.title('Age Distribution', fontsize=14)
                plt.xlabel('Age', fontsize=12)
                plt.ylabel('Frequency', fontsize=12)
                plt.grid(axis='y', alpha=0.75)
                plt.show()
            else:
                messagebox.showwarning("Warning", "'age' column not found in data.")
        else:
            messagebox.showwarning("Warning", "No data uploaded!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthDataAnalyzer(root)
    root.mainloop()
