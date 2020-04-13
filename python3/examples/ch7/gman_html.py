# 小綠人點矩陣
gman = [ 0x180 , 0x3c0 , 0x180 , 0xc0 , 0xf0 , 0xe8 , 0x164 ,
         0x264 , 0x70 , 0x50 , 0x8e , 0x81 , 0x82 , 0x300 ]

# 每個小綠人為 14x10 點矩陣構成
R , C = 14 , 10

headstr = '''
<!DOCTYPE html>
<html>
<head>
   <meta charset="UTF-8">
   <title>小 綠 人</title>
   <style>
      .red {width:10mm;height:10mm;background-color:red;}
      .green {width:10mm;height:10mm;background-color:green;}
      .blue {width:10mm;height:10mm;background-color:blue;}
      .white {width:10mm;height:10mm;background-color:white;}
   </style>
</head>
'''

stys = [ "red" , "green" , "blue" ]
wsty = "white"

tailstr = "</body>\n</html>\n"  

# 產生 html 語法檔
with open( "gman.htm","w") as outfile :

	outfile.write( headstr )
	outfile.write( "<body>\n<table>\n" )

	# 每列
	for r in range(R) :

		outfile.write( "<tr>\n" )

		# 每個小綠人
		for k in range(3) :

			# 每行
			for c in range(C-1,-1,-1) :

				if gman[r] & ( 1 << c ) :
					outfile.write( '<th class="' + stys[k] + '"></th>\n' )
				else :
					outfile.write( '<th class="' + wsty + '"></th>\n' )

			outfile.write( '<th class="' + wsty + '"></th>\n' )

		outfile.write( "</tr>\n" )

	outfile.write( "</table>\n" ) 
	outfile.write( tailstr )
