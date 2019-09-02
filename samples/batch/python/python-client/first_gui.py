#GUI for CLOx
import json
import sys
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def create_csv():
    os.system('python3 clox_json.py')

def transcribe():
    os.system('python3 main.py')

#key down function
def click():
    languagedict = {
    "Arabic - EG": "ar-EG",
    "Catalan - ES": "ca-ES",
    "Chinese - CN": "zh-CN",
    "Chinese - HK": "zh-HK",
    "Chinese - TW": "zh-TW",
    "Danish - DK": "da-DK",
    "Dutch - NL": "nl-NL",
    "English - AU": "en-AU",
    "English - CA": "en-CA",
    "English - GB": "en-GB",
    "English - IN": "en-IN",
    "English - NZ": "en-NZ",
    "English - US": "en-US",
    "Spanish - ES": "es-ES",
    "Spanish - MX": "es-MX",
    "Finnish - FI": "fi-FI",
    "French - CA": "fr-CA",
    "French - FR": "fr-FR",
    "German - DE": "de-DE",
    "Hindi - IN": "hi-IN",
    "Italian - IT": "it-IT",
    "Japanese - JP": "jp-JP",
    "Korean - KR": "kr-KR",
    "Norwegian - NO": "no-NO",
    "Polish - PL": "pl-PL",
    "Portuguese - BR": "pt-BR",
    "Portuguese - PT": "pt-PT",
    "Russian - RU": "ru-RU",
    "Swedish - SE": "se-SE"
    }
    key = keyentry.get()
    uri = urientry.get()
    region = regioncombo.get()
    lang = languagecombo.get()
    start_time = startentry.get()
    output.insert(tk.END, key + " ")
    output.insert(tk.END, uri + " ")
    output.insert(tk.END, region + " ")
    output.insert(tk.END, lang + " ")
    output.insert(tk.END, start_time)
    lang_val = languagedict[lang]
    config_dict = {}
    config_dict['key'] = key
    config_dict['uri'] = uri
    config_dict['region'] = region
    config_dict['language'] = lang_val
    config_dict['start_time'] = start_time
    config_file = open('clox_config_test.txt', 'w')
    config_file.write(json.dumps(config_dict))
    config_file.close()

### main
window = tk.Tk()
window.title("CLOx Transcription Service")

### Photo
image1 = Image.open("clox_logo.jpg")
photo1 = ImageTk.PhotoImage(image1)
tk.Label(window, image=photo1, bg="black") .grid(row=0, column=0, sticky=tk.W)

tk.Label(window, text="API key:") .grid (row=1, column=0, sticky=tk.W)
keyentry = tk.Entry(window, width=29, bg="white")
keyentry.grid(row=2, column=0, sticky=tk.W)

### create label & text entry box 
tk.Label(window, text="Azure Blob URI:") .grid(row=3, column=0, sticky=tk.W)
urientry = tk.Entry(window, width=71, bg="white")
urientry.grid(row=4, column=0, sticky=tk.W)

tk.Label(window, text="Azure Account Region:") .grid(row=5, column=0, sticky=tk.W)
regioncombo = ttk.Combobox(window, values=[
    "West US",
    "West US 2",
    "East US",
    "East US 2",
    "Central US",
    "North Central US",
    "South Central US",
    "Central India",
    "East Asia",
    "Southeast Asia",
    "Japan East",
    "Korea Central",
    "Australia East",
    "Canada Central",
    "North Europe",
    "West Europe",
    "UK South",
    "France Central"
])
regioncombo.grid(column=0, row=6, sticky=tk.W)

tk.Label(window, text="Language:") .grid(row=7, column=0, sticky=tk.W)
langvalues=[
    "Arabic - EG",
    "Catalan - ES",
    "Chinese - CN",
    "Chinese - HK",
    "Chinese - TW",
    "Danish - DK",
    "Dutch - NL",
    "English - AU",
    "English - CA",
    "English - GB",
    "English - IN",
    "English - NZ",
    "English - US",
    "Spanish - ES",
    "Spanish - MX",
    "Finnish - FI",
    "French - CA",
    "French - FR",
    "German - DE",
    "Hindi - IN",
    "Italian - IT",
    "Japanese - JP",
    "Korean - KR",
    "Norwegian - NO",
    "Polish - PL",
    "Portuguese - BR",
    "Portuguese - PT",
    "Russian - RU",
    "Swedish - SE"
]
languagecombo = ttk.Combobox(window, values = langvalues)
languagecombo.grid(row=8, column=0, sticky=tk.W)

###get start time of file
tk.Label(window, text="Start time of recording in milliseconds") .grid(row=9, column=0, sticky=tk.W)
startentry = tk.Entry(window, width=12, bg="white")
startentry.grid(row=10, column=0, sticky=tk.W)

### add a submit button
tk.Label(window, text="Click below to save your settings") .grid(row=11, column=0, sticky=tk.W)
ttk.Button(window, text="Save", width=4, command=click) .grid(row=12, column=0, sticky=tk.W)

### show output
tk.Label(window, text="Output:") .grid(row=13, column=0, sticky=tk.W)
output = tk.Text(window, width=75, height=1, wrap=tk.WORD, background="white")
output.grid(row=14, column=0, sticky=tk.W)

tk.Label(window, text="Click below to begin transcription") .grid(row=15, column=0, sticky=tk.W)
ttk.Button(window, text="Transcribe", width=10, command=transcribe) .grid(row=16, column=0, sticky=tk.W)

tk.Label(window, text="Click below to create your CSV from the json file") .grid(row=17, column=0, sticky=tk.W)
ttk.Button(window, text="Create CSV", width=10, command=create_csv) .grid(row=18, column=0, sticky=tk.W)

### run the main loop
window.mainloop()
