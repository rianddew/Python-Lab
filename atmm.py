def sistem_atm():
    # Konfigurasi Awal
    saldo = 1000000
    pin_benar = "2810"
    
    print("Selamat Datang di ATM Bersama")
    
    # Fitur PIN Login
    while True:
        input_pin = input("Masukkan PIN Anda: ")
        if input_pin == pin_benar:
            print("\nLogin Berhasil!")
            break
        else:
            print("PIN Salah! Silakan coba lagi.")
    
    # Menampilkan Menu HANYA SEKALI di awal
    print("\n=== MENU ATM BERSAMA ===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")
    print("------------------------")
    
    # Loop Transaksi
    while True:
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            print(f"Saldo Anda saat ini: Rp. {saldo:,}")

        elif pilihan == '2':
            nominal = int(input("Masukkan nominal tarik tunai (Kelipatan 50.000): "))
            if nominal % 50000 != 0:
                print("Gagal: Harus kelipatan Rp. 50.000")
            elif nominal > saldo:
                print("Gagal: Saldo tidak mencukupi")
            else:
                saldo -= nominal
                print(f"Berhasil! Sisa saldo: Rp. {saldo:,}")

        elif pilihan == '3':
            nominal = int(input("Masukkan nominal setor tunai (Kelipatan 50.000): "))
            if nominal % 50000 != 0:
                print("Gagal: Harus kelipatan Rp. 50.000")
            else:
                saldo += nominal
                print(f"Berhasil! Total saldo: Rp. {saldo:,}")

        elif pilihan == '4':
            print("Terima kasih telah menggunakan ATM Bersama")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")

# Menjalankan Program
sistem_atm()