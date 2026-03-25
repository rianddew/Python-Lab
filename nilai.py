nilai = int(input("Masukkan nilai: "))
if nilai < 35:
    print ("Nilai anda tergolong E")
elif nilai < 50:
    print("Nilai anda tergolong D")
elif nilai < 60:
    print("Nilai anda tergolong C")
elif nilai < 65:
    print("Nilai anda tergolong BC")
elif nilai < 70:
    print("Nilai anda tergolong B")
elif nilai < 80:
    print("Nilai anda tergolong AB")
else:
    print("Nilai anda tergolong A")