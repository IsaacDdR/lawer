import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

class ButtonFactory():
    def createButton(self, type_):
        return buttonTypes[type_]()
class ButtonBase():
    relief     ='flat'
    foreground ='white'
    def getButtonConfig(self):
        return self.relief, self.foreground
    
class ButtonRidge(ButtonBase):
    relief     ='ridge'
    foreground ='red'        
    
class ButtonSunken(ButtonBase):
    relief     ='sunken'
    foreground ='blue'        

class ButtonGroove(ButtonBase):
    relief     ='groove'
    foreground ='green'        

buttonTypes = [ButtonRidge, ButtonSunken, ButtonGroove] 

class OOP():
    def __init__(self): 
        self.win = tk.Tk()         
        self.win.title("LEYES VRGS")      
        self.createWidgets()

    def createWidgets(self):    
        tabControl = ttk.Notebook(self.win)     
        tab1 = ttk.Frame(tabControl)            
        tab2 = ttk.Frame(tabControl)

        e1 = ttk.Entry(tabControl)

        tabControl.add(tab1, text='Crear')    
        tabControl.pack(expand=1, fill="both")  

        tabControl.add(tab2, text='Buscar')    
        tabControl.pack(expand=1, fill="both")  

        self.monty = ttk.LabelFrame(tab1, text='Crear')
        self.monty.grid(column=0, row=0, padx=8, pady=4)        

        tabControl.add(e1)

        self.monty = ttk.LabelFrame(tab2, text= 'Buscar')
        self.monty.grid(column=0, row=0, padx=8, pady=4)        

        scr = scrolledtext.ScrolledText(self.monty, width=30, height=3, wrap=tk.WORD)
        scr.grid(column=0, row=3, sticky='WE', columnspan=3)

        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)
        fileMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="File", menu=fileMenu)
        helpMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=helpMenu)
        
        self.createButtons()

    def createButtons(self):
            
        

        """
        factory = ButtonFactory()

        # Button 1
        rel = factory.createButton(0).getButtonConfig()[0]
        fg  = factory.createButton(0).getButtonConfig()[1]
        action = tk.Button(self.monty, text="Button "+str(0+1), relief=rel, foreground=fg)   
        action.grid(column=0, row=1)  

        # Button 2
        rel = factory.createButton(1).getButtonConfig()[0]
        fg  = factory.createButton(1).getButtonConfig()[1]
        action = tk.Button(self.monty, text="Button "+str(1+1), relief=rel, foreground=fg)   
        action.grid(column=1, row=1)  
        
        # Button 3
        rel = factory.createButton(2).getButtonConfig()[0]
        fg  = factory.createButton(2).getButtonConfig()[1]
        action = tk.Button(self.monty, text="Button "+str(2+1), relief=rel, foreground=fg)   
        action.grid(column=2, row=1)          
        """

#         # using a loop to do the above
#         for idx in range(len(buttonTypes)):
#             rel = factory.createButton(idx).getButtonConfig()[0]
#             fg  = factory.createButton(idx).getButtonConfig()[1]
#             
#             action = tk.Button(self.monty, text="Button "+str(idx+1), relief=rel, foreground=fg)   
#             action.grid(column=idx, row=1)            
  
#==========================
oop = OOP()
oop.win.mainloop()
"""
def __init__(self, window):
        self.container = window
        self.buttons = tk.Frame(window)
        self.QUIT = tk.Button(self.buttons, text='QUIT', fg='red',
                              command=self.writequit)
        self.long_rest = tk.Button(self.buttons, text='Long rest',
                                   command=lambda: self.rest('long'))
        self.short_rest = tk.Button(self.buttons, text='Short rest',
                                    command=lambda: self.rest('short'))
        self.next_turn = tk.Button(self.buttons, text='Next turn',
                                   command=lambda: self.rest('turn'))
        self.core = ttk.Notebook(window)
        self.core.bind("<<NotebookTabChanged>>", self.tab_update)
        ######
        self.frontpage = tk.Frame(self.core)
        self.featurespage = tk.Frame(self.core)
        self.attackpage = tk.Frame(self.core)
        self.inventorypage = tk.Frame(self.core)
        self.spellspage = tk.Frame(self.core)
        # self.draw_static()
        self.startup_begin() 

master = Tk()

style = ttk.Style(master)
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

create = ttk.Notebook()
f1 = ttk.Frame(create)
f2 = ttk.Frame(create)

Label(master, text="FECHA:").grid(row=0)
Label(master, text="IMPUTADO:").grid(row=1)
Label(master, text="VICTIMA:").grid(row=2)
Label(master, text="LUGAR:").grid(row=3)
Label(master, text="DELITO:").grid(row=4)
Label(master, text="CIUDAD:").grid(row=5)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

create.add(f1, text="CREAR")
create.add(f2, text="BUSCAR")

mainloop( )
"""
