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
        self.dataheader = None
    
    def get_excel_file_path(self):
        #hide the root window
#        Tk().withdraw()
        self.file_path = askopenfilename (title = "Select an Excel Data File", filetypes = [("Excel files", "*.xlsx *.xls"), ("All files", "*.*")])
        if not self.file_path:
            print("No file selected.")
        return self.file_path

    def load_file(self):
        """
        Loads the selected Excel file into a DataFrame.
        """
        self.dataframe = pd.read_excel(self.file_path, header = None)
        i = 0
        for index, row in self.dataframe.iterrows():
            if row.isnull().all() or (row == '').all():
                i += 1
            else:
                break  # Stop at the first non-blank row
                
        self.dataheader = pd.read_excel(self.file_path, header=i)
#            self.correlation_data = self.dataframe.corr()
#            print (self.correlation_data.to_string())

        
    def display_data(self):
        """
        Displays the first few rows of the loaded DataFrame.
        """
        if self.dataframe is not None:
            print (self.dataheader.to_string())
            print (self.dataframe.to_string())
        else:
            print("No data to display.")

excel_loader = ExcelLoader()
file_path = excel_loader.get_excel_file_path()
#excel_loader.load_file()
#excel_loader.display_data()

