# menghitung diskon dan pajak
def hitungan_total(harga_total, student):
    D = 0.20
    P = 0.05
    
    if student:
        diskon = harga_total * D
    else:
        diskon = 0.0
        
    diskon_total = harga_total - diskon

    pajak_penjualan = diskon_total * P
        
    total_dgn_pajak = diskon_total + pajak_penjualan

    return diskon , diskon_total, pajak_penjualan, total_dgn_pajak


harga_total = float(input("masukkan total pembelian anda => $"))
kalo_student = input("apakah ente mahasiswa? (ya/tidak):").lower() == 'ya'

diskon, diskon_total, pajak_penjualan, total_dgn_pajak = hitungan_total(harga_total, kalo_student)

if kalo_student:
    print(f"\nTotal pembelian: ${harga_total:.2f}")
    print(f"dDiskon mahasiswa (20%): ${diskon:.2f}")
    print(f"Total setelah diskon: ${diskon_total}")
    
else:
    print(f"\nTotal pembelian: ${harga_total:.2f}")
    
print(f"Pajak penjualan (5%): ${pajak_penjualan:.2f}")
print(f"Total akhir: ${total_dgn_pajak:.2f}")