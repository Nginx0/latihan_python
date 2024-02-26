#Fungsi kwargs
def math(*args,**kwargs):
    output = 0
    if kwargs["opsi"] == "tambah":
        for angka in args:
            output += angka

    elif kwargs["opsi"] == "kali":
        output = 1
        for angka in args:
            output *= angka

    else:
        print("Apa coba")

    return output

hasil = math(2,4,2,8,9,opsi="tambah")
print(f"Hasil jumlah = {hasil}")

hasil = math(2,8,5,9,3,opsi="kali")
print(f"Hasil kali = {hasil}")

print("\nProgram selesai")
