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
	tkinter.messagebox.showinfo('About DCleaner','Version: 2.0.0 / Author: Jin\n\n----Your storage folder location---- \n\n>>>> {0}\n----Your extensions/folders saved ----\n\n{1}'.format(cleanfold,aboutlist))
