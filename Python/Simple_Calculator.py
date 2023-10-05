from tkinter import *
import operator
import re
class application:
    def __init__(self,window):
        # - Output field - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        self.output=Entry(window)
        self.output.grid(row=0,column=1,columnspan=3)

        # - Numbers - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        self.Btn1=Button(window,text="1",height=5,width=10,command= lambda: self.displayer("1"))
        self.Btn1.grid(row=1,column=0,padx=2,pady=4)

        self.Btn2=Button(window,text="2",height=5,width=10,command= lambda: self.displayer("2"))
        self.Btn2.grid(row=1,column=1,padx=2,pady=4)

        self.Btn3=Button(window,text="3",height=5,width=10,command= lambda: self.displayer("3"))
        self.Btn3.grid(row=1,column=2,padx=2,pady=4)

        self.Btn4=Button(window,text="4",height=5,width=10,command= lambda: self.displayer("4"))
        self.Btn4.grid(row=2,column=0,padx=2,pady=4)

        self.Btn5=Button(window,text="5",height=5,width=10,command= lambda: self.displayer("5"))
        self.Btn5.grid(row=2,column=1,padx=2,pady=4)

        self.Btn6=Button(window,text="6",height=5,width=10,command= lambda: self.displayer("6"))
        self.Btn6.grid(row=2,column=2,padx=2,pady=4)

        self.Btn7=Button(window,text="7",height=5,width=10,command= lambda: self.displayer("7"))
        self.Btn7.grid(row=3,column=0,padx=2,pady=4)

        self.Btn8=Button(window,text="8",height=5,width=10,command= lambda: self.displayer("8"))
        self.Btn8.grid(row=3,column=1,padx=2,pady=4)

        self.Btn9=Button(window,text="9",height=5,width=10,command= lambda: self.displayer("9"))
        self.Btn9.grid(row=3,column=2,padx=2,pady=4)

        self.Btn0=Button(window,text="0",height=5,width=10,command = lambda: self.displayer("0"))
        self.Btn0.grid(row=4,column=0,padx=2,pady=4)

        #- Symbols - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        self.Sym1=Button(window,text="=",height=5,width=23, command = lambda: self.operations("=")) #Insert a command parameters for symbols here
        self.Sym1.grid(row=4,column=3,columnspan=2,padx=4,pady=4)

        self.Sym2=Button(window,text="+",height=5,width=10, command = lambda: self.displayer("+"))
        self.Sym2.grid(row=4,column=1,padx=2,pady=4)

        self.Sym3=Button(window,text="Del",height=5,width=10, command = lambda: self.operations("Del"))
        self.Sym3.grid(row=1,column=3,padx=2,pady=4)

        self.Sym4=Button(window,text="Clear",height=5,width=10, command = lambda: self.operations("Clear"))
        self.Sym4.grid(row=1,column=4,padx=2,pady=4)

        self.Sym5=Button(window,text="x",height=5,width=10, command = lambda: self.displayer("x"))
        self.Sym5.grid(row=2,column=3,padx=2,pady=4)

        self.Sym6=Button(window,text="/",height=5,width=10, command = lambda: self.displayer("/"))
        self.Sym6.grid(row=2,column=4,padx=2,pady=4)

        self.Sym8=Button(window,text="-",height=5,width=10, command = lambda: self.displayer("-"))
        self.Sym8.grid(row=4,column=2,padx=2,pady=4)

        # - Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def displayer(self,number):
        if number!="Clear" and number!="=" and number !="Del":
            field=self.output.get()
            self.numbers=""
            self.numbers+=number
            self.output.insert(len(field),self.numbers)

    def operations(self,operation):
        if operation=="Clear":
            self.output.delete(0,END)
        if operation=="Del":
            field=self.output.get()
            self.output.delete(len(field)-1,END)
        if operation=="=":
            field=self.output.get()
            storage=re.split(pattern = r"([+-x/])",string = str(field))
            for space in storage:
                if space=="":
                    storage.remove(storage[storage.index(space)])
            i=-1
            while True:
                i+=1
                current=storage[i]
                try:
                    next=storage[storage.index(current)+1]
                    if (next!='x' and next!='/' and next!='+' and next!='-') and (current!='x' and current!='/' and current!='+' and current!='-'):
                        result=current+next
                        storage[i]=result
                        storage.remove(next)
                        i-=1
                    elif current==storage[-1]:
                        break
                    else:
                        pass
                except:
                    break
            application.calculator(self,storage)
    def calculator(self,storage):
        print(storage)
        for entry in storage: # Operation solvers solving expressions by their respective symbols
            if entry=="x":
                num1=int(storage[storage.index(entry)-1])
                num2=int(storage[storage.index(entry)+1])
                result=operator.mul(num1,num2)
                num1=str(storage[storage.index(entry)-1])
                num2=str(storage[storage.index(entry)+1])
                placeHolder=storage.index(num1)
                storage.remove(num1)
                storage.remove(num2)
                storage.remove(entry)
                storage.insert(placeHolder,str(result))
            if entry=="/":
                num1=int(storage[storage.index(entry)-1])
                num2=int(storage[storage.index(entry)+1])
                result=operator.truediv(num1,num2)
                num1=str(storage[storage.index(entry)-1])
                num2=str(storage[storage.index(entry)+1])
                placeHolder=storage.index(num1)
                storage.remove(num1)
                storage.remove(num2)
                storage.remove(entry)
                storage.insert(placeHolder,str(result))
        for entry in storage:
            if entry=="+":
                num1=int(storage[storage.index(entry)-1])
                num2=int(storage[storage.index(entry)+1])
                result=operator.add(num1,num2)
                num1=str(storage[storage.index(entry)-1])
                num2=str(storage[storage.index(entry)+1])
                placeHolder=storage.index(num1)
                storage.remove(num1)
                storage.remove(num2)
                storage.remove(entry)
                storage.insert(placeHolder,str(result))
            if entry=="-":
                num1=int(storage[storage.index(entry)-1])
                num2=int(storage[storage.index(entry)+1])
                result=operator.sub(num1,num2)
                num1=str(storage[storage.index(entry)-1])
                num2=str(storage[storage.index(entry)+1])
                placeHolder=storage.index(num1)
                storage.remove(num1)
                storage.remove(num2)
                storage.remove(entry)
                storage.insert(placeHolder,str(result))
        application.checker(self,storage)
    def checker(self,storage):
        if ("x" in storage) or ("/" in storage) or ("+" in storage) or ("-" in storage):
            application.calculator(self,storage)
        else:
            total=storage[0]
            self.output.delete(0,END)
            self.output.insert(0,total)
        
window = Tk()
window.geometry("450x450+50+50")
window.title("Calculator")
application(window)
window.mainloop()