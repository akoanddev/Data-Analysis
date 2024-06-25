""" 
This will show GUI with various analysis methods as well as
selection of Excel or CSV file types
"""

"""
This will show GUI with various analysis methods as well as
selection of Excel or CSV file types
"""

"""
This will show GUI with various analysis methods as well as
selection of Excel or CSV file types
"""

import tkinter as tk
from tkinter import ttk

class InitialSelector:

    def __init__(self):
        self.root = None
        self.analysis_method = None
        self.file_type = None
    
    def initial_selector(self):
        self.root = tk.Tk()
        self.root.title("Data Analytical Method Options")

        # Initialize the StringVar instances after the Tk instance is created
        self.analysis_method = tk.StringVar()
        self.file_type = tk.StringVar()

        # Info label (previously the notes text field)
        tk.Label(self.root, text="Data-Analysis from Excel and CSV Datapacks created by Aung:").grid(row=0, column=0, columnspan=2, pady=10)
        
        analysis_methods = ["Correlation Study"]
        self.analysis_method.set(analysis_methods[0])
        tk.Label(self.root, text="Select Analysis Method:").grid(row=1, column=0, columnspan=2, pady=10)
        method_menu = ttk.Combobox(self.root, textvariable=self.analysis_method, values=analysis_methods)
        method_menu.grid(row=2, column=0, columnspan=2, pady=10)

        # File type radio buttons
        self.file_type.set("Excel")
        tk.Label(self.root, text="Select Dataset File Types:").grid(row=3, column=0, pady=10, sticky=tk.W)
        tk.Radiobutton(self.root, text="Excel File", variable=self.file_type, value="Excel").grid(row=3, column=1, pady=10, sticky=tk.W)
        tk.Radiobutton(self.root, text="CSV File", variable=self.file_type, value="CSV").grid(row=4, column=1, pady=10, sticky=tk.W)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.on_submit).grid(row=7, column=0, columnspan=2, pady=20)

        self.root.mainloop()

    def on_submit(self):
        # Handle the submit button press here
        print(f"Analysis Method: {self.analysis_method.get()}")
        print(f"File Type: {self.file_type.get()}")
        # You can add more actions here

if __name__ == "__main__":
    selector = InitialSelector()
    selector.initial_selector()
