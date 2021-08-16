import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from PIL import Image, ImageTk
import pemalas

# =============== RTechS ==============
# =             Script By             = 
# =      Rusman Tobyakta Siregar      =
# =            @rusman_toby           =
# =       rusmants.public@pm.me       =
# =====================================


bhn = pemalas.bhn #mengambil list kertas dan font dari pemalas.py

class Dashboard:
	def __init__(self, master):
		self.win = master
		self.win.geometry('800x575')
		self.win.title('Pemalas @rusman_toby')
		p1 = tk.PhotoImage(file = 'media/logo.png')
		self.win.iconphoto(True, p1)
		self.win.resizable(False, False)

		self.waktu = datetime.datetime.now()
		self.hari = self.waktu.strftime('%Y-%m-%d')

		self.frm_utama = tk.Frame(self.win)
		self.frm_utama.pack(fill=tk.BOTH, expand=True, padx=11, pady=11)

		self.lbl_status = tk.StringVar()
		self.lbl_status.set('Ready ...')

		self.sty_atas()
		self.sty_bawah()

		self.win.mainloop()


################### Bagian atas window utama ###########################

	def messageBox(self, win,tipe='info',title='p', pesan='p'):

		def close():
			ms.destroy()

		ms = tk.Toplevel(win)
		ms.title(title)
		ms.resizable(False, False)		
		if tipe == 'info':
			tk.Label(ms, text=pesan,font=('calibri', 15)).pack(pady=20,padx=20)
			tk.Button(ms, text='OK', font=('calibri', 10), command=close).pack(pady=(0,10))


	def def_cekbox_tanggal(self):
		if self.var_check.get():
			self.txt_tanggal.config(state='normal')
			self.tanggal.set(self.hari)
		else:
			self.tanggal.set('')
			self.txt_tanggal.config(state='disabled')

	def sty_atas(self):
		self.frm_atas = tk.Frame(self.frm_utama)
		self.frm_atas.pack(fill=tk.BOTH)
		self.def_frm_detail()
		self.def_frm_option()


	def def_frm_option(self):
		frm_option = tk.Frame(self.frm_atas)
		frm_option.grid(row=0, column=1, padx=20)

		self.kertas = tk.StringVar()
		self.kertas.set('Kertas 1')

		self.font = tk.StringVar()
		self.font.set('Font 1')

		self.warna = tk.IntVar()
		self.warna.set(0)

		list_kertas = []
		for i in bhn['gambar']:
			list_kertas.append(f'Kertas {i}')

		#list_kertas = ('Kertas 1', 'Kertas 2', 'Kertas 3', 'Kertas 4', 'Kertas 5')
		list_font = []
		for i in bhn['font']:
			list_font.append(f'Font {i}')

		tk.Label(frm_option, text = 'Kertas : ').grid(row=0, column=0, sticky="W")
		combo_kertas = ttk.Combobox(frm_option, state='readonly',textvariable=self.kertas, values=list_kertas, width=12).grid(row=0, column=1)
		tk.Label(frm_option, text = 'Font    : ').grid(row=1, column=0, sticky="W")
		combo_font = ttk.Combobox(frm_option, state='readonly',textvariable=self.font, values=list_font,width=12).grid(row=1, column=1)

		tk.Label(frm_option, text = 'Warna : ').grid(row=2, column=0, sticky="W")
		tk.Radiobutton(frm_option, text="Hitam", variable=self.warna, value=0).grid(row=2, column=1,sticky="E")
		tk.Radiobutton(frm_option, text="Merah", variable=self.warna, value=1).grid(row=2, column=2,sticky="E")
		tk.Radiobutton(frm_option, text="Biru", variable=self.warna, value=2).grid(row=2, column=3,sticky="E")

		tk.Button(frm_option, text='Preview', command=self.filter_preview).grid(row=3, column=0)

	def def_frm_detail(self):
		frm_detail = tk.Frame(self.frm_atas)
		frm_detail.grid(row=0, column=0)

		self.title_1 = tk.StringVar(); self.title_1.set('')
		self.isi_1 = tk.StringVar(); self.isi_1.set('')

		self.title_2 = tk.StringVar(); self.title_2.set('')
		self.isi_2 = tk.StringVar(); self.isi_2.set('')

		self.title_3 = tk.StringVar(); self.title_3.set('')
		self.isi_3 = tk.StringVar(); self.isi_3.set('')

		self.tanggal = tk.StringVar(); self.tanggal.set(self.hari)
		self.var_check = tk.IntVar()

		tk.Label(frm_detail, text='Judul').grid(row=0, column=0)
		tk.Label(frm_detail, text='Isi').grid(row=0, column=2)

		tk.Entry(frm_detail, textvariable=self.title_1, width=10).grid(row=1, column=0, pady=3)
		tk.Label(frm_detail, text=' = ').grid(row=1, column=1)
		tk.Entry(frm_detail, textvariable=self.isi_1).grid(row=1, column=2)

		tk.Entry(frm_detail, textvariable=self.title_2, width=10).grid(row=2, column=0, pady=3)
		tk.Label(frm_detail, text=' = ').grid(row=2, column=1)
		tk.Entry(frm_detail, textvariable=self.isi_2).grid(row=2, column=2)

		tk.Entry(frm_detail, textvariable=self.title_3, width=10).grid(row=3, column=0, pady=3)
		tk.Label(frm_detail, text=' = ').grid(row=3, column=1)
		tk.Entry(frm_detail, textvariable=self.isi_3).grid(row=3, column=2)

		self.txt_tanggal = tk.Entry(frm_detail, textvariable=self.tanggal)
		self.txt_tanggal.grid(row=4, column=2)
		checkbtn_tgl = tk.Checkbutton(frm_detail, text='Tanggal', variable=self.var_check, command=self.def_cekbox_tanggal)
		checkbtn_tgl.select()
		checkbtn_tgl.grid(row=4, column=0)

		tk.Label(frm_detail, text=' = ').grid(row=4, column=1)


################### Bagian bawah window utama #############################


	def upd_preview(self):
		isi = open('./tugas.txt', 'r').read()
		self.txt_view.configure(state='normal')
		self.txt_view.delete('0.0', tk.END)
		self.txt_view.insert("0.0",isi)
		self.txt_view.configure(state='disabled')

	def sty_bawah(self):

		frm_bawah = tk.Frame(self.frm_utama, bg='blue')
		frm_bawah.pack(fill=tk.BOTH,expand=True, pady=(30,0))

		self.txt_view = tk.Text(frm_bawah, width=95, height=20)
		self.txt_view.grid(row=0, column=0)

		scroll_view = tk.Scrollbar(frm_bawah,orient="vertical", command=self.txt_view.yview)
		self.txt_view.configure(yscrollcommand=scroll_view.set)
		scroll_view.grid(row=0, column=1,sticky=tk.N+tk.S)

		
		self.upd_preview()
		frm_bawah2 = tk.Frame(frm_bawah, bg='blue')
		frm_bawah2.grid(row=1, column=0, pady=7, sticky='EW')
		tk.Label(frm_bawah2, textvariable=self.lbl_status, bg='blue', fg='white').pack(side='left', padx=5)

		frm_btn = tk.Frame(frm_bawah2, bg='blue')
		frm_btn.pack(side='right')

		tk.Button(frm_btn, text='Edit Tugas',command=self.win_texteditor).grid(row=0, column=1,padx=9)

		tk.Button(frm_btn, text='Mulai Kerjakan', command=self.filter_kerjakan).grid(row=0, column=2)
		

	################################ Fungsi Utama #######################################

	def filter_kerjakan(self):
		info = {}
		p = ((self.title_1.get(),self.title_2.get(),self.title_3.get()), (self.isi_1.get(),self.isi_2.get(),self.isi_3.get()))
		for title, isi in zip(p[0],p[1]):
			if title != '':
				info[title] = isi
		
		if self.var_check.get() and self.tanggal.get() != '':
			info['tanggal'] = self.tanggal.get()


		listTinta = ((42, 43, 43), (168, 9, 12), (6, 14, 118))
		opt = [int(self.kertas.get().strip('Kertas ')),int(self.font.get().strip('Font ')), listTinta[self.warna.get()]]
		isi = open('./tugas.txt', 'r').read()
		self.kerjakan(opt, info, isi)

	def filter_preview(self):
		isi = """1. Ini adalah Contoh kertas dan Font
   - @rusman_toby

2. Ini adalah Contoh kertas dan Font"""

		listTinta = ((42, 43, 43), (168, 9, 12), (6, 14, 118))
		opt = [int(self.kertas.get().strip('Kertas ')),int(self.font.get().strip('Font ')), listTinta[self.warna.get()]]
		p = self.kerjakan(opt, {}, isi)



	def kerjakan(self, opt, info, isi):
		jam = datetime.datetime.now().strftime('%H-%M-%S')
		
		p = pemalas.Tulis(isi, opt[0], opt[1], opt[2], info, f'hasil/{jam}')
		hasil = p.Menulis()

		if hasil['error']:
			self.messageBox(self.win,'info','Error',hasil['pesan'])
			self.lbl_status.set('Gagal buat tugas')
		else:
			fl = '\n'.join(hasil['file'])
			pe = 'Succes\n'+fl
			self.messageBox(self.win,'info','Berhasil', pe)
			self.lbl_status.set('Sukses buat tugas')
		

	################## Window edit tugas / tugas editor ##########################


	def save_tugas(self):
		with open('./tugas.txt', 'w') as tulis:
			tulis.write(self.txt_edit.get('0.0', tk.END))
		self.upd_preview()
		self.lbl_status.set('Tugas Berhasil di save')


	def resetTugas(self):
		if messagebox.askokcancel("Reset", "Tugas akan direset, dan menjadi kosong"):
			with open('./tugas.txt', 'w') as rst:
				rst.write('')
			self.txt_edit.delete('0.0', tk.END)
			self.txt_edit.insert("0.0",'')
			self.lbl_status.set('Tugas Berhasil di reset')
			self.upd_preview()
			

	def win_texteditor(self):
		text = open('./tugas.txt', 'r').read()
		win_texteditor = tk.Toplevel(self.win)

		win_texteditor.geometry('720x720')
		win_texteditor.title('Tugas Editor - Pemalas @rusman_toby')
		win_texteditor.resizable(False, True)

		self.frm_utama_2 = tk.Frame(win_texteditor)
		self.frm_utama_2.pack(fill=tk.BOTH, expand=True, padx=11, pady=(0,11))

		self.txt_edit = tk.Text(self.frm_utama_2, width=85, height=37)
		self.txt_edit.insert('0.0', text)

		tk.Button(self.frm_utama_2, text='Reset Tugas', command=self.resetTugas).grid(row=0,column=0, sticky=tk.E, pady=(5))


		self.txt_edit.grid(row=1, column=0)

		scroll_view = tk.Scrollbar(self.frm_utama_2, orient="vertical", command=self.txt_edit.yview)
		self.txt_edit.configure(yscrollcommand=scroll_view.set)
		scroll_view.grid(row=1, column=1,sticky=tk.N+tk.S)


		tk.Button(win_texteditor, text='Close', command=win_texteditor.destroy).pack(side="left")
		tk.Button(win_texteditor, text='Save', command=self.save_tugas).pack(side='right', fill=tk.BOTH, expand=True)


Dashboard(tk.Tk())