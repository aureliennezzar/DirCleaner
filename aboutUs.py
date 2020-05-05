def menu_aboutus():
	extstoclean,storingfolders = [],[]
	aboutlist = ""
	configfile = open("config.dat","r")
	configlines= configfile.readlines();configfile.close()
	configlines=configlines[1:]
	for line in range(len(configlines)):
		linesplit=configlines[line].split("<dcv2>")
		extadded=linesplit[0];storfold = linesplit[1].replace("\n","")
		aboutlist+= "{0}  >>>   {1}\n".format(extadded, storfold.split("/")[-1])
	tkinter.messagebox.showinfo('About Us','Version 0.7\n\nBy: Jin\nStorage folder : {0}\nExtensions/Folder : \n{1}'.format(cleanfold,aboutlist))
