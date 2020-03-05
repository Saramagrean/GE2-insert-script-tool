def go_tod(name, f,offset):
	def readint(x):
			x = f.read(x)
			x = int.from_bytes(x, byteorder='big')		#tambah reff
			return x
	f.seek(offset)
	pointer = readint(4)
	csize = readint(4)
	print(name + " {0:08X} ".format(pointer)+ "{0:08X} ".format(csize)+"{0:08X} ".format(offset))
	return ""
#--------------------------------------------------------------
def get_off(name, f,offset):
	def readint(x):
			x = f.read(x)
			x = int.from_bytes(x, byteorder='little')		#tambah reff
			return x
	f.seek(offset)
	pointer = readint(3)*2048
	print(name + " {0:08X} ".format(pointer))
	return pointer
#--------------------------------------------------------------
def get_size(name, f,offset,pl):
	def readint(x):
			x = f.read(x)
			x = int.from_bytes(x, byteorder='little')		#tambah reff
			return x
	f.seek(offset)
	pointer = readint(3)*2048
	id= f.read(1)
	csize= readint(4)
	print(name + " {0:08X} ".format(csize))
	return csize
#--------------------------------------------------------------
def write_size(name, f,offset, csize,dsize):
	f.seek(offset)
	f.read(4)
	f.write((csize).to_bytes(4, byteorder='little', signed=True))
	nameof = f.read(4)
	element = f.read(4)
	null = f.read(12)
	f.write((dsize).to_bytes(4, byteorder='little', signed=True))
	return ""
def go_to(name, f,offset,npoin):
	f.seek(offset)
	f.write((npoin).to_bytes(3, byteorder='little', signed=True))
	f.write(b'\x60')
	ptcsize = f.tell()
	csize = f.read(4)
	nameof = f.read(4)
	element = f.read(4)
	null = f.read(12)
	dsize = f.read(4)
	f.seek(ptcsize)
	f.write(dsize)
	print(name + " {0:08X} ".format(npoin*2048))
	return ""
	
	