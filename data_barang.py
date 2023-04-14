#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root"
)

#preparing a cursor object
cursorObject = dataBase.cursor()

#creating database
cursorObject.execute("CREATE DATABASE db_sales_V3922003")


# In[3]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    database="db_sales_V3922003"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# create table Stok_Barang
courseRecord = """CREATE TABLE Stok_Barang (
                   Id_Barang VARCHAR(255) PRIMARY KEY,
                   Nama_Barang VARCHAR(255),
                   Harga_Barang INT,
                   Stok_Awal INT,
                   Barang_Masuk INT,
                   Barang_Keluar INT,
                   Stok_Akhir INT
                   )"""
cursorObject.execute(courseRecord)

# disconnecting from server
dataBase.close()


# In[1]:


import mysql.connector

if __name__ == '__main__':
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        database="db_sales_V3922003"
    )
    cursorObject = dataBase.cursor()

    def insert_data():
        # input data
        id_barang = input("Masukkan ID Barang: ")
        nama_barang = input("Masukkan Nama Barang: ")
        harga_barang = int(input("Masukkan Harga Barang: "))
        stok_awal = int(input("Masukkan Stok Awal: "))
        barang_masuk = int(input("Masukkan Barang Masuk: "))
        barang_keluar = int(input("Masukkan Barang Keluar: "))
        stok_akhir = stok_awal + barang_masuk - barang_keluar

        # query untuk insert data
        insert_query = f"INSERT INTO Stok_Barang (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir) VALUES ('{id_barang}', '{nama_barang}', {harga_barang}, {stok_awal}, {barang_masuk}, {barang_keluar}, {stok_akhir})"
        cursorObject.execute(insert_query)
        dataBase.commit()

        print(f"Data Barang dengan ID {id_barang} telah berhasil ditambahkan")
        
    def show_data():
        # query untuk select semua data dari tabel Stok_Barang
        select_query = "SELECT * FROM Stok_Barang"
        cursorObject.execute(select_query)

        # menampilkan semua data dari tabel Stok_Barang
        records = cursorObject.fetchall()
        for record in records:
            print(record)
     
    def update_data():
         # input ID Barang yang akan diupdate
        id_barang = input("Masukkan ID Barang yang akan diupdate: ")

        # query untuk select data berdasarkan ID Barang
        select_query = f"SELECT * FROM Stok_Barang WHERE Id_Barang = '{id_barang}'"
        cursorObject.execute(select_query)

        # menampilkan data yang akan diupdate
        record = cursorObject.fetchone()
        if record:
            print(f"Data Barang dengan ID {id_barang}:")
            print(record)
            # input data yang baru
            nama_barang = input("Masukkan Nama Barang baru (kosongkan jika tidak ingin mengubah): ")
            harga_barang = input("Masukkan Harga Barang baru (kosongkan jika tidak ingin mengubah): ")
            stok_awal = input("Masukkan Stok Awal baru (kosongkan jika tidak ingin mengubah): ")
            barang_masuk = input("Masukkan Barang Masuk baru (kosongkan jika tidak ingin mengubah): ")
            barang_keluar = input("Masukkan Barang Keluar baru (kosongkan jika tidak ingin mengubah): ")
            # query untuk update data
            update_query = f"UPDATE Stok_Barang SET "
            if nama_barang:
                update_query += f"Nama_Barang = '{nama_barang}', "
            if harga_barang:
                update_query += f"Harga_Barang = {harga_barang}, "
            if stok_awal:
                update_query += f"Stok_Awal = {stok_awal}, "
            if barang_masuk:
                update_query += f"Barang_Masuk = {barang_masuk}, "
            if barang_keluar:
                update_query += f"Barang_Keluar = {barang_keluar}, "
            # menghitung stok akhir
            stok_akhir = record[3] + int(barang_masuk or 0) - int(barang_keluar or 0)
            update_query += f"Stok_Akhir = {stok_akhir} WHERE Id_Barang = '{id_barang}'"
            cursorObject.execute(update_query)
            dataBase.commit()
            print(f"{cursorObject.rowcount} record(s) updated.")
            print(f"Data Barang dengan ID {id_barang} telah berhasil diupdate")
        else:
            print(f"Data Barang dengan ID {id_barang} tidak ditemukan")
            
    def delete_data():
        # input ID Barang yang akan dihapus
        id_barang = input("Masukkan ID Barang yang akan dihapus: ")

        # query untuk select data berdasarkan ID Barang
        select_query = f"SELECT * FROM Stok_Barang WHERE Id_Barang = '{id_barang}'"
        cursorObject.execute(select_query)

        # menampilkan data yang akan dihapus
        record = cursorObject.fetchone()
        if record:
            print(f"Data Barang dengan ID {id_barang}:")
            print(record)
            # konfirmasi penggunaan untuk menghapus data
            confirm = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
            if confirm.lower() == 'y':
                # query untuk delete data
                delete_query = f"DELETE FROM Stok_Barang WHERE Id_Barang = '{id_barang}'"
                cursorObject.execute(delete_query)
                dataBase.commit()
                print(f"Data Barang dengan ID {id_barang} telah berhasil dihapus")
        else:
            print(f"Data Barang dengan ID {id_barang} tidak ditemukan")
            
    def search_data():
        try:

            # membuat cursor
            cursorObject = dataBase.cursor()

            # input keyword untuk mencari data
            keyword = input("Masukkan keyword untuk mencari data: ")

            # query untuk select data yang mengandung keyword pada ID Barang atau Nama Barang
            search_query = f"SELECT * FROM Stok_Barang WHERE Id_Barang LIKE '%{keyword}%' OR Nama_Barang LIKE '%{keyword}%'"
            cursorObject.execute(search_query)

            # menampilkan data yang mengandung keyword
            records = cursorObject.fetchall()
            if records:
                for record in records:
                    print(record)
            else:
                print(f"Tidak ditemukan data Barang dengan keyword '{keyword}'")

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL", error)

        finally:
            # menutup koneksi database
            if (dataBase.is_connected()):
                cursorObject.close()
                print("MySQL connection closed")

    def main_menu():
        print("===== Aplikasi Database Python =====")
        print("1. Insert Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        print("0. Keluar")
        print("=====================================")
        choice = int(input("Masukkan pilihan anda: "))
        return choice

    while True:
        choice = main_menu()
        if choice == 1:
            insert_data ()
        elif choice == 2:
            show_data ()
        elif choice == 3:
            update_data ()
        elif choice == 4:
            delete_data ()
        elif choice == 5:
            search_data ()
        elif choice == 0:
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


# In[ ]:




