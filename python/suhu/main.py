#program main
import os
import suhu

#Program Menghitung Suhu
while(True):
	os.system("clear")
	print("1.Mencari °C.")
	print("2.Mencari °F.")
	print("3.Mencari °R.")
	print("4.Mencari Kelvin.\n")
	
	usr_option = int(input("Pilih Rumus >> "))
	
	#Program mencari °C
	if usr_option == 1:
		print("1.Rumus °R menjadi °C.")
		print("2.Rumus °F menjadi °C.")
		print("3.Rumus Kelvin menjadi °C.\n")
		
		option = int(input("Pilih Rumus >> "))
		
		if option == 1:
			nilai = int(input("Suhu °R: "))
			hasil = suhu.R_to_C(nilai)
			print(f"Suhu sekarang: {hasil}°C.")
			break
		
		elif option == 2:
			nilai = int(input("Suhu °F: "))
			hasil = suhu.F_to_C(nilai)
			print(f"Suhu sekarang: {hasil}°C.")
			break
			
		elif option == 3:
			nilai = int(input("Suhu Kelvin: "))
			hasil = suhu.K_to_C(nilai)
			print(f"Suhu sekarang: {hasil}°C.")
			break
		
		else:
			print("Apa coba")
	
	#Program mencari °F
	elif usr_option == 2:
		print("1.Rumus °C menjadi °F.")
		print("2.Rumus °R menjadi °F.")
		print("3.Rumus Kelvin menjadi °F.\n")
	
		option = int(input("Pilih Rumus >> "))
		
		if option == 1:
			nilai = int(input("Suhu °C: "))
			hasil = suhu.C_to_F(nilai)
			print(f"Suhu sekarang: {hasil}°F.")
			break
			
		elif option == 2:
			nilai = int(input("Suhu °R: "))
			hasil = suhu.R_to_F(nilai)
			print(f"Suhu sekarang: {hasil}°F.")
			break
		
		elif option == 3:
			nilai = int(input("Suhu Kelvin: "))
			hasil = suhu.K_to_F(nilai)
			print(f"Suhu sekarang: {hasil}°F.")
			break
			
		else:
			print("apa coba")
	
	#Program mencari °R
	elif usr_option == 3:
		print("1.Rumus °F menjadi °R.")
		print("2.Rumus °C menjadi °R.")
		print("3.Rumus Kelvin menjadi °R.\n")
		
		option = int(input("Pilih rumus >> "))
		
		if option == 1:
			nilai = int(input("suhu °F: "))
			hasil = suhu.F_to_R(nilai)
			print(f"Suhu sekarang: {hasil}°R.")
			break
			
		elif option == 2:
			nilai = int(input("suhu °C: "))
			hasil = suhu.C_to_R(nilai)
			print(f"Suhu sekarang: {hasil}°R.")
			break
			
		elif option == 3:
			nilai = int(input("suhu Kelvin: "))
			hasil = suhu.F_to_R(nilai)
			print(f"Suhu sekarang: {hasil}°R.")
			break
			
		else:
			print("apa coba")
	
	#Program memcari Kelvin
	elif usr_option == 4:
		print("1.Rumus °F menjadi Kelvin.")
		print("2.Rumus °C menjadi Kelvin.")
		print("3.Rumus °R menjadi Kelvin.\n")
	
		option = int(input("Pilih rumus >> "))
	
		if option == 1:
			nilai = int(input("suhu °F: "))
			hasil = suhu.F_to_K(nilai)
			print(f"Suhu sekarang: {hasil} Kelvin.")
			break
	
		elif option == 2:
			nilai = int(input("suhu °C: "))
			hasil = suhu.C_to_K(nilai)
			print(f"Suhu sekarang: {hasil} Kelvin.")
			break
	
		elif option == 3:
			nilai = int(input("suhu °R: "))
			hasil = suhu.R_to_K(nilai)
			print(f"Suhu sekarang: {hasil} Kelvin.")
			break
	
		else:
			print("apa coba")
			