import pandas as pd
from tabulate import tabulate

class Transaction:
  def __init__(self):
      '''
      Fungsi inisialisasi dictionary
      cart : dictionary untuk menyimpan data transaksi
      valid_cart : penanda data yang diinput ke dictionary cart valid (boolean)
                 nilainya dapat berubah False setelah validitasnya dicek melalui fungsi
      '''

      self.cart = dict()
      self.valid_cart = True

  def add_item(self, nama, jumlah, harga):
      ''' 
      Fungsi untuk menambah item yang ingin dibeli
      nama   : nama item yang ingin dibeli (str)
      jumlah : jumlah item yang ingin dibeli (int)
      harga  : harga item yang dibeli (int)
      '''

      #cek tipe data 
      if type(jumlah)!=int:
        print('Jumlah item harus berupa angka!')
      elif type(harga)!=int:
        print('Harga item harus berupa angka')
      else:
        #data dimasukkan ke dalam dictionary
        cart_add = {nama: [jumlah, harga, jumlah*harga]}
        self.cart.update(cart_add)
        print(f'Item dalam pesanan: {nama} sebanyak {jumlah} dengan harga Rp {harga}.')    

  def update_item(self, nama, nama_baru):
        '''
        Fungsi untuk mengubah item yang sebelumnya dimasukkan ke dictionary
        nama      : nama item yang ingin diubah (str)
        nama_baru : nama item pengganti
        '''

        temp = self.cart[nama]
        self.cart.pop(nama)
        self.cart.update({nama_baru: temp})

        #menampilkan perubahan nama item 
        self.print_order()
        print(f'Nama item {nama} telah diubah menjadi {nama_baru}.')

  def update_item_qty(self, nama, jumlah_baru):
        '''
        Fungsi untuk mengubah jumlah item yang sebelumnya dimasukkan ke dictionary
        nama        : nama item yang ingin diubah jumlahnya (str)
        jumlah_baru : jumlah baru dari item (int)
        '''

        #cek tipe data
        if type (jumlah_baru)!=int:
          print('Jumlah harus berupa angka!')
        else:
          #data dimasukkan ke dalam dictionary
          self.cart[nama][0] = jumlah_baru
          self.cart[nama][2] = jumlah_baru*self.cart[nama][1]

          ##menampilkan perubahan jumlah item
          self.print_order()
          print(f'Jumlah item {nama} telah diubah menjadi {jumlah_baru}.')

  def update_item_price(self, nama, harga_baru):
        '''
        Fungsi untuk mengubah harga item yang sebelumnya dimasukkan ke dictionary
        nama       : nama item yang ingin diubah harganya (str)
        harga_baru : harga baru dari item (int)
        '''

        #cek tipe data
        if type (harga_baru)!=int:
          print('Harga harus berupa angka!')
        else:
          #data dimasukkan ke dalam dictionary
          self.cart[nama][1] = harga_baru
          self.cart[nama][2] = harga_baru*self.cart[nama][0]

          ##menampilkan perubahan harga
          self.print_order()
          print(f'Harga item {nama} telah diubah menjadi {harga_baru}.')

  def delete_item(self, nama):
      '''
      Fungsi untuk menghapus item, jumlah, dan harga dari dictionary
      nama : nama item yang ingin dihapus (str)
      '''

      try:
          self.cart.pop(nama)
          print(f'Item {nama} telah dihapus.')
          print('')
          self.print_order()

      except KeyError:
          print(f'{nama} tidak ada dalam keranjang.')

  def reset_transaction(self):
      '''
      Fungsi untuk menghapus seluruh pesanan dalam dictionary
      '''

      self.cart =self.cart.clear
      print('Seluruh item berhasil dihapus.')       

  def print_order(self):
      '''
      Fungsi untuk menampilkan seluruh pesanan dalam dictionary
      '''

      try:
          data_order = pd.DataFrame(self.cart).T
          headers = ['Nama Item', 'Jumlah Item', 'Harga per Item', 'Total Harga Item']
          print(tabulate(data_order, headers, tablefmt="github"))
      
      except:
          print('Pesanan belum ada.') 

  def check_order(self):
      '''
      Fungsi untuk melakukan cek validitas dan menampilkan pesanan dalam dictionary
      '''

      try:
          #menampilkan seluruh pesanan
          data_order = pd.DataFrame(self.cart).T
          headers = ['Nama Item', 'Jumlah Item', 'Harga per Item', 'Total Harga Item']
          print(tabulate(data_order, headers, tablefmt="github"))

          #cek jumlah atau harga bernilai lebih dari 0
          kolom = 0
          while kolom <2:
              for data in data_order[kolom]:
                  if data<=0:
                      self.valid_cart = False
              kolom+=1

          if self.valid_cart:
              print('Pesanan sudah benar.')
          else:
              print('Terdapat kesalahan pada input jumlah atau harga item. Mohon input kembali!')

      except ValueError:
          print('Pesanan belum ada.')

  def total_price(self):
        '''
        Fungsi untuk menampilkan seluruh pesanan dan total belanja.
        '''
        
        #memastikan validitas pesanan sebelum menjalankan method
        self.check_order()
        
        #menghitung diskon yang didapat
        if self.valid_cart:

            #menghitung total belanja
            total_belanja = 0
            for item in self.cart:
                total_belanja += self.cart[item][2] 

            #menghitung diskon
            if total_belanja >500_000:
                diskon = int(total_belanja*0.1)
                total_belanja = int(total_belanja-diskon)
                print(f"Anda mendapatkan diskon 10% sebesar Rp {diskon}. Total belanja Anda adalah Rp {total_belanja} (sudah termasuk diskon).")        

            elif total_belanja >300_000:
                diskon = int(total_belanja*0.08)
                total_belanja = int(total_belanja-diskon)
                print(f"Anda mendapatkan diskon 8% sebesar Rp {diskon}. Total belanja Anda adalah Rp {total_belanja} (sudah termasuk diskon).")

            elif total_belanja >200_000:
                diskon = int(total_belanja*0.05)
                total_belanja = int(total_belanja-diskon)
                print(f"Anda mendapatkan diskon 5% sebesar Rp {diskon}. Total belanja Anda adalah Rp {total_belanja} (sudah termasuk diskon).")

            else:
                print(f"Total belanja Anda adalah Rp {total_belanja}.")
        
        else:
            print("Total belanja belum bisa dihitung karena kesalahan input. Mohon periksa kembali.")

