import zlib


def blz_com(f,dsize):
	f.seek(0,0)
	def compress_chunk(size):
		deflate_compress = zlib.compressobj(9, zlib.DEFLATED, -15)
		data = deflate_compress.compress(f.read(size)) + deflate_compress.flush()
		chunksize = len(data).to_bytes(2, byteorder='little', signed=True)
		data = chunksize + data
		return data
#---------------------
	deflate_compress = zlib.compressobj(9, zlib.DEFLATED, -15)
	tail_size = dsize%0xffff
	number_part = dsize//0xffff
#---------------------
	if dsize <=0xffff:
		compressed = None
		compressed = deflate_compress.compress(f.read()) + deflate_compress.flush()
		chunksize = len(compressed).to_bytes(2, byteorder='little', signed=True)
		compressed = b"blz2" + chunksize  + compressed
		return compressed
#---------------------
	else :
		compressed  =b""
		i=0
		head= compress_chunk(tail_size)
		compressed = compressed + head
		while i <number_part-1 :
			chunk = compress_chunk(0xffff)
			compressed = compressed + chunk
			i+=1
		last_chunk = compress_chunk(0xffff)
		compressed = b'blz2' + last_chunk + compressed
		return compressed

			