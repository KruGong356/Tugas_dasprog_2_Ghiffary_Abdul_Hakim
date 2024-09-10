def hitung_bmi(berat_lb, tinggi_in):
    BMI = 703 * berat_lb / (tinggi_in ** 2)
    return round(BMI, 2)

def kategori_bmi(BMI):
    if BMI < 18.5:
        return "kurus"
    elif 18.5 <= BMI < 25:
        return "normal"
    elif 25 <= BMI < 30:
        return "kelebihan berat badan"
    elif 30 < BMI:
        return "obesitas"
    
berat_lb = float(input(" masukan bb anda dalam pound =>"))
tinggi_in = float(input("masukan tb anda dalam inci =>"))

BMI = hitung_bmi(berat_lb, tinggi_in)

kategori = kategori_bmi(BMI)

print(f"\nBMI anda: {BMI}")
print(f"kategori bb anda: {kategori}")