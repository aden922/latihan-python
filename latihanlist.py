print ("DATA BUKU")


listData = []
while True:
    judul = input(f"masukan nama judul\t : ")
    penulis =  input(f"masukan nama penulis\t : ")
    ListBuku = [judul , penulis]
    listData.append(ListBuku)

    print("\n===========data buku =============")

    for index, buku in enumerate(listData):
        print(f"{index+1} | {buku[0]}, | {buku[1]}")


    print("\n==============memastikan============")
    IsStop = input("apakah anda ingin lanjut(y/n)")
    if IsStop.lower() == "n" or IsStop.lower() == "no":
         break
        
print("program selesai")
