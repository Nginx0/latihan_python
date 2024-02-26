import datetime as dt
import os

template = {"nama":"nama",
            "nim":"00000000",
            "sks_lulus":0,
            "lahir":dt.datetime(1111,1,11)
        }

data_mahasiswa = {}

while True:
    os.system("clear")
    print(10*"=","PROGRAM DATA MAHASISWA",10*"=")

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = input("SKS Lulus: ")
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31): "))
    mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    print(mahasiswa)
