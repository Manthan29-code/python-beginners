import os
import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

def download_pdfs():
    sub_code = entry_sub_code.get()
    sub_name = entry_sub_name.get()

    if not sub_code or not sub_name:
        messagebox.showwarning("Input Error", "Please enter both subject code and subject name.")
        return

    curr_dir = os.getcwd()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Starting download for subject: {sub_name}...\n")

    # Download Summer files
    for i in range(17, 24):
        url = f"https://gtu.ac.in/uploads/S20{i}/BE/{sub_code}.pdf"
        response = requests.get(url)
        if response:
            file_path = os.path.join(curr_dir, f"{sub_name}_S{i}.pdf")
            with open(file_path, "wb") as file:
                file.write(response.content)
            output_text.insert(tk.END, f"✔ Downloaded: {sub_name}_S{i}.pdf\n")
        else:
            output_text.insert(tk.END, f"✘ {sub_name}_S{i} not available.\n")

    # Download Winter files
    for i in range(17, 24):
        url = f"https://gtu.ac.in/uploads/W20{i}/BE/{sub_code}.pdf"
        response = requests.get(url)
        if response:
            file_path = os.path.join(curr_dir, f"{sub_name}_W{i}.pdf")
            with open(file_path, "wb") as file:
                file.write(response.content)
            output_text.insert(tk.END, f"✔ Downloaded: {sub_name}_W{i}.pdf\n")
        else:
            output_text.insert(tk.END, f"✘ {sub_name}_W{i} not available.\n")

    output_text.insert(tk.END, "Download process completed.\n")

# Setup the GUI window
root = tk.Tk()
root.title("PDF Downloader")
root.geometry("500x500")
root.configure(bg="#f4f4f4")

# Header Label
header_label = tk.Label(root, text="GTU PDF Downloader", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white")
header_label.pack(fill=tk.X, pady=(0, 10))

# Subject Code
tk.Label(root, text="Subject Code:", font=("Helvetica", 10, "bold"), bg="#f4f4f4").pack(pady=5)
entry_sub_code = tk.Entry(root, width=30, font=("Helvetica", 10), relief="groove", bd=2)
entry_sub_code.pack(pady=5)

# Subject Name
tk.Label(root, text="Subject Name:", font=("Helvetica", 10, "bold"), bg="#f4f4f4").pack(pady=5)
entry_sub_name = tk.Entry(root, width=30, font=("Helvetica", 10), relief="groove", bd=2)
entry_sub_name.pack(pady=5)

# Download Button
download_button = tk.Button(
    root, text="Download PDFs", font=("Helvetica", 12, "bold"),
    bg="#4CAF50", fg="white", activebackground="#45a049", relief="raised", command=download_pdfs
)
download_button.pack(pady=15)

# Output text area
output_text = scrolledtext.ScrolledText(root, width=55, height=15, wrap=tk.WORD, font=("Courier", 10), bg="#e0f7fa")
output_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
