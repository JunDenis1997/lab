import requests
import pprint
import json
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb

def saveInfoRep(event):
    nameRep = nameEntry.get()
    res = requests.get("https://api.github.com/users/" + nameRep).json()
    if 'message' in res and res['message'] == 'Not Found':
        mb.showinfo("Информация", "Репозиторий не найден")    
    else:
        company =  res["company"]
        created_at =  res["created_at"]
        email =  res["email"]
        id =  res["id"]
        name =  res["name"]
        url =  res["url"]
        rep = {
            "company": res["company"],
            "created_at": res["created_at"],
            "email": res["email"],
            "id": res["id"],
            "name": res["name"],
            "url": res["url"]
        }
        jsonrepo = json.dumps(rep)
        with open(nameRep + '.json', 'w') as f:
            json.dump(jsonrepo, f)
        mb.showinfo("Информация", "Информация сохранена")

Height = 300
Width = 500
ws = Tk()
ws.geometry(str(Width) + 'x'+ str(Height))
ws.title('Олейников Денис Сергеевич')

ws.resizable(False, False)

nameEntry = Entry(ws)
nameEntry.pack(anchor=NW, side=LEFT, padx=6, pady=6)
reqbutton = Button(ws, text='Сохранить')
reqbutton.pack(anchor=NW, side=LEFT, padx=6, pady=6)
reqbutton.bind('<Button-1>', saveInfoRep)
ws.mainloop()
