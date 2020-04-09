# -*- coding:utf-8 -*-
# author:pcat
# http://pcat.cnblogs.com

from Crypto.Cipher import AES

def getBMPheader():
	#bmp是LITTLE-ENDIAN（小字节序、低字节序）
	bfType='424d' #文件类型
	bfSize='360c 3000' #文件大小，本题3148800+54
	bfReserved1='0000' #保留，为0
	bfReserved2='0000' #保留，为0
	bfOffBits='3600 0000' #数据离文件头偏离量
	biSize='2800 0000' #位图信息头的大小
	biWidth='5605 0000' #宽度，本题1366
	biHeight='0003 0000' #高度，本题768
	biPlanes='0100' #颜色平面数，为1
	biBitCount='1800' #比特数/像素，本题24位
	biCompression='0000 0000' #压缩类型，0为不压缩
	biSizeImage='0000 0000' #图像的大小，本题多少无所谓
	biXPelsPerMeter='0000 0000' #水平分辨率，缺省
	biYPelsPerMeter='0000 0000' #垂直分辨率，缺省
	biClrUsed='0000 0000' #使用的颜色索引数，本题多少无所谓
	biClrImportant='0000 0000' #重要的颜色索引数，本题多少无所谓
	bmp_header=bfType+bfSize+bfReserved1+bfReserved2+bfOffBits
	bmp_header+=biSize+biWidth+biHeight+biPlanes+biBitCount+biCompression+biSizeImage
	bmp_header+=biXPelsPerMeter+biYPelsPerMeter+biClrUsed+biClrImportant
	bmp_header=bmp_header.replace(' ','')
	return bmp_header

def foo():
	ciphertext=open('bestwing12345678.bmp','rb').read() #记得有'b'
	key='bestwing12345678'
	obj=AES.new(key,AES.MODE_ECB)
	message=obj.decrypt(ciphertext)
	fsave=open('out.bmp','wb') #记得有'b'
	fsave.write(getBMPheader().decode('hex')+message)
	fsave.close()
	pass

if __name__ == '__main__':
	foo()
	print 'ok'
