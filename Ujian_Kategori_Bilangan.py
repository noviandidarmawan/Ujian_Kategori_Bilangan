def kategori(angka):
    jawaban =[]
    if angka > 0 or angka <= 0:
        jawaban.append('Bulat')
    if angka < 0:
        jawaban.append('Negatif')
    if angka >=0:
        jawaban.append('Cacah')
    if angka == 0: 
        jawaban.append('Nol')
    if angka > 0: 
        jawaban.append('Asli')
    if angka > 0 and angka % 2 != 0: 
        jawaban.append('Ganjil')
    if angka > 0 and angka % 2 == 0: 
        jawaban.append('Genap')

    if angka > 1:
        for i in range(2,angka):
            if (angka % i) == 0:
                jawaban.append('Komposit')
                break
        else:
            jawaban.append('Prima')
    return jawaban



inputan =  input('masukkan angka: ')
if inputan == inputan.lower() and inputan == inputan.upper() and inputan.find('.') != -1:
    print('angka tidak boleh ada koma')
elif inputan == inputan.lower() and inputan == inputan.upper():
    inputan = int(inputan)
    print(kategori(inputan))
else:
    print('inputan bukan angka')




