#program dadu
import random

while True:

    print("1. Lempar dadu")
    print("2. Keluar\n")

    user = int(input("Mau pilih mana bang: "))

    if user==1:
        nomor = random.randint(1,6)
        print(f"\n[ {nomor} ]\n")

    elif user==2:
        print("Memutuskan sambungan...")
        break

    else:
        break

