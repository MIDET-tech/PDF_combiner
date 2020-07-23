#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import PySimpleGUI as sg
import PyPDF2
import warnings

def submit_func():
    merger = PyPDF2.PdfFileMerger()
    for i in range(number):
        merger.append(values[i])
    merger.write("combined_file.pdf")
    merger.close()
    
    sg.popup("The combined PDF file has been output successfully as [combined_file.pdf]")

warnings.simplefilter("ignore")

#Number of files
number = 2

sg.theme("SandyBeach")

layout = [[sg.Text("Browse 2 or more pdf files you want to combine")],
          [sg.Text("File 1", size=(8, 1)),sg.Input(), sg.FileBrowse()],
          [sg.Text("File 2", size=(8, 1)),sg.Input(), sg.FileBrowse()],
          [sg.Button("AddFile", key="AddFile"),sg.Submit(), sg.Cancel()]]

window = sg.Window("PDF combiner", layout)

while True:
    event, values = window.read()

    if event in [None,"Cancel"]:
        break
    elif event == "AddFile":
        number += 1
        new_layout = [[sg.Text("Browse 2 or more pdf files you want to combine")],
              [sg.Text("File 1", size=(8, 1)),sg.Input(), sg.FileBrowse()],
              [sg.Text("File 2", size=(8, 1)),sg.Input(), sg.FileBrowse()],
              [sg.Button("AddFile", key="AddFile"),sg.Submit(), sg.Cancel()]]
        for i in range(number-2):
            additional_file = [sg.Text("File {}".format(i+3), size=(8, 1)),sg.Input(), sg.FileBrowse()]
            new_layout.insert(i+3 , additional_file)
        window.close()
        window = sg.Window("PDF combiner", new_layout)
    elif event == "Submit":
        if values[0] and values[1] != None:
            submit_func()
            break
        else:
            sg.popup("Please browse more than 2 files")

window.close()

