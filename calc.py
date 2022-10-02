# Описание внешнего вида калькулятора
import tkinter as tk


win = tk.Tk()

win.title ('Калькулятор')

#Размеры окна 500х600, 
#100 и 200 - расположение относительно верхнего левого угла

win.geometry('500x600+100+200') 

#Запрет изменения размеров окна

win.resizable(False, False) 

win.mainloop()

