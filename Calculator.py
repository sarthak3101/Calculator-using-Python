import math
from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('575x470')
root.resizable(0,0)
root.configure(background = '#222222')
opers = ['+',"-","*","/"] # USED LATER

#--Functions--
def enterNum(x):
	if entry.get() == '0':
		entry.delete(0,END)
		entry.insert(0,str(x))
	else:
		length = len(entry.get())
		entry.insert(length,str(x))

def enterOper(x):
	global opers
	length = len(entry.get())
	if entry.get()[length-1] not in opers:
		entry.insert(length,btn_oper[int(x)]['text'])
	else:
		entry.delete(length-1,END)
		entry.insert(length,btn_oper[int(x)]['text'])

def funEqual():
	a = entry.get()
	entry.delete(0,END)
	entry.insert(0,eval(a))

def funCls():
	entry.delete(0,END)
	entry.insert(0,'0')

def funClr():
	length = len(entry.get())
	entry.delete(length-1,END)
	if length == 1:
		entry.insert(0,'0')

def funFact():
	a = int(entry.get())
	fact = 1
	for i in range(1,a+1):
		fact *= i
	entry.delete(0,END)
	entry.insert(0,str(fact))

def NaturalLog():
	a = float(entry.get())
	ln = str(math.log(a))
	entry.delete(0,END)
	entry.insert(0,ln)

def Log():
	a = float(entry.get())
	log = str(math.log10(a))
	entry.delete(0,END)
	entry.insert(0,log)

def AntiLn():
	a = float(entry.get())
	aln = str(math.e**a)
	entry.delete(0,END)
	entry.insert(0,aln)

##-Entry Box--
entry = Entry(width = 55,bg = 'green',font = 'times 14 bold',justify = RIGHT)
entry.place(x = 10, y = 20)
entry.insert(0,'0')

#--Buttons--
btn_num = []
for i in range(10):
	btn_num.append(Button(width = 10,bg = 'red',text = str(i), height = 2, command = lambda x = i: enterNum(x)))
tnum = 1
for i in range(3):
	for j in range(3):
		btn_num[tnum].place(x = 10 + j*120, y = 60 + i*70)
		tnum += 1

btn_oper = []
for i in range(4):
	btn_oper.append(Button(width = 10,bg = 'aqua', height = 2, command = lambda x = i: enterOper(x)))

opers = ['+',"-","*","/"]
for i in range(4):
	btn_oper[i]['text'] = opers[i]
	btn_oper[i].place(x = 370, y = 60 + i*70)

btn_zero = Button(width = 45,bg = 'red',text = '0',height = 2,command = lambda x = 0:enterNum(x))
btn_zero.place(x = 10,y = 270)

btn_eql = Button(width = 78,bg = 'purple',height = 2, text = '=',command = funEqual)
btn_eql.place(x = 10,y = 340)

btn_clr = Button(width = 37,bg = 'purple',height = 2, text = 'C',command = funClr)
btn_clr.place(x = 10,y = 410)

btn_cls = Button(width = 37,bg = 'purple',height = 2, text = 'CE',command = funCls)
btn_cls.place(x = 296,y = 410)

btn_fact = Button(width = 10,bg = 'aqua', height = 2,text = "FACT", command = funFact)
btn_fact.place(x = 483, y = 60)

btn_ln = Button(width = 10,bg = 'aqua', height = 2,text = "ln", command = NaturalLog)
btn_ln.place(x = 483, y = 130)

btn_log = Button(width = 10,bg = 'aqua', height = 2,text = "log", command = Log)
btn_log.place(x = 483, y = 200)

btn_aln = Button(width = 10,bg = 'aqua', height = 2,text = "anti ln", command = AntiLn)
btn_aln.place(x = 483, y = 270)

#--The Mainloop--
root.mainloop()
