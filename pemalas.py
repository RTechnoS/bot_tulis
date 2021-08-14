from PIL import Image, ImageDraw, ImageFont
import re

# =============== RTechS ==============
# =             Script By             = 
# =      Rusman Tobyakta Siregar      =
# =            @rusman_toby           =
# =       rusmants.public@pm.me       =
# =====================================
# 
 # File ini bagian dari:
 # 
 # pemalas 
 # Pembuat tulisan menjadi text di kertas dalam bentuk gambar
 # 
 # Aplikasi dan source code ini dirilis berdasarkan lisensi GPL V3
 # 
 # 
 # Dengan ini diberikan izin, secara gratis, kepada siapa pun yang mendapatkan salinan
 # dari perangkat lunak ini dan file dokumentasi terkait ("Aplikasi Ini"), untuk diperlakukan
 # tanpa batasan, termasuk hak untuk menggunakan, menyalin, mengubah dan/atau mendistribusikan,
 # asal tunduk pada syarat berikut:
 # 
 # Pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus disertakan dalam
 # setiap salinan atau bagian penting Aplikasi Ini. Barang siapa yang menghapus atau menghilangkan
 # pemberitahuan ini melanggar ketentuan lisensi Aplikasi Ini.
 # 
 # PERANGKAT LUNAK INI DISEDIAKAN "SEBAGAIMANA ADANYA", TANPA JAMINAN APA PUN, BAIK TERSURAT MAUPUN
 # TERSIRAT. PENULIS ATAU PEMEGANG HAK CIPTA SAMA SEKALI TIDAK BERTANGGUNG JAWAB ATAS KLAIM, KERUSAKAN ATAU
 # KEWAJIBAN APAPUN ATAS PENGGUNAAN ATAU LAINNYA TERKAIT APLIKASI INI.
 # 
 # @scripy pemalas
 # @author	RTechS - Rusman Tobyakta Siregar
 # @copyright	Hak Cipta 2020 - 2021 RTechS - Rusman Tobyakta Siregar
 # @profile 	https://github.com/rtechnos

alamat = './'
bhn = {
	    'gambar':{
			    1:{'nama':'bahan_1.jpg', 'baris': 25, 'perEnter':92, 'lokasi':[531,347], 'info':[310, 170, 60], 'tgl':[335, 1675], 'nomor':[529,212]},
			    2:{'nama':'bahan_2(1).jpg', 'baris': 25, 'perEnter':104, 'lokasi':[570,322], 'info':[305, 170, 56], 'tgl':[375, 1815], 'nomor':[551,169]},
			    3:{'nama':'bahan_3.jpg', 'baris': 25, 'perEnter':103, 'lokasi':[605,305], 'info':[320, 170, 60], 'tgl':[410, 1780], 'nomor':[598,153]},
			    4:{'nama':'bahan_4.jpg', 'baris': 31, 'perEnter':92, 'lokasi':[505,280], 'info':[255, 130, 56], 'tgl':[315, 1695], 'nomor':[491,100]},
			    5:{'nama':'bahan_5(4).jpg', 'baris': 31, 'perEnter':94, 'lokasi':[515,313], 'info':[300, 140, 60], 'tgl':[320, 1720], 'nomor':[518,145]}
			},
	    
        'font':{    
	            1:{'nama':'font1.ttf', 'ukuran':48, 'autoEnter':{1:79,2:86,3:86,4:85,5:89}},  #succes
	            2:{'nama':'font2.ttf', 'ukuran':67, 'autoEnter':{1:74,2:82,3:82,4:78,5:78}},  #succes
	            3:{'nama':'font3.ttf', 'ukuran':61, 'autoEnter':{1:67,2:73,3:73,4:75,5:76}}
           }
	    }

class Tulis:
	def __init__(self,text='@rusman_toby', kertas=1, font=1, color=(42, 43, 43), info={'':''}, lok='./@awakmalas_bot'):
		self.text = text 
		self.noKertas = int(kertas)
		self.rawKertas = bhn['gambar'][self.noKertas] 
		self.rawFont =  bhn['font'][int(font)] 
		self.color = color
		self.info = info
		self.lokasi = lok
		

	def Menulis(self): #Proses awal nulis (mengambil font dan kertas)
		self.countLoop = 1
		self.kertas = Image.open(alamat+'bahan/'+self.rawKertas['nama'])
		self.d1 = ImageDraw.Draw(self.kertas)

		if 'kurangFont' in self.rawKertas:
			ukuranFont = self.rawFont['ukuran'] - self.rawKertas['kurangFont']
		else:
			ukuranFont = self.rawFont['ukuran']

		self.myfont = ImageFont.truetype(alamat+'bahan/'+self.rawFont['nama'], ukuranFont)

		atasInfo = self.rawKertas['info'][0]
		sampingInfo = self.rawKertas['info'][1]
		for data in self.info.keys():
			if data == 'nama':
				self.d1.text((sampingInfo,atasInfo), 'Nama : '+str(self.info['nama']), font=self.myfont, fill = self.color)
				atasInfo += self.rawKertas['info'][2]
			elif data == 'kelas':
				self.d1.text((sampingInfo,atasInfo), 'Kelas : '+str(self.info['kelas']), font=self.myfont, fill = self.color)
				atasInfo += self.rawKertas['info'][2]
			else:
				self.d1.text((sampingInfo,atasInfo), (data+' : '+self.info[data]), font=self.myfont, fill = self.color)
				atasInfo += self.rawKertas['info'][2]

		proces = self.prosesText()
		return proces

	def prosesText(self): #memfilter text dan merapikan text agar sesuai dengan lebar/tinggi kertas
		enter = self.text.split('\n')
		jumlahEnter = len(enter)
		if jumlahEnter > (self.rawKertas['baris']*2):
			kirim = {'error':True, 'pesan':f"❌ JUMLAH BARIS BERLEBIH ❌\nJumlah Baris anda = {jumlahEnter}\nMaximal Baris pada kertas ini = {self.rawKertas['baris']*2} baris\nKertas lebih besar adalah bigboss, double folio dan dua lembar \n\ncek di /help"}
			return kirim
		else:
			awalAtas = self.rawKertas['lokasi'][0]
			self.textHasil = []
			maxKar = self.rawFont['autoEnter'][int(self.noKertas)]
			for tt in enter:
				panjangKar = len(str(tt))
				txtPtg = []
				while panjangKar > maxKar:
					self.textHasil.append(tt[:maxKar])
					tt = tt[maxKar:]
					panjangKar -= maxKar
				else:
					self.textHasil.append(tt)
			if len(self.textHasil) > (self.rawKertas['baris']*2):
				kirim = {'error':True, 'pesan':f"❌ JUMLAH BARIS BERLEBIH ❌\nJumlah Baris anda = {len(self.textHasil)}\nMaximal Baris pada kertas ini = {self.rawKertas['baris']*2} baris\nKertas lebih besar adalah bigboss, double folio dan dua lembar\n\ncek di /help"}
				return kirim
			return self.prosesNulis()


	def prosesNulis(self): #proses menempelkan teks ke kertas
		jumlahEnter = len(self.textHasil)
		if len(self.textHasil) > self.rawKertas['baris']:
			self.countLoop = 2
		namaFile = []
		aWal = 0

		for i in range(self.countLoop):
			awalAtas, awalSamping = self.rawKertas['lokasi']
			nomorAtas, nomorSamping = self.rawKertas['nomor']
			for num, tt in enumerate(self.textHasil[aWal:self.rawKertas['baris']*(i+1)]):
				panjangKar = len(str(tt))
				if 'duo' in self.rawKertas: 
					if num == (self.rawKertas['baris'] / 2):
						awalAtas = self.rawKertas['lokasi'][0]
						awalSamping += self.rawKertas['duo']['kliSamping']

						nomorAtas = self.rawKertas['nomor'][0]
						nomorSamping += self.rawKertas['duo']['kliSamping']

				self.d1.text((awalSamping, awalAtas), tt, font=self.myfont, fill = self.color)
				awalAtas += self.rawKertas['perEnter']
				nomorAtas += self.rawKertas['perEnter']

			aWal = self.rawKertas['baris']

			__lok = f"{self.lokasi}({i+1}).jpg"
			namaFile.append(__lok)
			self.kertas.save(__lok)
			
			self.kertas = Image.open(alamat+'bahan/'+self.rawKertas['nama'])
			self.d1 = ImageDraw.Draw(self.kertas)

		kirim = {'error':False, 'pesan':f"Jumlah Baris Teks : {jumlahEnter}", 'file':namaFile}
		return kirim

