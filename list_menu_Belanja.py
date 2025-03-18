print("================================================")
print("==========Selamat Datang Di Menu Berbelanja==========")
daftar_belanja = []

def tambah_item(item):
    daftar_belanja.append(item)
    print(f'"{item}" telah ditambahkan ke daftar belanja.')

def tampilkan_daftar():
    if daftar_belanja:
        print("\n Daftar Belanjaan yang sudah dimasukkan dalam keranjang adalah:")
        for i, item in enumerate(daftar_belanja, 1):
            print(f"{i}. {item}")
    else:
        print("\nDaftar Belanja Kosong, Silahkan masukkan belanjannya dulu.")

def hapus_item(index):
    if 0 <= index < len(daftar_belanja):
        item = daftar_belanja.pop(index)
        print(f'"{item}" telah dihapus dari daftar belanja.')
    else:
        print("Index tidak valid.")
while True:
    print("================================================")
    print("\n Silahkan Pilih Menu Apa Yang ingin anda lakukan : ")
    print("1. Tambah Item")
    print("2. Lihat Daftar Belanja")
    print("3. Hapus Item")
    print("4. Keluar")
    print("")
    print("================================================")
    pilihan = input("Pilih Menu yang ingin dilakukan dengan menulis Angka (1-4) : ")
    print("================================================")
    
    if pilihan == "1" :
        item = input("Masukkan item Belanjaan yang ingin kamu Beli : ")
        tambah_item(item)
        print()
    elif pilihan == "2" :
        tampilkan_daftar()
    elif pilihan == "3" :
        tampilkan_daftar()
        index = int(input("Masukkan nomor item yang ingin dihapus: ")) - 1
        hapus_item(index)
    elif pilihan == "4" :
        break
    else:
        print("!!!!!!!!!!!!!!!!Pilihan tidak valid, silakan coba lagi !!!!!!!!!!!!!!!!!!!!")
