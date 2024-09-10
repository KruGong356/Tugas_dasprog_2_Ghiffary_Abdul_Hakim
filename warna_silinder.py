warna = input("masukan huruf pertama  dari warna silinder (Y,O,B,G) =>").lower()

if warna =='o':
    isi = "Amonia"
elif warna == 'y':
    isi = "Hidrogen"
elif warna == 'b':
    isi = "Karbon Monoksida"
elif warna == 'g':
    isi = "oksigen"
else:
    isi = "Isi tidak diketahui ( contents unknown)"
    
print(f"isi silinder => {isi}")