# Proyek Python: Super Kasir

## Latar Belakang
Bisnis ritel mengalami persaingan yang ketat. Kepuasan pelanggan menjadi faktor penting untuk memenangkan persaingan. Pemilik sebuah supermarket menghadapi masalah bahwa antrean di kasir seringkali membuat pelanggan harus menunggu lama, karena pelayanan di kasir terbatas, sementara kedatangan pelanggan terus meningkat. Oleh karena itu, pemilik berinisiatif untuk melakukan perbaikan proses bisnis pada bagian kasir. Pelayanan di kasir akan ditingkatkan melalui penggunaan sebuah sistem kasir yang dapat mencatat dan menghitung transaksi pelanggan secara cepat dan tepat.
Super Kasir merupakan suatu sistem kasir self-service yang dirancang agar pelanggan bisa memasukkan item barang yang ingin dibeli dan jumlah barang yang diinginkan, serta harga barang tersebut. Sistem juga akan membantu perhitungan jumlah transaksi pelanggan, termasuk diskon yang diperoleh, apabila jumlah transaksinya mencapai nominal tertentu.

## Tujuan
Membuat sistem kasir self-service (Super Kasir) dengan spesifikasi fitur yang  membantu pelanggan dalam berbelanja sebagai berikut:
1. Membuat proses untuk `menambah item`
2. Membuat proses untuk `mengubah nama item`
3. Membuat proses untuk `mengubah jumlah item`
4. Membuat proses untuk `mengubah harga item`
5. Membuat proses untuk `menghapus item`
6. Membuat proses untuk `reset transaksi`
7. Membuat proses untuk `cek validitas pesanan`
8. Membuat proses untuk `menghitung dan menampilkan total belanja`
9. Membuat proses untuk `menghitung dan menampilkan diskon` dengan ketentuan:
    - Jika total belanja lebih dari Rp500.000, maka memperoleh diskon 10%
    - Jika total belanja lebih dari Rp300.000, maka memperoleh diskon 8%
    - Jika total belanja lebih dari Rp200.000, maka memperoleh diskon 5%

## Flowchart
![flowchart super kasir](https://user-images.githubusercontent.com/119470539/218087056-1e418df7-8e2e-43d5-8923-c2175a264706.png)

## Penjelasan Fungsi
Fungsi-fungsi untuk menjalankan proses dalam sistem super kasir berada dalam class Transaction pada file script.py antara lain:
1. `__init__`
Fungsi inisialisasi dictionary.
cart       : dictionary untuk menyimpan data transaksi 
valid_cart : penanda data yang diinput ke dictionary cart valid (boolean)
             nilainya dapat berubah False setelah validitasnya dicek melalui fungsi
2. `add_item(nama, jumlah, harga)`
Fungsi untuk menambah item yang ingin dibeli.
nama       : nama item yang ingin dibeli (str)
jumlah     : jumlah item yang ingin dibeli (int)
harga      : harga item yang dibeli (int)

3. `update_item(nama, nama_baru)`
Fungsi untuk mengubah item yang sebelumnya dimasukkan ke dictionary.
nama       : nama item yang ingin diubah (str)
nama_baru  : nama item pengganti

4. `update_item_qty(nama, jumlah_baru)`
Fungsi untuk mengubah jumlah item yang sebelumnya dimasukkan ke dictionary.
nama        : nama item yang ingin diubah jumlahnya (str)
jumlah_baru : jumlah baru dari item (int)

5. `update_item_price(nama, harga_baru)`
Fungsi untuk mengubah harga item yang sebelumnya dimasukkan ke dictionary.
nama       : nama item yang ingin diubah harganya (str)
harga_baru : harga baru dari item (int)

6. `delete_item(nama)`
Fungsi untuk menghapus item, jumlah, dan harga dari dictionary.
nama : nama item yang ingin dihapus (str)

7. `reset_transaction()`
Fungsi untuk menghapus seluruh pesanan dalam dictionary.

8. `print_order()`
Fungsi untuk menampilkan seluruh pesanan dalam dictionary.

9. `check_order()`
Fungsi untuk melakukan cek validitas dan menampilkan pesanan dalam dictionary.

10. `total_price()`
Fungsi untuk menampilkan seluruh pesanan dan total belanja.

## ***Test Case*** 
### ***Test Case*** I : Menambahkan Item
Pelanggan ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan adalah:
- Nama Item: Es Krim, Jumlah: 1, Harga: 7_000
- Nama Item: Coklat, Jumlah: 2, Harga: 30_000

Output:
![Output 1](https://user-images.githubusercontent.com/119470539/218087364-4b14a30e-83c7-402e-bc64-67ce0274f2f4.png)

### ***Test Case*** II : Menghapus Item
Pelanggan tidak jadi beli salah satu item dari pesanan yang sudah ditambahkan, maka pelanggan menggunakan method `delete item()` untuk menghapus item. Item yang ingin dihapus oleh Pelanggan adalah **Coklat**.

Output:
![Output 2](https://user-images.githubusercontent.com/119470539/218087556-defe0de7-3567-4ffc-afeb-c44c0bc69c13.png)

### ***Test Case*** III : Mereset Seluruh Item
Pelanggan merasa salah dalam memasukkan item yang ingin dipesan, tetapi tidak ingin menghapus item satu per satu, maka Pelanggan dapat menghapus seluruh item yang sudah ditambahkan dengan menggunakan method `reset_transaction()`.

Output:
![Output 3](https://user-images.githubusercontent.com/119470539/218087679-930fd179-6790-438e-ae8e-9192b90250c5.png) 

### ***Test Case*** IV : Menghitung Total Belanja
Ketika Pelanggan selesai belanja, maka item yang ingin dibeli akan ditampilkan, kemudian total belanja yang harus dibayar oleh Pelanggan dihitung dan ditampilkan menggunakan method `total_price()`. 

Output:
![Output 4](https://user-images.githubusercontent.com/119470539/218087795-acd0951f-0c8d-4c60-a421-c04bd3f25f8a.png)

### ***Test Case*** V : Mengubah Item
Pelanggan telah menambahkan item yaitu:
nama : Kopi Susu     jumlah : 10 harga: 5_000
nama : Biskuit       jumlah : 2  harga: 15_000
nama : Kacang Goreng jumlah : 5  harga: 7_000
Namun Pelanggan ingin mengubah **Kacang Goreng** yang sudah ditambahkan menjadi **Kacang Goreng Bawang** menggunakan metode `update_item_name()`.

Output:
![Ouput 5](https://user-images.githubusercontent.com/119470539/218087906-59c1cf81-0005-4799-9a78-211b0ba6c81e.png)

### ***Test case*** VI : Mengubah Jumlah Item
Pelanggan ingin mengubah jumlah **Biskuit** yang sebelumnya 2 buah menjadi 10 buah dengan metode `update_item_qty()`.

Output:
![Ouput 6](https://user-images.githubusercontent.com/119470539/218088121-7d150bc8-ce62-4d38-87bd-33afab35ab83.png)

### ***Test Case*** VII : Mengubah Harga Item
Pelanggan ingin mengubah harga per item dari **Kopi Susu** yang sebelumnya 5000 menjadi 7000 per item-nya dengan metode `update_item_price()`.

Output:
![Ouput 7](https://user-images.githubusercontent.com/119470539/218088235-467da31d-9018-4df0-aaf7-5ad1076eb6a0.png)

### ***Test Case*** VIII : Cek Validitas Pesanan
Pelanggan ingin mengecek validitas (kebenaran) pesanan yang diinput dengan mengggunakan method `check_order`. Proses ini dilakukan sebelum total belanja dan diskon dihitung agar pesanan valid.

Output:
![Output 8](https://user-images.githubusercontent.com/119470539/218088311-0243f2d9-b16a-482e-a06d-b8d3c62ee5ff.png)

### ***Test Case *** IX : Menghitung Total Belanja dan Diskon
Pelanggan yang selesai berbelanja kemudian menghitung total belanja dan diskon yang akan diperoleh sesuai dengan ketentuan dengan menggunakan method `total_price`.

Output:
![Output 9](https://user-images.githubusercontent.com/119470539/218088411-6c335af3-d59e-4424-b35a-c093baea6b78.png)

## Kesimpulan
Super Kasir dengan fitur-fiturnya dapat membantu Pemilik Supermarket untuk meningkatkan efektivitas proses bisnis pada bagian kasir, sehingga pelanggan dapat berbelanja dengan lebih cepat.