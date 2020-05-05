#!/bin/python
# -*- coding: utf-8 -*-
#Name : DirCleaner V2
#Author : strak_stark
#Date : 2020

#=======================================================================
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import *
import tkinter.messagebox
from tkinter.messagebox import askokcancel
import os
from os import path
import shutil


global btn1,btn2,btn3,cleanfoldB
root = Tk()
root.resizable(0, 0)
def createfolder():
	global e,e2,new_window
	new_window = Toplevel(root)
	new_window.attributes("-topmost", 1)
	new_window.resizable(0, 0)
	new_window.geometry('250x75')
	new_window.title("Create storage folder")
	label1 = Label(new_window, text="Name for your storage folder")
	label1.pack()

	e = Entry(new_window)
	e.pack()
	btn1 = Button(new_window,text='Create',command=createfolder2)
	btn1.pack()
	new_window.protocol("WM_DELETE_WINDOW",new_window.destroy)

def createfolder2():
	foldname= e.get()
	rep = filedialog.askdirectory(initialdir="/",title="Where do you want to create '{}'".format(foldname))
	foldname="{0}/{1}".format(rep,foldname)
	try:
		os.mkdir(foldname)
		os.mkdir(foldname+"/FOLDERS")

	except:
		askokcancel("Erreur!", "The folder '{}' already exists, please chose another one...".format(foldname))
		e.delete(0, END)
		e.insert(0, "")
	else:

		configfile = open("config.dat","a")
		configfile.write(foldname);configfile.close()
		cleanfold=foldname
		tkinter.messagebox.showinfo('One more step ! ','Now you just have to add the extensions you want to move by pressing "Add extensions",\n then just chose the folder to keep this particular files...\n\nGood Luck, my email if you want to report bugs : email@exemple.com')
		new_window.destroy()
def addex_add():
	extension= entryex.get()
	if extension=="":
		return tkinter.messagebox.showerror('Error!','Entry empty ! ')
	else:
		while True:
			extfolder = filedialog.askdirectory(initialdir=cleanfold,title="With wich folder you want to assign '.{}' ?".format(extension))
			if extfolder!="":
				configfile = open("config.dat","a")
				configfile.write("\n.{0}<dcv2>{1}".format(extension,extfolder));configfile.close()
				entryex.delete(0, END)
				entryex.insert(0, "")
				return
			else:
				tkinter.messagebox.showerror('Error!','Entry empty ! ')

def addex():
	global entryex,window_addex
	btn1['state']=DISABLED;btn2['state']=DISABLED;btn3['state']=DISABLED;btn4['state']=DISABLED
	window_addex = Toplevel(root)
	window_addex.resizable(0, 0)
	window_addex.geometry('300x100')
	window_addex.title("Add extensions")

	labelex = Label(window_addex, text="Write extension without dot (ex: rar,jpg etc...)")
	labelex.pack()
	entryex = Entry(window_addex)
	entryex.pack()
	ex1 = Button(window_addex,text="Add extensions",command=addex_add)
	ex1.pack()
	exquit = Button(window_addex,text="Return",command=addexexit)
	exquit.pack()
	window_addex.protocol("WM_DELETE_WINDOW",addexexit)
def addexexit():
	btn1['state']=NORMAL;btn2['state']=NORMAL;btn3['state']=NORMAL;btn4['state']=NORMAL
	window_addex.destroy()
def func_movefolds():
	btn1['state']=DISABLED;btn2['state']=DISABLED;btn3['state']=DISABLED;btn4['state']=DISABLED
	fold2mov = filedialog.askdirectory(initialdir="/",title="Wich folder do you want to move ?")
	btn1['state']=NORMAL;btn2['state']=NORMAL;btn3['state']=NORMAL;btn4['state']=NORMAL
	if fold2mov=="":
		return
	else:
		shutil.move(fold2mov, cleanfold.replace("\n","/FOLDERS"))	
	tkinter.messagebox.showinfo('Done!','Folder moved...')
	return
def func_clean():
	global var_chk,choice1,choice2
	choice1,choice2=False,False
	btn1['state']=DISABLED;btn2['state']=DISABLED;btn3['state']=DISABLED;btn4['state']=DISABLED
	extstoclean,storingfolders = [],[]
	configfile = open("config.dat","r")
	configlines= configfile.readlines();configfile.close()
	configlines=configlines[1:]
	for line in range(len(configlines)):
		linesplit=configlines[line].split("<dcv2>")
		extadded=linesplit[0];storfold = linesplit[1].replace("\n","")
		extstoclean.append(extadded);storingfolders.append(storfold)
	dirtoclean = filedialog.askdirectory(initialdir="/",title="Wich folder do you want to clean ?")
	if dirtoclean=="":
		btn1['state']=NORMAL;btn2['state']=NORMAL;btn3['state']=NORMAL;btn4['state']=NORMAL
		return
	else:
		dirtoclean+="/"
	deskfiles = os.listdir(dirtoclean)
	errnum=0
	errfiles=[]
	for ext in range(len(extstoclean)):
		for f in deskfiles:
			if extstoclean[ext] in f:
				try:
					shutil.move("{}".format(dirtoclean+f), storingfolders[ext])
				except Exception:
					tkinter.messagebox.showinfo('Done!','{0} Already exists in {1}, it will not be moved...'.format(f, storingfolders[ext]))
					pass


	btn1['state']=NORMAL;btn2['state']=NORMAL;btn3['state']=NORMAL;btn4['state']=NORMAL
	tkinter.messagebox.showinfo('Done!','Folder cleaned !')
def window_errf_show(file,choice):
	global window_errf,var_chk
	if choice==0:
		var_chk = IntVar()
		window_errf = Toplevel(root)
		window_errf.resizable(0, 0)
		window_errf.geometry('300x100')
		window_errf.title("This file already exists ! ")
		errf_label = Label(window_errf,text="[{}] A file with this name already exists".format(file))
		errf_label.pack()
		errf_btn = Button(window_errf,text="Don't move",command=errf1)
		errf_btn.pack()
		errf_btn2 = Button(window_errf,text="Move but keep both files",command=errf2)
		errf_btn2.pack()
		if errnum>1:
			errf_apply = Radiobutton(window_errf, text="Apply my choice for the next {} files ".format(errnum), variable=var_chk, value=1)
			errf_apply.pack()
	elif choice==1:
		pass
	elif choice==2:
		num = 1
		while True:
			try:
				shutil.move("{}".format(file[0], file[1]))
			except Exception:
				errnum+=1

def errf1():
	global choice1,choice2
	choice = var_chk.get()
	if choice:
		choice1=True
#Create menubar
menubar = Menu(root)
root.config(menu = menubar)
#Create sub-menus
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu = subMenu)
subMenu.add_command(label="Exit", command=exit)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu = subMenu)
subMenu.add_command(label="About DCleaner", command = menu_aboutus)

root.geometry('250x175')
root.title("DirCleaner 2.0.0")
root.iconbitmap('brush.ico')
btn1 = Button(root,text='Clean a folder',command=func_clean)
btn1.pack(expand="yes")
btn2 = Button(root,text='Add extensions',command=addex)
btn2.pack(expand="yes")
btn4 = Button(root,text='Move folders',command=func_movefolds)
btn4.pack(expand="yes")

btn3 = Button(root,text='Exit',command=exit)
btn3.pack(expand="yes")



if not path.exists("config.dat"):
	tkinter.messagebox.showinfo('Welcome!','Welcome to DCleanerV2 ! Its your first time on the program, so you have to enter a name for your storage folder ! \n All files/Folders that you want to move will be moved inside it...\nFollow the step and enjoy ! ')
	createfolder()
else:
	configfile = open("config.dat","r")
	configlines= configfile.readlines();configfile.close()
	cleanfold=configlines[0]

root.protocol("WM_DELETE_WINDOW",exit)
root.mainloop()