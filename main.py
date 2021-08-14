from PIL import Image, ImageDraw, ImageFont
import time, os
import pemalas

# =============== RTechS ==============
# =             Script By             = 
# =      Rusman Tobyakta Siregar      =
# =            @rusman_toby           =
# =       rusmants.public@pm.me       =
# =====================================

waktuFile = time.strftime("%y%m%d-%H%M%S")
bhn = pemalas.bhn

def clear(): # untuk membersihkan/menghapus tampilan terminal/cmd
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def pilih():
    for gam in bhn['gambar']:  # Menampilkan list kertas
        print(gam,'.',bhn['gambar'][gam]['nama'],'berjumlah',bhn['gambar'][gam]['baris'],'baris')

    milihKertas = input('\nPilih kertas : ')
    
    if milihKertas not in str(bhn['gambar'].keys()) or milihKertas == '':
        milihKertas = 1
        print('Otomatis diubah ke kertas 1\n')

    for fon in bhn['font']: # Menampilkan list font
        print(fon,'.',bhn['font'][fon]['nama'],'Ukuran :',bhn['font'][fon]['ukuran'])

    milihFont = input('\nPilih Font : ')

    if milihFont not in str(bhn['font'].keys()) or milihFont == '':
        milihFont = 1
        print('Otomatis diubah ke Font 1\n')

    print("\nKosongkan Jika tidak ingin mencetak Nama & Kelas diatas kertas")
    InNama = str(input("Nama : "))
    InKelas = str(input("Kelas : "))

    info = {}
    if InNama != '':
        info['nama']=InNama

    if InKelas != '':
        info['kelas']=InKelas

    print("Silahkan Di tunggu")
    return milihKertas, milihFont, info


clear() 
print("\n\t\tRusman Tobyakta Siregar\n\t\t@rusman_toby\n")

while True:
    milihK, milihF, info = pilih() 

    with open('Tulisan.txt', 'r', encoding='utf-8') as viewText: #Membaca File Tulisan.txt 
        textUser = viewText.read()
    lok = f'./hasil/{waktuFile}' # masukkan nama file tanpa ekstansi, misal ingin menyimpan menjadi "tugas.jpg" maka hapus ".jpg" dan sisahkan "tugas"
    prs = pemalas.Tulis(text=textUser, kertas=milihK, font=milihF, info=info, lok=f'{lok}')
    procces = prs.Menulis()

    clear()

    if procces['error']:
        print("\n=================== Failed ===================")
    else:
        print("\n================= Success ==================")
        print(f"""File : {' | '.join(procces['file'])}""")

    print(procces['pesan'],"\n\n","="*51,"\n")