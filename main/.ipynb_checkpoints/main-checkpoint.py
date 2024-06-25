#This is the central control integrated to execute separate modules

#from excel_loader import ExcelLoader
from initial_selection import InitialSelector

def main():
    initial_selection = InitialSelector()
    initial_selection.initial_selector()

if __name__ == "__main__":
    main()