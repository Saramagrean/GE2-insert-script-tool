#INSERT V.1
import os
import sys
sys.path.insert(0, '___Srigatan___/')
dirpath = os.path.dirname(os.path.realpath(__file__))
from ___Srigatan___.txt2msg import txt2msg
from shutil import copyfile
import zlib
def tr2_repack(input, output):
	f = open(dirpath + "/" + input, "rb")
	out = open(dirpath + "/" + output, 'wb')

#--------------------------------------------------
	def newfile(input,name):
		newname = input[:-4].replace("TR2/","SYSTEM_UPDATE_UNPACK/")
		fullfile = open(dirpath + "/" + newname +"/" + name, "rb")
		fullfile = fullfile.read()
		return fullfile
    
#--------------------------------------------------
	def readString(f):
		chars = []
		while True:
			c = f.read(1).decode('utf-8')
			if c == chr(0):
				return "".join(chars)
			chars.append(c)
#--------------------------------------------------
	def readint(x):
		x = f.read(x)
		x = int.from_bytes(x, byteorder='little')
		return x
#--------------------------------------------------
	name = os.path.basename(f.name)
	name = name[:-3] + "tr2"
	print("REPACK" ,name)
	f.seek(0x44)
	toc_size = readint(4)
	f.seek(0,0)
	x = f.read(toc_size)
	out.write(x)
	f.seek(0x38,0)
	headsize = readint(4)
	total = readint(4)
	k = 0
	while k < total:
		out.seek(0,2)
		num = readint(4)
		pt_off = f.tell()
		offold= readint(4)
		id = readint(4)
		pt_size = f.tell()
		sizeold = readint(4)
		sizeold = readint(4)
		nexti = f.tell()
		f.seek(offold)
		namefile = f.read(48).replace(b'\x00', b'').decode('utf-8')
		print("Insert", namefile)
		offset = out.tell()
		file_insert = newfile(input,namefile)
		size = len(file_insert)
		out.write(file_insert)
		out.seek(pt_off)
		out.write(offset.to_bytes(4, byteorder='little', signed=True))
		out.seek(pt_size)
		out.write(size.to_bytes(4, byteorder='little', signed=True))
		out.write(size.to_bytes(4, byteorder='little', signed=True))#
		f.seek(nexti)
		k +=1



def writeint(x, y):
	newPres.write(x.to_bytes(y, byteorder='little', signed=True))
	return x
def blz_com(data):
	BLZCOM = zlib.compressobj(9, zlib.DEFLATED, -15)
	compressed = None
	compressed = BLZCOM.compress(data) + BLZCOM.flush()
	chunksize = len(compressed).to_bytes(2, byteorder='little', signed=True)
	compressed = b"blz2" + chunksize  + compressed
	return compressed
def readString():
	chars = []
	while True:
		c = toc.read(1).decode('utf-8')
		if c == chr(0):
			return "".join(chars)
		chars.append(c)
imput =("GOD_EATER_2/TRANSLATE_INDONESIA/SYSTEM/0000_COMMON_MESSAGE.txt",
"GOD_EATER_2/TRANSLATE_INDONESIA/SYSTEM/0001_SAVEDATA_TEXT.txt",
"GOD_EATER_2/TRANSLATE_INDONESIA/SYSTEM/0002_NETWORK_MESSAGE.txt")
output=("___Srigatan___/SYSTEM_UPDATE_UNPACK/common_text/COMMON_MESSAGE",
"___Srigatan___/SYSTEM_UPDATE_UNPACK/common_text/SAVEDATA_TEXT",
"___Srigatan___/SYSTEM_UPDATE_UNPACK/network_text/NETWORK_MESSAGE" )
i=0
while i <3:
	f = open(dirpath + "/" + imput[i], 'r', encoding='utf-8')
	msg = open(dirpath + "/" + output[i], 'wb')
	txt2msg(f,msg)
	i+=1
tr2_repack("___Srigatan___/TR2/common_text.tr2", "___Srigatan___/SYSTEM_UPDATE_UNPACK/common_text.tr2")
tr2_repack("___Srigatan___/TR2/network_text.tr2", "___Srigatan___/SYSTEM_UPDATE_UNPACK/network_text.tr2")
copyfile(dirpath + "/" + "GOD_EATER_2/TRANSLATE_INDONESIA/SYSTEM/menu_font.conf.txt", dirpath + "/" + "___Srigatan___/SYSTEM_UPDATE_UNPACK/menu_font.conf")
def readint(x,f):
	x = f.read(x)
	x = int.from_bytes(x, byteorder='little')	#tambah reff
	return x
def fileload(x):
	fullfile = open(dirpath + "/" + "___Srigatan___/SYSTEM_UPDATE_UNPACK/" +  name, "rb")
	fullfile = fullfile.read()
	return fullfile
    		
with open(dirpath + "/" + "___Srigatan___/SYSTEM_UPDATE.EDAT", 'rb') as toc,open(dirpath + "/" + "GAME/MOD-IND/SYSTEM_UPDATE.EDAT", 'wb') as newPres:
	magic = toc.read(8)
	print("REPACK SYSTEM")
	unk = toc.read(8)
	tsize = readint(4,toc)
	toc.seek(0,0)
	ntoc = toc.read(tsize)
	newPres.write(ntoc)
	toc.seek(0xe0)
	i = 0
	pointer=()
	while i <24:
		oldfile_off = readint(3,toc)			
		id_grup = readint(1,toc)
		oldcsize = readint(4,toc)			
		oldname_off = readint(4,toc)			
		name_element = readint(4,toc)		
		null = toc.read(12)			
		olddsize = readint(4,toc)			
		next = toc.tell()			
		toc.seek(oldname_off)
		namef = readint(4,toc)		
		toc.seek(namef)		
		name = readString()
		ext = readString()
		name = name +"."+ext
		print(name)
		newfile = fileload(name)
		dsize = len(newfile)
		if oldcsize!= olddsize:
			newfile = blz_com(newfile)
			csize = len(newfile)
		else:
			csize = len(newfile)
		offset = newPres.tell()
		#pointer= pointer+(hex(offset)+hex(csize)+hex(dsize),)
		pointer= pointer+(offset,csize,dsize)
		newPres.write(newfile)
		if csize!=0:
			k = (16-(csize%16))
			if k !=16:
				newPres.write(b'\x00' *k)
		toc.seek(next)
		i+=1
	newPres.seek(0xe0)
	z= 0
	k=0
	while z <24:
		writeint(pointer[k],3)
		newPres.seek(1,1)
		k+=1
		writeint(pointer[k],4)
		k+=1
		newPres.seek(20,1)
		writeint(pointer[k],4)
		k+=1
		z+=1
		
		
		
	
	
	