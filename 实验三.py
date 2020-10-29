from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

window = Tk()
window.title("离散信号")
window.geometry("350x200")
lbl = Label(window, text="选择信号")
lbl.grid(column=0, row=0)

x = np.arange(-1, 10, 1)

def clicked1():
    y = [0,1,0,0,0,0,0,0,0,0,0]
    plt.stem(x,y)
    plt.show()
btn1 = Button(window, text="单位脉冲序列", command=clicked1)
btn1.grid(column=0, row=1)

def clicked2():
    y = [0,1,1,1,1,1,1,1,1,1,1]
    plt.stem(x,y)
    plt.show()
btn2 = Button(window,text="单位阶跃序列", command=clicked2)
btn2.grid(column=0,row=2)

def clicked3():
    x=np.linspace(0,10,10)
    y=3*0.6**x
    plt.stem(x,y)
    plt.show()
btn3 = Button(window,text="离散时间负指数", command=clicked3)
btn3.grid(column=0,row=3)

def clicked4():
    x=np.linspace(0,5,20)
    y = np.sin(0.5*np.pi*x)
    plt.stem(x,y)
    plt.show()
btn4 = Button(window,text="离散正弦", command=clicked4)
btn4.grid(column=0,row=4)
window.mainloop()