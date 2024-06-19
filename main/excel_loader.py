# this is to load excel file using window explorer
# Loaded file will be returned to the caller module

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class ExcelLoader:
    def __init__(self):
        """
        Initializes the ExcelLoader class with default attributes.
        """
        self.file_path = None
        self.dataframe = None
    
    def get_excel_file_path(self):
        #hide the root window
        Tk().withdraw()
        self.file_path = askopenfilename (title = "Select an Excel Data File", filetypes = [("Excel files", "*.xlsx *.xls"), ("All files", "*.*")])
        if not self.file_path:
            print("No file selected.")
        return self.file_path

    def load_file(self):
        """
        Loads the selected Excel file into a DataFrame.
        """
        if self.file_path:
            self.dataframe = pd.read_excel(self.file_path)
            print(f"Loaded file: {self.file_path}")
        else:
            print("No file selected to load.")

    def display_data(self):
        """
        Displays the first few rows of the loaded DataFrame.
        """
        if self.dataframe is not None:
            print("Data Preview:")
            print (self.dataframe.head())
            print (self.dataframe.to_string())
        else:
            print("No data to display.")

# Create an instance of ExcelLoader
excel_loader = ExcelLoader()

# Use the get_excel_file_path method
file_path = excel_loader.get_excel_file_path()

# Load and display the data
excel_loader.load_file()
excel_loader.display_data()

