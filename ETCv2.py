#INSERT V.1
import os
import sys
sys.path.insert(0, '___Srigatan___/')
dirpath = os.path.dirname(os.path.realpath(__file__))
from ___Srigatan___.pt_off import pt_off
from ___Srigatan___.name import name
from ___Srigatan___.new_poin import new_poin
from ___Srigatan___.func import go_to
from ___Srigatan___.func import write_size
from ___Srigatan___.func import go_tod
from ___Srigatan___.func import get_off
from ___Srigatan___.func import get_size
from ___Srigatan___.nama_txt import nama_txt
from ___Srigatan___.nama_file import nama_file
from ___Srigatan___.txt2msg import txt2msg
from ___Srigatan___.nama_tr2 import nama_tr2
from ___Srigatan___.nama_tr2_new import nama_tr2_new
from ___Srigatan___.tr2repack import tr2_repack
from ___Srigatan___.blzcompress import blz_com
from ___Srigatan___.mission import MISSION_KST
from ___Srigatan___.article import ARTICLE_KST
from ___Srigatan___.article_ex import ARTICLE_EX_KST






with open('GE2_BASE.iso', 'r+b') as iso:
	file_loc ={
"0013_game_text.tr2":iso,
"0019_game_text.tr2":iso,
"0028_game_text.tr2":iso,
}
#-------------------------------REPACK TR2-----------------------------------------------------------------------		

	def CONVERT_TXT():
			i=0
			while i<75:
				f = open(nama_txt[i], 'r', encoding='utf-8')
				out = open(nama_file[i],'wb')
				txt2msg(f,out)
				i+=1
			return ""
#-------------------------------REPACK TR2-----------------------------------------------------------------------		
	def REPACK_TR2():
		i= 0
		while i <74:
			tr2_repack(nama_tr2[i], nama_tr2_new[i])
			i+=1


#-------------------------------INSERT TR  MOD 2 KE ISO-----------------------------------------------------------------------
	def INSERT_TR2_MOD():
		i=0
		while i<85:
			k = name[i]
			new_tr2 = open("___Srigatan___/TR2NEW/" + k, 'rb')
			dsize = len(new_tr2.read())
			insert_file  = blz_com(new_tr2,dsize)
			csize = len(insert_file)
			write_size(k, file_loc[k], pt_off[k], csize, dsize)
			patch.seek(offset)
			patch.write(insert_file)
			patch.write(b'\x00'*0x100)
			print("INSERT", k)
			i+=1
#-----------------------------------------------------------------------------------------------------
	CONVERT_TXT()
	REPACK_TR2()
	print("SIP GAN!!!!!!!!!")