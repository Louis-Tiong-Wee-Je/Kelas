#Atur cara mnentukan penempatan kelas

nama = str(input("Masukkan nama anda:"))
markah = float(input("Masukkan marah anda:"))

#kategori kelas
if markah <= 40:
    print("Anda ditemptan di kelas Dedikasi")
elif markah <= 60:
    print("Anda ditemptan di kelas Cerdik")
elif markah <= 80:
     print("Anda ditemptan di kelas Bijak")
elif markah > 80:
     print("Anda ditemptan di kelas Amanah")
    
