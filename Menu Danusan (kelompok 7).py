# Program Menu Danusan

# Daftar produk danusan
menu_danusan = {
    1: {"nama": "Roti Bakar", "harga": 8000},
    2: {"nama": "Es Teh Manis", "harga": 5000},
    3: {"nama": "Mie Goreng", "harga": 10000},
    4: {"nama": "Kopi Susu", "harga": 7000},
    5: {"nama": "Cimol Pedas", "harga": 6000}
}

keranjang = []

def tampilkan_menu():
    print("\n=== MENU DANUSAN ===")
    for key, item in menu_danusan.items():
        print(f"{key}. {item['nama']} - Rp{item['harga']}")
    print("====================")

def pilih_menu():
    tampilkan_menu()
    try:
        pilihan = int(input("Kamu mau beli apa nih? Masukin nomor menu yang mau kamu beli yaa: "))
        if pilihan in menu_danusan:
            jumlah = int(input(f"Masukkan jumlah {menu_danusan[pilihan]['nama']}: "))
            item = menu_danusan[pilihan]
            total_harga = item["harga"] * jumlah
            keranjang.append({"nama": item["nama"], "jumlah": jumlah, "total": total_harga})
            print(f"{jumlah} {item['nama']} berhasil ditambahkan ke keranjang :D")
        else:
            print("Yaaaahhhh menu ini belum ada :()")
    except ValueError:
        print("Pilihanmu ngga valid nih. Masukin angka aja yaa ;)")

def lihat_keranjang():
    if not keranjang:
        print("Keranjang belanjamu masih kosong nih.")
        return

    print("\n=== KERANJANG BELANJA ===")
    for item in keranjang:
        print(f"{item['jumlah']}x {item['nama']} - Rp{item['total']}")
    print("==========================")

def beli_barang():
    if not keranjang:
        print("Keranjang belanjamu masih kosong nih.")
        return
    
    print("\n=== KERANJANG BELANJA ===")
    total_belanja = 0
    for item in keranjang:
        print(f"{item['jumlah']}x {item['nama']} - Rp{item['total']}")
        total_belanja += item["total"]
    print(f"Total Belanja: Rp{total_belanja}")
    print("==========================")

def payment():
    if not keranjang:
        print("Belum ada payment yang bisa dilakukan.")
        return
    else:
        print("\n=== PAYMENT DANUSAN ===")
        print("1. Transfer")
        print("2. Cash")
        print("=====================")

        pilihan = input("Kamu mau payment lewat apa? Pilih salah satu yaa: ")
        if pilihan == "1":
            transfer()
        elif pilihan == "2":
            cash()

def bni():
    print("1845713537 (a.n. Gendis Asti Yulianti)")

def bri():
    print("1298 0100 8680 501 (a.n. Gendis Asti Yulianti)")

def dana():
    print("085747341015 (a.n. Fatima Harjanto)")

def gopay():
    print("0895421976197 (a.n. Gendis)")

def shopeepay():
    print("0895421976197 (a.n. gendhisas_)")

def transfer():
    if not keranjang:
        print("Tidak ada payment yang bisa dilakukan")
        return
    else:
        print("\n=== TRANSFER ===")
        print("1. BNI")
        print("2. BRI")
        print("3. Dana")
        print("4. Gopay")
        print("5. Shopeepay")
        print("=================")

        pilihan = input("Pilih salah satu yaaww: ")
        if pilihan == "1":
            bni()
        elif pilihan == "2":
            bri()
        elif pilihan == "3":
            dana()
        elif pilihan == "4":
            gopay()
        elif pilihan == "5":
            shopeepay()
        else:
            print("Yaaah metode transfer lainnya belum bisa :(")

def cash():
    print("Pembayaran cash bisa dilakukan saat barang mau diambil yaa")
    print("Kamu bisa hubungi nomer di bawah ini buat janjian")
    print("083162389072 (Daffa)")
    print("085747341015 (Fatima)")
    print("0895421976197 (Gendis)")

def main():
    while True:
        print("\n===== PROGRAM DANUSAN =====")
        print("1. Lihat Menu")
        print("2. Pilih Menu")
        print("3. Lihat Keranjang")
        print("4. Beli Barang")
        print("5. Payment")
        print("6. Keluar")
        print("===========================")

        pilihan = input("Kamu mau ngapain? Pilih (1-5): ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            pilih_menu()
        elif pilihan == "3":
            lihat_keranjang()
        elif pilihan == "4":
            beli_barang()
        elif pilihan == "5":
            payment()
        elif pilihan == "6":
            print("Terima kasih telah berbelanja <3")
            break
        else:
            print("Pilihan kamu ngga ada. Coba lagi yaa :)")

# Jalankan program
main()
