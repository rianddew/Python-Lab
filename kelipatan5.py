angka = int(input("Masukkan angka: "))
lima = angka % 5
if lima == 0:
    print(f"{angka * 10} adalah bilangan kelipatan 5 dan sudah dikali 10")
else:
    print(f"{angka} bukan bilangan kelipatan 5")