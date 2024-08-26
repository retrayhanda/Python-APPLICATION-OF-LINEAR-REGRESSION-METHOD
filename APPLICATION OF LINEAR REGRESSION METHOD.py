import getpass
import math

# Definisi warna menggunakan ANSI escape codes
HITAM = "\033[30m"
MERAH = "\033[31m"
HIJAU = "\033[32m"
KUNING = "\033[33m"
BIRU = "\033[34m"
MAGENTA = "\033[35m"
SIAN = "\033[36m"
PUTIH = "\033[37m"
RESET = "\033[0m"

class Cover:
    def coveran(self):
        print(f"""{BIRU}
||=====================================================================================================||
||                  PENERAPAN METODE REGRESI LINIER DALAM APLIKASI SISTEM PERAMALAN                    ||
||                              JUMLAH BAHAN BAKU UNTUK PRODUKSI TAHU                                  ||
||=====================================================================================================||
||                                                                                                     ||
||                                            DISUSUN OLEH:                                            ||
||                                         Rahmad Haret Rayhanda                                       ||
||                                                                                                     ||              
||=====================================================================================================||{RESET}""")

    def intro(self):
        width = 105
        print(f"{KUNING}{'-'*60}{RESET}".center(width + 8))
        print(f"{KUNING}|            Selamat Datang di Program Peramalan            |{RESET}".center(width + 8))
        print(f"{KUNING}{'-'*60}{RESET}".center(width + 8))
        print("="*105)

cover = Cover()

class Login:
    def menu_1(self):
        while True:
            print(f"{KUNING}Silahkan masukkan pilihan anda!{RESET}".center(105 + 8))
            print(' '.ljust(46) + ("1. Log in"))
            print(' '.ljust(46) + ("2. Registrasi"))
            choice = input(' '.ljust(40) + ("masukkan pilihan (1/2) :"))
            if choice == '1':
                print('-' * 105)
                print(f"{KUNING}|   Silahkan Log in   |{RESET}".center(105 + 8))
                print('-' * 105)
                self.login()
                break
            elif choice == '2':
                print('-' * 105)
                print(f"{KUNING}|   Silahkan Buat Akun Anda   |{RESET}".center(105 + 8))
                print('-' * 105)
                self.buat_akun()
                break
            else:
                print("Data Invalid. Silahkan masukkan opsi yang tersedia.")

    def login(self):
        h = 3
        while h > 0:
            username = input(' '.ljust(35) + ("masukkan username anda :"))
            password = input(' '.ljust(35) + ("masukkan password anda :"))
            if username == "kelompok 4C" and password == 'keren':
                print(f"{MAGENTA}Log in diterima, Selamat datang Kelompok 4C!{RESET}".center(105 + 8))
                break
            else:
                h -= 1
                if h > 0:
                    print(f"{MAGENTA}Log in ditolak, silahkan coba lagi.{RESET}".center(105 + 8))
                else:
                    print(f"{MAGENTA}Kesempatan habis. Silahkan Daftar Akun.{RESET}".center(105 + 8))
                    self.buat_akun()

    def buat_akun(self):
        nama = input(' '.ljust(40) + ("Username :"))
        pw = input(' '.ljust(40) + ("Password :"))
        print('-' * 105)
        print(f"{MAGENTA}Akun anda berhasil dibuat! Silahkan Log in.{RESET}".center(105 + 8))
        h = 3
        while h > 0:
            user_2 = str(input(' '.ljust(40) + ("masukkan username anda :")))
            pwd_2 = str(getpass.getpass(' '.ljust(40) + ("masukkan password anda :")))
            if nama == user_2 and pw == pwd_2:
                print(f"{MAGENTA}Log in diterima, Selamat datang {nama}!{RESET}".center(105 + 8))
                break
            else:
                h -= 1
                if h > 0:
                    print()
                    print(" ".ljust(27), f"{MAGENTA}Username atau Password salah, silahkan coba lagi.{RESET}")
                else:
                    print()
                    print(' '.ljust(32), f"{MAGENTA}Kesempatan habis. Silahkan Daftar Akun.{RESET}")
                    self.buat_akun()
                    

login = Login()

class Menu2:
    def daftar_menu(self):
        while True: 
            indent = ' ' * 45
            print('='*105)
            print(' ' * 48 + f"{KUNING}Daftar Menu{RESET}")
            print(indent + "1. Penjelasan Program")
            print(indent + "2. Input Data")
            print(indent + "3. Program Peramalan")
            print(indent + "4. Selesai")
            jwb = input(indent + "Masukkan pilihan :")
            if jwb == '1':
                self.penjelasan()
            elif jwb == '2':
                print('='*105)
                d = int(input('Jumlah data yang akan dimasukkan: '))
                for i in range(d):
                    print()
                    tanggal = (input('Tanggal\t\t: '))
                    penjualan = int(input('Penjualan\t: '))
                    produksi = int(input('Produksi\t: '))
                    listdata.input_data(tanggal, penjualan, produksi)
                    if i == d-1:
                        listdata.tampil_data()
            elif jwb == '3':
                if not listdata.data:
                    print(f"{MAGENTA}Silahkan input data terlebih dahulu{RESET}".center(105 + 8))
                    self.daftar_menu()
                    break
                
                else:
                    print('-'*105)
                    print('\n')
                    print(f'{KUNING}Tabel Peramalan {RESET}: {MERAH}Metode Regresi Linier{RESET}'.center(90))
                    program.rumus()
               
            elif jwb == '4':
                print(' '*40, f'{MAGENTA}Program selesai.. GoodBye!{RESET}')
                break 

            else:
                print(f'{MERAH}Pilihan tidak valid. Silahkan coba lagi{RESET}'.center(105 + 8))

    def penjelasan(self):
        print()
        print("-" * 105)
        print(' ' * 35 + f'''{KUNING}Penerapan Metode Regresi Linier dalam
                    Aplikasi Sistem Peramalan Jumlah Bahan Baku untuk Produksi Tahu{RESET}''')
        print("-" * 105)
        print(' '.ljust(40) + f'{MERAH}     Gambaran Umum{RESET}')
        desc_text = '''       Program ini dapat meramalkan jumlah tahu yang harus diproduksi berdasarkan
            jumlah permintaan dan membuat kebijakan dalam menentukan jumlah bahan baku 
                            yang harus disediakan dalam periode tertentu.'''.center(125)
        print(' '.ljust(8) + desc_text)
        print('\n')
        print(' '.ljust(48) + f'{MERAH}Tujuan{RESET}')
        tujuan_text = '''           Membantu pemilik usaha tahu dalam menentukan jumlah produksi dan 
                                        persediaan bahan baku tahu.'''.center(125)
        print(' '.ljust(8) + tujuan_text)
        print('\n')
        print(' '.ljust(40) + f'{MERAH}Metode : Regresi Linier{RESET}')
        metode_text = '''       Metode analisis data yang memprediksi nilai data yang tidak diketahui dengan 
                            menggunakan nilai data terkait yang diketahui.'''.center(125)
        print(' '.ljust(8) + metode_text)
        print()
        print(' '.ljust(38) + f'{MERAH}Rumus Metode Regresi Linier{RESET}')
        print("a = Σy - bΣx".center(106))
        print("b = (n.Σxy - (Σx.Σy)) / (nΣx² - (Σx)²)".center(106))
        print("Y = a + bx".center(106))

menu2 = Menu2()

class listdata:
    def __init__(self):
        self.data = []
    
    def input_data(self, tanggal, penjualan, produksi):
        self.data.append([tanggal, penjualan, produksi])

    def tampil_data(self):
        print(f'\n{SIAN} Daftar Penjualan dan Produksi Tahu{RESET}')
        print()
        print('='*37)
        print(f'|{KUNING}  Tanggal   {RESET}|{KUNING} Penjualan {RESET}|{KUNING} Produksi |{RESET}')
        print('-'*37)
        for j in self.data:
            print(f'| {j[0]:^10} | {j[1]:^9} | {j[2]:^8} |')
        print('='*37)

listdata = listdata()

class program:
    def rumus(self):
        t = [i[0] for i in listdata.data]
        x = [i[1] for i in listdata.data]
        y = [i[2] for i in listdata.data]
        n = len(x)
        x2 = [i**2 for i in x]
        y2 = [i**2 for i in y]
        xy = [x[i]*y[i] for i in range(n)]
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x2 = sum(x2)
        sum_y2 = sum(y2)
        sum_xy = sum(xy)

        b = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
        a = (sum_y - b*sum_x) / n
        bulat_a = round(a,3)
        bulat_b = round(b,3)

        kolom_lebar = 10
    
        print('='*79)
        print('| {0:^{kolom_lebar}} | {1:^{kolom_lebar}} | {2:^{kolom_lebar}} | {3:^{kolom_lebar}} | {4:^{kolom_lebar}} | {5:^{kolom_lebar}} |'.format(
            f'{KUNING} Tanggal  {RESET}', f'{KUNING}     X    {RESET}', f'{KUNING}     Y    {RESET}', f'{KUNING}    X²    {RESET}', f'{KUNING}    Y²    {RESET}',f'{KUNING}    XY    {RESET}',kolom_lebar=kolom_lebar))
        print('-'*79)
        for i in range(n):
            print('| {0:^{kolom_lebar}} | {1:^{kolom_lebar}} | {2:^{kolom_lebar}} | {3:^{kolom_lebar}} | {4:^{kolom_lebar}} | {5:^{kolom_lebar}} |'.format(
                t[i].center(kolom_lebar), str(x[i]).center(kolom_lebar), str(y[i]).center(kolom_lebar), str(x2[i]).center(kolom_lebar), str(y2[i]).center(kolom_lebar), str(xy[i]).center(kolom_lebar), 
                kolom_lebar=kolom_lebar))
        print('='*79)
        print()

        print(f"{MAGENTA}Catatan{RESET} :")
        print(f"{SIAN}          X{RESET} = Jumlah Penjualan")
        print(f"{SIAN}          Y{RESET} = Jumlah Produksi")      

        print("\n")

        print("Dari tabel diatas, maka didapatkan data :")
        print("ΣX\t= ", sum_x)
        print("ΣY\t= ", sum_y)
        print("ΣX²\t= ", sum_x2)
        print("ΣY²\t= ", sum_y2)
        print("ΣXY\t= ", sum_xy)
        print("b\t= ", bulat_b)
        print("a\t= ", bulat_a)
        print()

        X = int(input("Jumlah permintaan: "))
        Y = bulat_a + bulat_b*X
        bulat = round(Y)
        print(f"{SIAN}Y\t= {Y} potong tahu, dibulatkan menjadi {bulat} potong tahu{RESET}")
        print()

        print(f'{MERAH}Bahan Baku{RESET}')
        kedelai = bulat / 7000 
        kedelai_bulat = round(kedelai,2)
        print(f'{SIAN}\n> KEDELAI{RESET}')
        print('1 kwintal kedelai  dapat menghasilkan 7000 potong tahu')
        print(f'Maka banyak kedelai yang dibutuhkan untuk membuat {bulat} potong tahu adalah {kedelai_bulat} kwintal ')
        
        air = kedelai*1500
        air_bulat = round(air,2)
        print(f'{SIAN}\n> AIR{RESET}')
        print('1 kwintal kedelai membutuhkan 1500 liter air')
        print(f'Maka banyak air yang dibutuhkan untuk membuat {bulat} potong tahu adalah {air_bulat} liter ')
        
        gas = kedelai*4
        gas_bulat = math.ceil(gas)
        print(f'\n{SIAN}> TABUNG GAS{RESET}')
        print('1 kwintal kedelai membutuhkan 4 tabung gas')
        print(f'Maka banyak gas yang dibutuhkan untuk membuat {bulat} potong tahu adalah {gas_bulat} tabung ')
    
program = program()

cover.coveran()
cover.intro()
login.menu_1()
menu2.daftar_menu()