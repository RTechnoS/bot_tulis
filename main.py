from PIL import Image, ImageDraw, ImageFont

#Daftar font dan kertas beserta properti nya
bhn = {
    'gambar':{1:{'nama':'bahan_1.jpg', 'baris': 25, 'perEnter':92, 'samping':340, 'atas':540}, #succes
              2:{'nama':'bahan_2(1).jpg', 'baris': 25, 'perEnter':104, 'samping':338, 'atas':570}, #succes
              #3:{'nama':'bahan_3(duo).jpg', 'baris': 25, 'perEnter':90, 'samping':340, 'atas':540, 'tam':2},
              #4:{'nama':'bahan_4(duo).jpg', 'baris': 31, 'perEnter':90, 'samping':340, 'atas':540, 'tam':2},
              3:{'nama':'bahan_5.jpg', 'baris': 25, 'perEnter':103, 'samping':305, 'atas':600}, #succes
              4:{'nama':'bahan_6.jpg', 'baris': 31, 'perEnter':92, 'samping':280, 'atas':505}, #succes
              5:{'nama':'bahan_7(6).jpg', 'baris': 31, 'perEnter':94, 'samping':315, 'atas':515}, #succes
              6:{'nama':'bahan_8.jpg', 'baris': 31, 'perEnter':95, 'samping':325, 'atas':555}, #succes
              7:{'nama':'bahan_9.jpg', 'baris': 25, 'perEnter':102, 'samping':340, 'atas':515}, #succes
              8:{'nama':'bahan_10(9).jpg', 'baris': 25, 'perEnter':106, 'samping':300, 'atas':510} #succes
            },
    
    'font':{1:{'nama':'font1.ttf', 'ukuran':50, 'warna':(0, 0, 0)},  #succes
            2:{'nama':'font2.ttf', 'ukuran':70, 'warna':(0, 0, 0)},  #succes
            3:{'nama':'font3.ttf', 'ukuran':56, 'warna':(0, 0, 0)},  #succes 
            4:{'nama':'font4.ttf', 'ukuran':55, 'warna':(7, 6, 6)}   #succes
           }}

#Untuk user memilih Font dan Kertas 

for gam in bhn['gambar']:
    print(gam,'.',bhn['gambar'][gam]['nama'],'berjumlah',bhn['gambar'][gam]['baris'],'baris')

milihK = int(input('\nPilih kertas : '))

if milihK not in bhn['gambar']:
    milihK = 1
    print('Pilihan anda tidak ada, otomatis diubah ke kertas 1')

for fon in bhn['font']:
    print(fon,'.',bhn['font'][fon]['nama'],'Ukuran :',bhn['font'][fon]['ukuran'])

milihF = int(input('\nPilih Font : '))

if milihF not in bhn['font']:
    milihF = 1
    print('Pilihan anda tidak ada, otomatis diubah ke Font 1')

pilihKertas = bhn['gambar'][milihK]
tulisan =  bhn['font'][milihF]

#########################################################

kertas = Image.open('bahan/'+pilihKertas['nama']) #membuka file kertas yang dipilih
d1 = ImageDraw.Draw(kertas)
myfont = ImageFont.truetype('bahan/'+tulisan['nama'], tulisan['ukuran']) #membuka file font yang dipilih

def proccesText(tex):
    kirim = ""
    enter = tex.split('\n') #Memisahkan text per baris(enter)
    jumlahEnter = len(enter) #jumlah baris
    if jumlahEnter > pilihKertas['baris']:
        kirim = f"Teks tidak boleh lebih dari {pilihKertas['baris']} baris"
    else:
        awalAtas = pilihKertas['atas']
        for tt in enter: #Mengulang text yang sudah dipisah barisnya
            d1.text((pilihKertas['samping'],awalAtas), tt, font=myfont, fill = tulisan['warna']) #proces menulis
            awalAtas += pilihKertas['perEnter'] #Memberi jarak ke baris baru
            
        lokasi = "Hasil.jpg"
        kertas.save(lokasi) #file hasil
        kirim = f"Succes disimpan di {lokasi}\nJumlah Baris Teks : {jumlahEnter}"
    return kirim


#Membuka file Tulisan.txt tempat tulisan kalian
with open('Tulisan.txt', 'r') as viewText:
    textUser = viewText.read()
proces = proccesText(textUser)
print(proces)
