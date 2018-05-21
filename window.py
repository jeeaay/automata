#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: Jeay 
 * @Date: 2018-05-21 08:04:05 
 * @Last Modified by: Jeay
 * @Last Modified time: 2018-05-21 14:49:13
 */
'''

from tkinter import *

root = Tk()
root.title("Automata")

class window:
  def __init__(self):
    # root.geometry('500x300+500+200')
    # frame = Frame(root)
    # frame1.pack(fill=BOTH)
    # Label(frame1, text="网站列表").grid(row=0,column=0,columnspan=2)
    # Label(frame1, text="服务器").grid(row=0, column=2, sticky=W)
    frmT = Frame(width=800, height=60, bg='#ccc')
    frmT.pack(side='top')
    
    # frmT.grid(row=0, column=0, columnspan=2)
    frmL = Frame(width=600, height=500, bg='#ddd')
    frmL.pack(side='left')
    # frmL.grid(row=1, column=0)
    frmR = Frame(width=200, height=500, bg='#eee')
    frmR.pack(side='right')
    # frmR.grid(row=1, column=1)

    frmT.pack_propagate(0)
    frmL.pack_propagate(0)
    frmR.pack_propagate(0)

    Label(frmT, text = 'Hello label').pack()
    Label(frmL, text='Hello label L').pack()
    Label(frmR, text='Hello label R').pack()

    # frmB.grid(row=2, column=0, columnspan=2)
    #Label(frmT, text="网站列表").grid(row=0, column=0)
    #Label(frmT, text="网站列表").grid(row=0,column=1)
    """ frmLT = Frame(root,width=500, height=320, bg='white')
    frmLC = Frame(root,width=500, height=150, bg='red')
    frmLB = Frame(root,width=500, height=30)
    frmRT = Frame(root,width=200, height=500)
    frmLT.grid(row=0, column=0)
    frmLC.grid(row=1, column=0)
    frmLB.grid(row=2, column=0)
    frmRT.grid(row=0, column=1, rowspan=3) """

    root.mainloop()
window()