#Program latihan CRUD
import os
database = ["--nama--"]

while True:
  os.system("clear")
  print(10*"=","DATABASE MAHASISWA",10*"=")
  print("1. Tambah Data")
  print("2. Update Data")
  print("3. Tampilkan Data")
  print("4. Hapus Data")
  print("5. Keluar Program\n")
  
  usr = input("Command >> ")
  
  if usr=="1":
    os.system("clear")
    print("=====Tambah Data Mahasiswa=====")
    add_data = input("masukan data: ")
    database.append(add_data)
  
  elif usr=="2":
    os.system("clear")
    print("=====Update Data=====")
    count = 0
    for data in database:
      print(f"{count}. {data}")
      count+=1
    
    print("\n\nTekan ENTER untuk batal")
    x = input("No data yang ingin diganti\n>> ")
    if x=="":
      continue
    else:
      y = input("Data baru >> ")
      database[int(x)] = y
    
  elif usr=="3":
    os.system("clear")
    print("=====Tampilkan Data Mahasiswa=====")
    count = 0
    for data in database:
      print(f"{count}. {data}")
      count+=1
    
    print(input("\n\n[Tekan ENTER]"))
    
  elif usr=="4":
    os.system("clear")
    print("=====Hapus Data Mahasiswa=====")
    count = 0
    for data in database:
      print(f"{count}. {data}")
      count+=1
    
    print("\n\nTekan ENTER untuk batal")
    x = input("Pilih data yang igin dihapus berdasarkan nama\n>> ")
    if x=="":
      continue
    else:
      database.remove(x)
      
  elif usr=="5":
    print("\nkeluar..")
    break
    
  else:
    print("\nCommand tidak valid!")
    print(input("[Tekan ENTER]"))
