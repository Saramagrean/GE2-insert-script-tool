import os

def tr2_repack(input, output):
	f = open(input, "rb")
	out = open(output, 'wb')

#--------------------------------------------------
	def newfile(input,name):
		newname = input[:-4].replace("TR2/","TR2_UNPACK/")
		fullfile = open(newname +"/" + name, "rb")
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


