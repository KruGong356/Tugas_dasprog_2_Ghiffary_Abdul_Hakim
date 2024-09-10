def cek_servis(service_choice, miles):
    if service_choice == 1:
        if 1500 < miles < 3000:
            return "kedaraan harus diservis untuk first service."
        else:
            return "kendaraan tidak memerlukan first service"
    elif service_choice == 2:
        if 3001 < miles < 4500:
            return "kendaraan harus diservis untuk second service."
        else:
            return "kendaraan tidak memerlukan second service."
    else:
        return "pilihan layanan tidak valid."
    
print("(1) first free service")
print("(2) second free service")
service_choice = int(input("pilih jenis servis (1 atau 2) =>"))
miles = int(input("masukkan miles kendaraan anda =>"))

pesan_servis = cek_servis(service_choice, miles)

print(pesan_servis)