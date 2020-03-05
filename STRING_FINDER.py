#INSERT V.1
import os
import sys
import glob
import errno
#------------------------------------------------------------------------------------------------------
dirpath = os.path.dirname(os.path.realpath(__file__))
#------------------------------------------------------------------------------------------------------
path = dirpath +"/GOD_EATER_2/TRANSLATE_INDONESIA/**/" + "*.txt"
k = input("STRING NYA : ")
k = k.encode("utf-8")
files =glob.glob(path)
for file in files:
	def readtext(txt):
		text = []
		while True :
			c = txt.readline()
			if c[5:10] == "-----":
				return "".join(text)
			text.append(c)
#---------------------------------------
	f =open(file, 'rb')
	txt = open(file,'r',encoding='utf-8')
	s = f.read()
	p = s.find(k)
	name = os.path.basename(f.name)
	x = int(p)
	
	if p != -1:
		txt.seek(x,0)
		string = readtext(txt)
		print ("NAMA FILE=",name)
		print(string)