nilai=int(input('Masukkan sebuah angka'))
def angka(nilai):
    if nilai%2 ==0:
        return'Genap'
    else:
        return"Ganjil"
hasil = angka(nilai)
print ('angka',nilai,'adalah',hasil)