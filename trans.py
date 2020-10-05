from tkinter import ttk
import tkinter as tk
from googletrans import Translator, LANGUAGES

win=tk.Tk()
win.title("Translator")
win.geometry("300x200")

##########    Get the text and the epecific language    ##########
def get():
	word=entry.get()
	destText =  destcombo.get()
	try:
		if word != '':
			text = trans(word,destText)
			label1=tk.Label(win,text=f"Translated in \""+destText+"\"....... : "+text+"",bg="yellow")
			label1.grid(row=5,column=0)
	except:
		pass

##########    Translate Text to a specific language  ##########
def trans(word,destText):
	translator=Translator(service_urls=['translate.google.com'])
	translation1=translator.translate(word,dest=destText)
	return translation1.text

##########    Languages    ##########
langs = ['English','French', 'Italian', 'Spanish', 'Hindi']

##########    Dropdown Menu    ##########
destlabel=tk.Label(win,text="To:")
destlabel.grid(row=0,column=0,sticky="W")
destcombo = ttk.Combobox(win,values=langs)
destcombo.grid(row=1,column=0)

##########    Text Box    ##########
label=tk.Label(win,text="Enter Word : ")
label.grid(row=3,column=0,sticky="W")

entry = tk.Entry(win)
entry.grid(row=4,column=0)

##########    Button translate   ##########
button = tk.Button(win,text="Translate", command=get)
button.grid(row=4,column=1)

win.mainloop()