from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb
import tkinter.filedialog as fd

# Обработчик события нажатия на кнопку на первом Notebook
def calc(event):
    try:
        param1 = number1.get().replace(',', '.')
        param2 = number2.get().replace(',', '.')
        #проверка на то что строка является числом. так как isdegit() проверяет только целые числа, то при помощи replace удаляем точку перед проверкой 
        if param1.replace('.','',1).isdigit() and param2.replace('.','',1).isdigit():
            str = round(float(eval(param1 + sign.get() + param2)), 5)
            result.delete(0, END)
            result.insert(0, str)
    except:
        result.delete(0, END)
        result.insert(0, "error")
# Обработчик события нажатия на кнопку на втором Notebook
def showMessage(event):
    tempStr = ''
    if ('selected' not in checkbutton1.state()) and ('selected' not in checkbutton2.state()) and ('selected' not in checkbutton3.state()):
        mb.showinfo("Информация", 'Ничего не выбрано')
    else:
        if 'selected' in checkbutton1.state():
            tempStr += 'Вы выбрали первый вариант\n'
        if 'selected' in checkbutton2.state():
            tempStr += 'Вы выбрали второй вариант\n'
        if 'selected' in checkbutton3.state():
            tempStr += 'Вы выбрали третий вариант\n'
        mb.showinfo("Информация", tempStr)
# Обработчик события нажатия на кнопку на третьем Notebook

def readFile(event):
    name = fd.askopenfile(filetypes=[("Текстовый файл", "*.txt")])
    with open(name.name, 'r',  encoding='utf-8') as f:
        # print(f.read())
        temptext = f.read()
    # temptext = temptext.encode('unicode')
    textArea.delete('1.0', END)
    textArea.insert(END, temptext)

Height = 300
Width = 700
ws = Tk()
ws.geometry(str(Width) + 'x'+ str(Height))
ws.title('Олейников Денис Сергеевич')
ws.resizable(False, False)
style = Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook.Tab": {"configure": {"width": int(Width/3) }},
        'TButton': {"configure": {'background': '#bbb'}}})

style.theme_use("MyStyle")
notebook = Notebook(ws)
notebook.pack(fill="both", pady=10, expand=True)


frame1 = Frame(notebook)
frame2 = Frame(notebook)
frame3 = Frame(notebook)



notebook.add(frame1, text='Калькулятор')
notebook.add(frame2, text='Чекбокс')
notebook.add(frame3, text='Работа с текстом')

#notebook 1
number1 = Entry(frame1)
number1.pack(anchor=NW, side=LEFT, padx=6, pady=6)
signs = ["+", "-", "*", "/"]
sign = Combobox(frame1, values=signs, state="readonly")
sign.pack(anchor=NW, side=LEFT, padx=6, pady=6)
number2 = Entry(frame1)
number2.pack(anchor=NW, side=LEFT, padx=6, pady=6)

equality = Label(frame1, text='=')
equality.pack(anchor=NW, side=LEFT, padx=6, pady=6)
result = Entry(frame1)
result.pack(anchor=NW, side=LEFT, padx=6, pady=6)
button1 = Button(frame1, text='Вычислить')
button1.pack(anchor=NW, side=LEFT, padx=6, pady=6)
button1.bind('<Button-1>', calc)


#notebook 2
checkbutton1 = Checkbutton(frame2, text="Первый вариант", onvalue=1, offvalue=0)
checkbutton2 = Checkbutton(frame2, text="Второй вариант", onvalue=1, offvalue=0)
checkbutton3 = Checkbutton(frame2, text="Третий вариант", onvalue=1, offvalue=0)
checkbutton1.pack(anchor=NW, padx=6, pady=6)
checkbutton2.pack(anchor=NW, padx=6, pady=6)
checkbutton3.pack(anchor=NW, padx=6, pady=6)
button2 = Button(frame2, text='Вывести сообщение')
button2.pack(anchor=NW, padx=6, pady=6)

button2.bind('<Button-1>', showMessage)

#notebook 3
 
button3 = Button(frame3, text='Выбрать файл')
button3.pack()
scrollbar=Scrollbar(frame3, orient='vertical')
textArea= Text(frame3, height = 20, width = 85)
scrollbar.config(command=textArea.yview)
scrollbar.pack(side=RIGHT, fill='y')
textArea.pack()
textArea.config(yscrollcommand = scrollbar.set)
button3.bind('<Button-1>', readFile)
ws.mainloop()
