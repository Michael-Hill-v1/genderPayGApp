import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import os


class classGui():
    # Put all the code inside the init routine, allowing the GUI to return an output
    # to the main routine
    def __init__(self, df):
        self.df = df
        self.output = ''

        def fSelectFolder():
            strFolder = filedialog.askdirectory()
            entryFilepath.delete(0, tk.END)
            entryFilepath.insert(0, strFolder)
        
        def fFilterLbNames(event):
            # Read the text in the 'entry' box
            strSubstring = entryNameFilter.get()
            # Choose the right year, and get the Names that include the text
            intYear = listboxYears.get(listboxYears.curselection())
            seriesNames = df.loc[
                (df['Year'] == intYear) & (df['Names'].str.contains(strSubstring.upper())),
                'Names']
            seriesNames = seriesNames.sort_values()
            # Update the listbox
            fUpdateListBox(listboxBox=listboxNames, seriesStrings=seriesNames)
                    
        def fUpdateListBox(listboxBox, seriesStrings):
            # Clear existing list
            listboxBox.delete(0, 'end')
            # Add new list
            for strString in seriesStrings:
                listboxBox.insert('end', strString)
            listboxBox.select_set(0)

        def fSelectName():
            if listboxNames.size() > 0:
                intYear = listboxYears.get(listboxYears.curselection())
                # Get the employer Id that matches the name
                strName = listboxNames.get(listboxNames.curselection())
                strEmployerId = df.at[df.loc[df['Names'] == strName].index[0], 'EmployerId']
                strFilepath = r'' + entryFilepath.get()
                if not os.path.exists(strFilepath):
                    try:
                        os.makedirs(strFilepath)
                    except:
                        messagebox.showerror('error', 'Couldn\'t create folder\n' + strFilepath)
                        return                
                self.output = intYear, strEmployerId, strFilepath
                tkGui.destroy()

        # Create the window and add widgets
        tkGui = tk.Tk()
        tkGui.title('Pay G App')
        tkGui.geometry('450x300')
        
        # Add a listbox displaying the years.  This will control the list of names.
        tk.Label(tkGui, text='Select Snapshot Year').grid(row=3, column=0, sticky='w', padx=20, pady=0)
        listboxYears = tk.Listbox(tkGui, exportselection=False)
        listboxYears.grid(row=5, column=0, sticky='ew', padx=20, pady=0)
        listboxYears.bind('<<ListboxSelect>>', fFilterLbNames)
        
        # Add a textbox for filtering the names
        tk.Label(tkGui, text='Search Names: ').grid(row=0, column=1, sticky='w', padx=0, pady=10)
        entryNameFilter = tk.Entry(tkGui)
        entryNameFilter.grid(row=0, column=2, sticky='ew', padx=0, pady=10)
        entryNameFilter.bind('<KeyRelease>', fFilterLbNames)
        entryNameFilter.focus()
        # Add a listbox displaying the names for the selected year.
        # This will control the SicCode list.
        tk.Label(tkGui, text='Select Name').grid(row=3, column=1, sticky='w', padx=0, pady=0)
        listboxNames = tk.Listbox(tkGui, exportselection=False)
        listboxNames.grid(row=5, column=1, columnspan=2, sticky='ew', padx=0, pady=0)

        # Add a button to allow browsing to select output filepath
        buttonBrowse = tk.Button(tkGui, text='Select output folder', command=fSelectFolder)
        buttonBrowse.grid(row=6, column=0, sticky='ew', padx=20, pady=10)
        # Add an entry box for filepath too
        entryFilepath = tk.Entry(tkGui)
        entryFilepath.grid(row=7, column=0, sticky='ew', padx=20, columnspan=4)
        entryFilepath.insert(0, 'C:\Temp')
        
        # Add a button to export the name
        buttonSelect = tk.Button(tkGui, text='Run report for selection', command=fSelectName)
        buttonSelect.grid(row=6, column=2, sticky='ew', padx=20, pady=10)

        # Populate the listboxes:
        # Get a series of years in descending order and populate the listbox
        seriesYears = df['Year']
        seriesYears = seriesYears.drop_duplicates().sort_values(ascending=False)
        fUpdateListBox(listboxBox=listboxYears, seriesStrings=seriesYears)
        # Update the names.
        fFilterLbNames('<<ListboxSelect>>')
            
        tk.mainloop()

def fGetSettings(df):
    return classGui(df).output
