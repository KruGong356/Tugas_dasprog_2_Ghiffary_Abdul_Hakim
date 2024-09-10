def leap(tahun):
    if (tahun % 4 ==0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return 1
    else:
        return 0
    
def hitung_nomor_hari(hari, bulan, tahun):
    hari_per_bulan_biasa = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    hari_per_bulan_kabisat = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap(tahun):
        hari_per_bulan = hari_per_bulan_kabisat
    else:
        hari_per_bulan = hari_per_bulan_biasa
        
        nomor_hari = sum(hari_per_bulan[:bulan - 1]) + hari
        return nomor_hari
    
hari = int(input("masukkan hari =>"))
bulan = int(input("masukkan bulan =>"))
tahun = int(input("masukkan tahun =>"))

nomor_hari = hitung_nomor_hari(hari, bulan, tahun)

print(f"nomor hari untuk tanggal {hari}/{bulan}/{tahun} adalah: {nomor_hari}")