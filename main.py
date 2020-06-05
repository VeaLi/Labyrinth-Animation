# -*- coding: utf-8 -*-
"""
Created on ~

@author: VinLes
"""

# Will create an animation for bread and Astart search.
# Reads the labyrinth from the text file
# Has to modes, RGB is better

import tkinter as tk
import time
import os
from sequencer import seq_it


class App():
    '''
    # Will create an animation for bread and Astart search.
    # Reads the labyrinth from the text file
    # Has to modes, RGB is better

    '''

    def __init__(self):
        self.GO = False
        self.dirl = os.listdir('ANIM')
        self.mode = 'breadth'
        self.l = iter(list(range(len(self.dirl))))
        self.W = 0

        self.root = tk.Tk()
        self.img = ''

        self.op1 = tk.StringVar()
        self.op1.set('search.txt')
        self.op2 = tk.StringVar()
        self.op2.set('')

        self.label2 = tk.Label(text="")
        self.label2.grid(row=4, sticky='w')

        self.btn1 = tk.Button(
            text='Breadth First', default=tk.ACTIVE, command=self.setB).grid(row=4, column=1)
        self.btn2 = tk.Button(text='A *', default=tk.ACTIVE,
                              command=self.setA).grid(row=4, column=3)
        self.e1 = tk.Entry(textvariable=self.op1).grid(row=4, column=4)
        self.btn3 = tk.Button(self.root, text='Run', default=tk.ACTIVE,
                              command=self.setActive).grid(row=4, column=5)

        self.label = tk.Label(text="")
        self.label.grid(row=3, columnspan=5)
        self.alg = 'breadth'
        self.update()

        self.root.mainloop()

    def setA(self):
        self.label.configure(text='current : A*  ')
        self.alg = 'astr'
        self.GO = False

    def setB(self):
        self.label.configure(text='current : Breadth First  ')
        self.alg = 'breadth'
        self.GO = False

    def setActive(self):

        if self.GO == False:
            # calculate
            print('computing ... slowly')
            for f in os.listdir('ANIM'):
                try:
                    os.remove('ANIM/'+f)
                except:
                    pass
            self.label.configure(text='computing ...  ')

            # time.sleep(1)
            name = self.op1.get()
            # SIMPLE

            seq_it(alg=self.alg, name=name, mode='RGB')
            self.dirl = os.listdir('ANIM')
            self.l = iter(list(range(len(self.dirl))))

            self.GO = True
        else:
            self.l = iter(list(range(len(self.dirl))))
            print('framing ... ')

    def update(self):
        now = time.strftime("%H:%M:%S")
        if self.GO:
            self.W = next(self.l, len(self.dirl)-1)
            self.img = tk.PhotoImage(file="ANIM\\{}.png".format(self.W))

            # that for small scale
            ##self.img = self.img.zoom(2,2)
            ##self.img = self.img.zoom(8,8)
            self.label.configure(image=self.img, bg='black')
            self.label2.configure(text='WAVE {} at {}'.format(self.W+1, now))
        self.root.after(50, self.update)


app = App()
