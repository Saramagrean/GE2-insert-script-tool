#INSERT V.1
with open("GE2_BASE.iso" , "r+b") as iso,open("GOD_EATER_2/TRANSLATE_INDONESIA/AUDIOTEXT/AUDIOTEXT_ISO.txt", 'r', encoding='utf-8')as f,open("___Srigatan___/AUDIOTEXT_ISO.TOC", "rb") as toc:
	def readint(x):
		x = toc.read(x)
		x = int.from_bytes(x, byteorder='little')
		return x
	def readtext(f):
		text = []
		while True :
			c = f.readline()
			if c[5:10] == "-----":
				return "".join(text)
			text.append(c)		
	total = 14982
	i = 0
	nama_msg = f.readline()[5:-1]
	encoding = f.readline()[9:-1]
	CRLF = f.readline()[5:-1]
	ID = f.readline()[3:-1]
	type = f.readline()[5:-1]
	jumlah_string = int(f.readline()[14:-1])
	sam = f.readline()
	sam = f.readline()
	STATUS = f.readline()
	TRANSLATOR = f.readline()
	LAST_CHECK = f.readline()
	sam = f.readline()
	while i < total:
		name = toc.read(0x18).replace(b'\x00', b'').decode('utf-8')
		offset = readint(4)
		size = readint(4)
		iso.seek(offset)
		num= int(f.readline()[1:-2])
		print("INSERT STRING [{0:08d}]".format(num))
		if num != i:
			print("[{0:08d}]".format(num),"SALAH, HARUSNYA[{0:08d}]".format(i))
			print("STRING HILANG")
			break
		string = readtext(f).encode("utf-8")
		sizetext = len(string)-1
		if sizetext-1 >= size:
			print("[{0:08d}]".format(num))
			print("SIZE KEGEDEAN GAN, DISINGKAT SAJA")
			break
		iso.write(string[:-1]+b'\x00')
		i+=1
	print("AUDIO TXT ISO SIP!!!!!")
iso.close()
f.close()
toc.close()
with open("GAME/MOD-IND/PATCH.EDAT" , "r+b") as patch,open("GOD_EATER_2/TRANSLATE_INDONESIA/AUDIOTEXT/AUDIOTEXT_PATCH.txt", 'r',encoding='utf-8')as f,open("___Srigatan___/AUDIOTEXT_PATCH.TOC", "rb") as toc:
	def readint(x):
		x = toc.read(x)
		x = int.from_bytes(x, byteorder='little')
		return x
	def readtext(f):
		text = []
		while True :
			c = f.readline()
			if c[5:10] == "-----":
				return "".join(text)
			text.append(c)
	nama_msg = f.readline()[5:-1]
	encoding = f.readline()[9:-1]
	CRLF = f.readline()[5:-1]
	ID = f.readline()[3:-1]
	type = f.readline()[5:-1]
	jumlah_string = int(f.readline()[14:-1])
	sam = f.readline()
	sam = f.readline()
	STATUS = f.readline()
	TRANSLATOR = f.readline()
	LAST_CHECK = f.readline()
	sam = f.readline()
	i=0
	while i < 279:
		toc.read(0x18)
		offset = readint(4)
		size = readint(4)
		num= int(f.readline()[1:-2])
		print("INSERT STRING [{0:08d}]".format(num))
		if num != i:
			print("[{0:08d}]".format(num),"SALAH, HARUSNYA[{0:08d}]".format(i))
			print("STRING HILANG")
			break
		string = readtext(f).encode("utf-8")
		sizetext = len(string)-1
		if sizetext-1 >= size:
			print("[{0:08d}]".format(num))
			print("SIZE KEGEDEAN GAN, DISINGKAT SAJA")
			break
		patch.seek(offset)
		patch.write(string[:-1]+b'\x00')
		i+=1
	print("AUDIO TXT PATCH SIP!!!!!")
	patch.close()
	f.close()
	toc.close()

		
	
	
	
	
	
	
		
		