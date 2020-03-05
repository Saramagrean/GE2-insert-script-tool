import os
import sys
import glob
import errno
def txt2msg(f ,msg):
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
	def readint(x):
		x = f.read(x)
		x = int.from_bytes(x, byteorder='little')
		return x
#------------------------------------------------------------------------------------------------------
	def writeint(x, y):
		msg.write(x.to_bytes(y, byteorder='little', signed=True))
		return x
#------------------------------------------------------------------------------------------------------
	def readString(f):
		chars = []
		while True:
			c = f.read(1).decode('utf-8')
			if c == chr(0):
				return "".join(chars)
			chars.append(c)
#------------------------------------------------------------------------------------------------------
	def readtext(f):
		text = []
		while True :
			c = f.readline()
			if c[5:10] == "-----":
				return "".join(text)
			text.append(c)
#------------------------------------------------------------------------------------------------------
	def utf8_2_msg(f,msg,CRLF):
		i = 0
		pointer =()
		while i < jumlah_string:
			offset = msg.tell()
			pointer = pointer + (offset,)
			string = readtext(f).encode('utf-8')
			if CRLF =="<br>":
				string = string[:-1].replace(b"\x0A", b"<br>")
			else:
				string =string[:-1]
			msg.write(string + pad)
			i+=1
		pointer = pointer +(msg.tell(),)
		msg.write(pad *(16-(msg.tell()%16)))
		msg.seek(pt)
		i = 0
		while i <len(pointer):
			writeint(pointer[i], 4)
			i+=1
#------------------------------------------------------------------------------------------------------	
	def utf8yobi_2_msg(f,msg,CRLF):
		i = 0
		pointer =()
		while i < jumlah_string:
			offset = msg.tell()
			num = f.readline()
			"""lif len(num)!= 7:
				print(filename)
				print(num+"^^^^^^^RUSAK! BETULIN")
				break"""
			num = int(num[1:-2])
			string = readtext(f).encode('utf-8')
			if CRLF =="<br>":
				string = string[:-1].replace(b"\x0A", b"<br>")
			else:
				string =string[:-1]
			pointer = pointer + (num, offset, len(string),)
			msg.write(string + pad)
			i+=1
		msg.write(pad *(16-(msg.tell()%16)))
		msg.seek(pt)
		i = 0
		while i <len(pointer):
			writeint(pointer[i], 4)
			i+=1
#------------------------------------------------------------------------------------------------------
	def utf16yobi_2_msg(f,msg,CRLF):
		i = 0
		pointer =()
		while i < jumlah_string:
			offset = msg.tell()
			num = f.readline()
			"""if len(num)!= 7:
				print(filename)
				print(num+"^^^^^^^RUSAK! BETULIN")
				break"""
			num = int(num[1:-2])
			string = readtext(f).encode('utf-16')
			len_str = len(string)-4
			pointer = pointer + (num, offset,len_str,)
			msg.write(string[2:-2] +(pad*2))
			i+=1
		msg.write(pad *(16-(msg.tell()%16)))
		msg.seek(pt)
		i = 0
		while i <len(pointer):
			writeint(pointer[i], 4)
			i+=1
#------------------------------------------------------------------------------------------------------
	pad = b'\x00'
	filename = os.path.basename(f.name)
	print("convert ",filename)
	nama_msg = f.readline()[5:-1]
	encoding = f.readline()[9:-1]
	CRLF = f.readline()[5:-1]
	ID = f.readline()[3:-1]
	type = f.readline()[5:-1]
	jumlah_string = int(f.readline()[14:-1])
	sam = f.readline()
	CODE = f.readline()
	sam = f.readline()
	STATUS = f.readline()
	TRANSLATOR = f.readline()
	LAST_CHECK = f.readline()
	poin = int(CODE[1:9])
	unk1 = int(CODE[10:18])
	unk2 = int(CODE[19:27])
	unk3 = int(CODE[28:36])
	unk4 = int(CODE[37:45])
	unk5 = int(CODE[46:54])
	sam = f.readline()
	msg.write(nama_msg.encode('utf-8'))
	msg.write(pad*(48-len(nama_msg)))
	msg.write(ID.encode('utf-8'))
	msg.write(pad*(8-len(ID)))
	msg.write(type.encode('utf-8'))
	msg.write(pad*(4-len(type)))
	writeint(unk1, 2)
	writeint(unk2, 2)
	msg.write(encoding.encode('utf-8'))
	msg.write(pad*(52-len(encoding)))
	writeint(unk3, 4)
	writeint(unk4, 2)
	writeint(unk5, 2)
	writeint(jumlah_string, 4)
	pt = msg.tell()
	msg.write(pad*(poin - pt))
	if encoding+type =="UTF-8":
		utf8_2_msg(f,msg,CRLF)
	elif encoding+type =="UTF-8yobi":
		utf8yobi_2_msg(f,msg,CRLF)
	elif encoding + type =="UTF-16LEyobi":
		utf16yobi_2_msg(f,msg,CRLF)
	else:
		print(filename)
		print("ENCODING TIDAK DIKETAHUI/RUSAK, HARAP DIBETULKAN :)")	
		
