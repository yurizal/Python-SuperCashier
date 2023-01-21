from rich.console import Console
from rich.table import Table
# from termcolor import colored #python -m pip install termcolor
from itertools import chain
from collections import defaultdict
"""
Class color untuk membuat warna pada teks
"""
class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

"""
class Transaksi memiliki beberapa function/method dan juga variable yang menampung :
- data_item = menyimpan data item/barang yang tersedia di AndyMart
- data_header_item = digunakan untuk header kolom
- data_order = dictionary kosong untuk menampung data yang akan dijoin kan dengan data_item dan juga untuk perhitungan total dan diskon
- data_header_order = digunakan untuk header kolom order
"""
class Transaksi():
    data_item = {
        "CITATO":10000,
        "SABUN MANDI":15000,
        "PASTA GIGI":8000,
        "ROTI":3000
    }
    data_header_item ={"No":"cyan",
                  "Item":"magenta",
                  "Harga":"green"}
    data_order = {}
    data_header_order ={"No":"cyan",
                  "Item":"magenta",
                  "Harga":"green",
                  "Jumlah":"green",
                  "Total":"green"}

    """
    inisialisasi pertama kali saat dibuat sebuah objek, yang mana untuk input data nama
    """
    def __init__(self):
        print(f"Selamat datang di AndyMart")
        self.nama  = input("Masukkan Nama Anda : ")

    """
    def table function/method untuk menampilkan table dari data Transaksi.data_item
    """
    def table(self):
        print("-"*30,"\n")
        print(f"Berikut item yang tersedia\n")
        self.table_data_item = Table(title="List Item Andy Mart")

        self.data_item = Transaksi.data_item
        self.data_header_item = Transaksi.data_header_item

        for index,key in enumerate(self.data_header_item.items()):
            self.table_data_item.add_column(f"{key[0]}", style=f"{key[1]}")

        for index,key in enumerate(self.data_item.items()):
            self.table_data_item.add_row(f"{index}",f"{key[0]}",f"Rp {key[1]}")

        console = Console()
        console.print(self.table_data_item)

    """
    def table_order function/method untuk menampilkan table dari data Transaksi.data_order
    """
    def table_order(self):
        self.table_data_order = Table(title="Item yang anda order sebagai berikut")
        self.data_item = Transaksi.data_item
        self.data_order = Transaksi.data_order
        self.data_header_order = Transaksi.data_header_order
        list_diskon =[]
        dict3 = defaultdict(list)
        for k, v in chain(self.data_item.items(), self.data_order.items()):
            dict3[k].append(v)

        # print(dict3['CITATO'][2])
        for index,key in enumerate(self.data_header_order.items()):
            if index == 0 :
                continue
            else:
                self.table_data_order.add_column(f"{key[0]}", style=f"{key[1]}")

        for key,value in enumerate(dict3.items()):
            try:
                harga = int(value[1][0])
                jumlah = int(value[1][1])
                total = harga * jumlah
                diskon = [total-(total*0.1),'10%'] if total > 500000 else [total-(total*0.08),'8%'] if total > 300000 else [total-(total*0.05),'5%'] if total > 200000 else [total,'0']
                self.table_data_order.add_row(f"{value[0]}",f"Rp {value[1][0]}",f"{value[1][1]}",f"Rp {int(diskon[0])}")
                print(key)
                if diskon[1] != '0':
                    list_diskon.append(f"item {value[0]} mendapatkan diskon {diskon[1]} dari Rp {total} menjadi Rp {int(diskon[0])}")

            except:
                continue

        console1 = Console()
        console1.print(self.table_data_order)
        for i in list_diskon:
            print(i)

    """
    def add_item function/method yang digunakan untuk menambah item dimana saat penambahan item harus sesuai dengan table/data yang disedikan oleh AndyMart
    Jika yang diinputkan tidak sama dengan data table, maka keluar alert atau tidak bisa diinputkan. Jika sesuai maka akan lanjut untuk input jumlah item
    Dan jika mengetikkan BACK maka akan kembali ke menu awal
    """
    def add_item(self,tambahItem):
        if tambahItem in Transaksi.data_item:
            self.update_item_qty(tambahItem)

        elif tambahItem == "BACK":
            return self.opsi()
        else:
            return f"{Color.DARKCYAN}Tidak ada item yang anda masukkan, silahkan cek item dan pesan kembali{Color.END}"
        return f"Pesanan Anda {Transaksi.data_order}\n"


    """
    function/method ini akan dijalankan jika function add_item memenuhi syarat yakni inputan harus sesuai dengan data table
    yang mana function ini akan menyimpan nama dan jumlah item dan disimpan di variable data_order.
    Jika menginputkan nama item yang sama dan jumlah item yang sama/berbeda maka akan update data di data_order.
    Jadi jika ingin merubah jumlah item, langsung diketikan saja jumlah yang diinginkan, maka akan terupdate
    """
    def update_item_qty(self,nama_item):
        while True:
            try:
                jumlahItem = input(f"{Color.BOLD}Pilih jumlah Item : {Color.END}").upper()
                if jumlahItem == "BACK":
                    return self.opsi()
                else:
                    jumlahItem = int(jumlahItem)
                    Transaksi.data_order[nama_item]=jumlahItem
                print(f"\n{Color.CYAN}Pesanan telah diupdate, silahkan menambahkan item lagi{Color.END}")
                break
            except:
                print(f'{Color.RED}Masukkan Decimal/Jumlah Item{Color.END}')

    """
    delete_item function untuk menghapus data per item. Jadi tinggal mengetikkan nama item yang ingin dihapus
    maka akan terhapus dan terupdate di data table order
    """
    def delete_item(self,nama_item):
        self.nama_item = nama_item
        pesan = input("Yakin mau hapus data (Yes=y, No=press any key) ?").upper()
        if pesan == "Y":
            for k,v in list(Transaksi.data_order.items()):
                if k == self.nama_item:
                    print(f"{Color.YELLOW}Item sudah dihapus{Color.END}")
                    del Transaksi.data_order[k]
                    return self.check_order()
        else:
            return self.check_order()
        print(f"Item {self.nama_item} tidak ada atau sudah dihapus, silahkan diperiksa kembali")

    """
    reset_transaction untuk menghapus semua item sekaligus.
    """
    def reset_transaction(self):
        rst = input("Anda yakin mau menghapus semua item yang sudah diinputkan (Yes=y, No=press any key)").upper()
        if rst == "Y":
            print("Semua Item sudah dihapus semua.")
            Transaksi.data_order.clear()
            return self.opsi()

    """
    function untuk mengecek item yang telah dipesan oleh user. Dimana jika user belum memesan item/barang maka akan keluar alert dan kembali lagi ke menu sebelumnya.
    Di function ini terdapat 3 opsi yang ditampilkan yakni :
    1. check out : opsi ini akan memberikan pesan ke user apakah pesanan mau dibayar atau belum. kalau dibayar program akan keluar kalau belum akan kembali lagi
    2. remove : opsi ini akan memberikan 2 pilihan ke user dimana user bisa memilih untuk menghapus per item atau menghapus semua item/reset transaction
    3. back : opsi untuk kembali ke menu awal, jika ingin keluar dari program atau memesan item
    """
    def check_order(self):
        print("\n")

        if len(Transaksi.data_order) == 0:
            print(f"{Color.UNDERLINE}{Color.BOLD}Anda belum menambahkan / mengorder item, silahkan order dengan mengetik angka 1, Terima kasih{Color.END}")
        else:

            self.table_order()
            while True:
                print("\n")
                print("Silahkan pilih opsi (1/2/3) : ")
                print(f"{Color.BLUE}1. Check Out{Color.END} (FINISH)\n{Color.YELLOW}2. Remove{Color.END} (DELETE/RESET Item)\n{Color.RED}3. BACK{Color.END} (Menu Utama)\n ")
                pilih = input("Silahkan pilih opsi anda : ")

                if pilih == "1":
                    selesai = input("Anda yakin ingin menyelesaikan pembayaran (Yes=Y, No=press any key)? ").upper()
                    # while True:
                    if selesai == "Y":
                        print(f"Silahkan membayar item anda\nTerima kasih sudah berkunjung ke AndyMart saudara/i {self.nama.upper()} \n")
                        quit()
                    else:
                        continue
                elif pilih == "2":
                    print(f"\n{Color.RED}Silahkan pilih opsi (1/2/press any key) :{Color.END}\n1. Delete (Hapus item)\n2. Reset (Hapus semua item)\n3. Cancel")
                    rmv = input("Silahkan pilih opsi anda : ").upper()
                    if len(Transaksi.data_order) == 0:
                        self.opsi()
                    elif rmv == "1":
                        print(Transaksi.data_order)
                        a = input("Silahkan ketikan item yang akan dihapus : ").upper()
                        self.delete_item(a)
                    elif rmv == "2":
                        self.reset_transaction()
                    else:
                        continue
                elif pilih == "3":
                    return self.opsi()
                else:
                    print(f"{Color.RED}Anda salah memilih opsi {Color.END}")

    """
    function ini digunakan untuk mengecek atau menampilkan table item yang tersedia di AndyMart
    dimana user bisa langsung menginputkan item dan jumlah item, Jika nama item sesuai dengan yang ada di table
    """
    def check_item(self):
        self.table()
        print(f"- Untuk memilih dan menambah item silahkan ketik nama item\n- Untuk update jumlah item silahkan ketik ulang nama item\n- Untuk kembali ke menu silahkan ketik {Color.RED}BACK{Color.END} sebelum memilih item")
        while True:
            tambahItem = input(f"{Color.BOLD}Pilih item : {Color.END}").upper()
            print(self.add_item(tambahItem))

    """
    function opsi adalah menu yang ditampilkan setelah menginputkan nama, Dimana terdapat 3 opsi yakni :
    1. check item berfungsi untuk menampilkan item dan memanggil function check_item() untuk melakukan proses ADD/UPDATE item
    2. check order berfungsi untuk menampilkan item yang sudah diinputkan oleh user dan juga ada fungsi untuk remove item
    3. Exit untuk keluar dari program
    """
    def opsi(self):
        while True:
            print("\n")
            print(f"{Color.GREEN}1. Check Item{Color.END} (ADD/UPDATE Item)\n{Color.BLUE}2. Check Order{Color.END} (VIEW/REMOVE ITEM)\n{Color.RED}3. Exit{Color.END}")

            pilihan = input("Silahkan pilih Opsi anda (1/2/3): ").upper()
            if pilihan == "1":
                self.check_item()
                # A == False
            elif pilihan == "2":
                self.check_order()
            elif pilihan == "3":
                print(f"Terima Kasih Telah datang {self.nama.upper()}, Selamat Datang Kembali")
                quit()
            else:
                print("Tidak ada opsi tersebut, silahkan pilih kembali!!!")
