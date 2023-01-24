# SuperCashier - Self Service

Python Super Cashier adalah program sederhana self service yang menggunakan python agar pelanggan bisa memesan barang atau item secara mandiri.

## Description App
- Terdapat table untuk menampilkan item-item apa saja yang bisa dipesan
- Pelanggan bisa menambahkan item dan juga jumlah per item
- Jumlah Item dapat diupdate
- Pelanggan bisa menghapus per item atau hapus sekaligus
- Pelanggan yang telah memesan atau akan membayar diatas ketentuan akan mendapatkan diskon
 
## FlowChart
![Flowchart-Tugas_Pacmaan_Python drawio(2)](https://user-images.githubusercontent.com/16360023/214219826-22bfb018-91be-451b-8f24-faeb19b453b1.png)

## Function Code
 | Function | Deskripsi |
 | -------- | --------- |
 | ```def __init__``` | Pertama kali program dijalankan dan penginputan nama |
 | ```def table(self)``` | Untuk menampilkan data atau item yang ada |
 | ```def table_order(self)``` | Untuk menampilkan data atau item yang telah diinputkan oleh pelanggan  |
 | ```def opsi(self)``` | Menu awal terdiri dari checkitem, checkorder dan exit |
 | ```def check_item(self)``` | View item dari function table dan input item  |
 | ```def add_item(self,tambah_item)``` | Input Item dan kembali ke menu |
 | ```def update_item_qty(self,nama_item)``` | Input atau update jumlah item dan kembali ke menu  |
 | ```def delete_item(self,nama_item)``` | Delete item yang telah diinputkan |
 | ```def reset_transaction(self)``` | Delete semua item yang telah diinputkan |
 | ```def check_order(self)``` | Untuk mengecek sudah input item atau tidak. Dan opsi untuk delete item |

## Running Program
- Buat folder dan environment terlebih dahulu
    ```
    mkdir <folder>
    cd <folder>
    copy program ke dalam folder
    python3 -m venv env
    ```
- Aktifkan environment
    ```
    source ./env/bin/activate
    ```
- Install terlebih dahulu package yang diperlukan pada requirement.txt
    ```
    pip install -r requirement.txt
    ```
    > Package yang digunakan 
    
    | Package | README |
    | ------- | ------ |
    | itertools | https://docs.python.org/3/library/itertools.html#itertools.chain |
    | rich | https://rich.readthedocs.io/en/stable/tables.html |
    | collection | https://docs.python.org/3/library/collections.html#collections.defaultdict |
    
- Jalankan app di terminal 
    ```
    python app.py
    ```
## Test Case
- _Menjalankan program dan input nama_

![Screenshot from 2023-01-23 15-21-22](https://user-images.githubusercontent.com/16360023/213993771-6ba694e6-6cfd-4258-94c1-c8378264d6c9.png)

- _Pilih Item (Check Item)_

![image](https://user-images.githubusercontent.com/16360023/213999553-6a957890-7a54-4cdb-85fc-57f8485c6e59.png)

- _Table Item_

![image](https://user-images.githubusercontent.com/16360023/213994475-0df10c14-1830-4385-8f83-aed26bbc6d5e.png)

- _Informasi Diskon_

![image](https://user-images.githubusercontent.com/16360023/214215382-1ad3802c-bd4e-4e6f-8f8c-aba5f154f848.png)

- _Tambah Item_

![image](https://user-images.githubusercontent.com/16360023/214215647-5727e88f-1245-438f-801c-acfa842f0d92.png)

- _Jika salah memasukkan nama item_

![image](https://user-images.githubusercontent.com/16360023/213994785-f78fa329-6d18-44c4-b3de-c11d2eb4fe27.png)

- _Tambah dan update item_

![image](https://user-images.githubusercontent.com/16360023/213995141-9302f7fc-c80f-4219-884e-eba38793daee.png)

- _Kembali ke menu awal_

![image](https://user-images.githubusercontent.com/16360023/213995211-5083de98-cf20-4424-889e-ac8dadaf3b1b.png)

- _Pilih Check order untuk melihat item yang sudah dipesan atau ingin menghapus item_

![image](https://user-images.githubusercontent.com/16360023/213995244-1c125d1f-4b0d-47c0-a3d9-4a683f1d4cff.png)

- _Hapus item_

![image](https://user-images.githubusercontent.com/16360023/213995282-c0e8f6d5-0c83-4102-91bb-387e5de7888a.png)

- _Check Out pemesanan_

![image](https://user-images.githubusercontent.com/16360023/213995313-5d72a04c-9cce-4e87-9d75-21e3486682be.png)


## Perbaikan kedepan
- ```Perbaikan clean code```
- ```Implementasi metode MVC```
