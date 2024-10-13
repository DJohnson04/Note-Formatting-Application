#takes in a file, sorts it using popular organization skills and the order  
from dotenv import load_dotenv
import google.generativeai as genai
import os
import tkinter as tk

#api handling
class FileHandling:
    def getFileContents(self, filename):
        with open(filename,'r') as f:
            old_content = f.readlines()
            content = ''
            for line in old_content:
                content += line
        return content
    def updateFileContents(self, filename, data):
        with open(filename,'w') as f:
           for n in data:
               f.write(n + '\n')

class ApiHandling:
    def __init__(self):
        load_dotenv()
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        genai.configure(api_key=os.getenv('APIKEY'))
        
    
    def returnFormattedData(self, file_content):
        response = self.model.generate_content("Organize the Text, Do Not remove any DATA only add on and make it more readible!: Data: " + file_content)
        formated_version = response.text.splitlines()
        return formated_version
            
        

#Implementing GUI inteface
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.entry = tk.Entry(self.root, text='File Path: ')
        self.file_path = tk.StringVar()

        self.file_path = tk.Label(self.root, text = 'File Path: ', font=('calibre',10, 'bold'))
        
        self.file_path_entry = tk.Entry(self.root,textvariable = self.file_path, font=('calibre',10,'normal'))
        
        self.sub_btn=tk.Button(self.root,text = 'Submit', command=self.submit)
        self.file_path.grid(row=0,column=0)
        self.file_path_entry.grid(row=0,column=1)
        self.sub_btn.grid(row=2,column=1)
    def submit(self):
        filepath=self.file_path_entry.get()
        print('filepath: ' + filepath)
        api = ApiHandling()
        file_handling = FileHandling()
        file_handling.updateFileContents(filepath, api.returnFormattedData(file_handling.getFileContents(filepath)))






#/Users/davidjohnson/Documents/Notes/Obsidian Vaults/Academic Notes/Academic Vault/Coding/Networking Notes/Test.md
gui = GUI()
gui.root.mainloop()
