import time
from tkinter import *


def disappear(event):
    root.attributes('-alpha', 0.01)


def show(event):
    root.attributes('-alpha', 1)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    window_wide_center = (screenwidth - width) / 2
    size = '%dx%d+%d+%d' % (width, height, window_wide_center, 0)
    root.geometry(size)


def set_window(root):
    root.attributes('-toolwindow', True, '-alpha', 0.9, '-fullscreen', False, '-topmost', True)
    root.overrideredirect(True)
    root.grid()
    center_window(root, 360, 30)
    root.bind(sequence='<Leave>', func=disappear)
    root.bind(sequence='<Enter>', func=show)


root = Tk()
set_window(root)
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()


class CreateContain:

    def __init__(self, root):
        self.fm1_1 = Frame(root)
        Label(text='virtual machine').grid(row=1, column=0, padx=20, pady=2)
        Label(text='dsp').grid(row=2, column=0, padx=20, pady=2)
        Label(text='console').grid(row=3, column=0, padx=20, pady=2)

        self.fm1_2 = Frame(root)
        Label(textvariable=var1, fg='blue', font=("黑体", 12)).grid(row=1, column=1, padx=60, pady=2)
        Label(textvariable=var2, fg='blue', font=("黑体", 12)).grid(row=2, column=1, padx=60, pady=2)
        Label(textvariable=var3, fg='blue', font=("黑体", 12)).grid(row=3, column=1, padx=60, pady=2)

    def gettime(self):
        var1.set(time.strftime("%H:%M:%S") + '    oo1')
        var2.set(time.strftime("%H:%M:%S") + '    oo2')
        var3.set(time.strftime("%H:%M:%S") + '    oo3')
        self.fm1_2.after(1000, self.gettime)


if __name__ == '__main__':
    create = CreateContain(root)
    create.gettime()
    mainloop()
