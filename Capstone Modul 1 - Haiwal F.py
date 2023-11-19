# Capstone Modul 1
# Program ini ialah Sistem Informasi Karyawan untuk menyimpan dan menganalisis sederhana data karyawan di suatu perusahaan

listKaryawan = [
    {"IDKaryawan" : "17-2001", "Nama" : "Agung", "Jenis Kelamin" : "M", "Umur" : 37, "Jabatan" : "President CEO", "Gaji" : 50000000, "adminRight" : True, "Password" : "admin2001", "trueAdmin" : True}, 
    {"IDKaryawan" : "19-2002", "Nama" : "Wahyu", "Jenis Kelamin" : "M", "Umur" : 35, "Jabatan" : "Manager HRD", "Gaji" : 18000000, "adminRight" : True, "Password" : "admin2002", "trueAdmin" : False}, 
    {"IDKaryawan" : "19-2003", "Nama" : "Ahmad", "Jenis Kelamin" : "M", "Umur" : 27, "Jabatan" : "Staff HRD/GA", "Gaji" : 10000000, "adminRight" : True, "Password" : "admin2003", "trueAdmin" : False}, 
    {"IDKaryawan" : "20-2004", "Nama" : "Ega", "Jenis Kelamin" : "F", "Umur" : 24, "Jabatan" : "Staff Finance", "Gaji" : 7000000, "adminRight" : False, "Password" : "", "trueAdmin" : False},
    {"IDKaryawan" : "20-2005", "Nama" : "Abdul", "Jenis Kelamin" : "M", "Umur" : 44, "Jabatan" : "Office Boy", "Gaji" : 5000000, "adminRight" : False, "Password" : "", "trueAdmin" : False}]

def showDataKaryawan():
    print("""\n\t\t\tDaftar Karyawan PT Hidup Senang Selalu
    
|ID Karyawan\t| Nama\t| Jenis \t| Umur\t| Jabatan\t|
|\t\t|\t| Kelamin\t|\t|\t\t|""")
    for i in range(len(listKaryawan)):
        print("| {}\t| {}\t|  {}\t\t|  {}\t| {}\t|".format(listKaryawan[i]["IDKaryawan"], listKaryawan[i]["Nama"], listKaryawan[i]["Jenis Kelamin"], listKaryawan[i]["Umur"], listKaryawan[i]["Jabatan"]))

def showCertainDataKaryawan():
    certainID = input("Masukan ID Karyawan yang ingin anda lihat datanya : ")
    for karyawan in listKaryawan:
        if karyawan["IDKaryawan"] == certainID:
            print("""\n\t\t\tKaryawan PT Hidup Senang Selalu
    
|ID Karyawan\t| Nama\t| Jenis \t| Umur\t| Jabatan\t|
|\t\t|\t| Kelamin\t|\t|\t\t|""")
            print("| {}\t| {}\t|  {}\t\t|  {}\t| {}\t|".format(karyawan["IDKaryawan"], karyawan["Nama"], karyawan["Jenis Kelamin"], karyawan["Umur"], karyawan["Jabatan"]))
            break
    if certainID != karyawan["IDKaryawan"]:
        print("ID Karyawan yang anda masukan tidak terdaftar")

def checkAdmin():
    idCheck = input("ADMIN LOGIN - Masukan ID Karyawan anda (ketik apapun untuk kembali): ")
    for karyawan in listKaryawan:
        if karyawan["IDKaryawan"] == idCheck:
            if karyawan["adminRight"] == True:
                passCheck = input("Masukan password anda : ")
                if passCheck == karyawan["Password"]:
                    print("Admin Login berhasil!")
                    return True
                else:
                    print("Password yang anda masukan salah\n Login Gagal!")
            else:
                print("ID anda tidak memiliki hak akses Admin\n Login Gagal!")
            break
    else: 
        print("ID tidak dikenal\n Login gagal!")
    return False

def admin_showDataKaryawan():
    print("""\n\t\t\tDaftar Karyawan PT Hidup Senang Selalu
    
|ID Karyawan\t| Nama\t| Jenis \t| Umur\t| Jabatan\t| Gaji\t\t| Admin\t|
|\t\t|\t| Kelamin\t|\t|\t\t|\t\t|\t|""")
    for i in range(len(listKaryawan)):
        print("| {}\t| {}\t|  {}\t\t|  {}\t| {}\t| {}\t| {}\t|".format(listKaryawan[i]["IDKaryawan"], listKaryawan[i]["Nama"], listKaryawan[i]["Jenis Kelamin"], listKaryawan[i]["Umur"], listKaryawan[i]["Jabatan"], listKaryawan[i]["Gaji"], listKaryawan[i]["adminRight"]))

def admin_showCertainDataKaryawan():
    certainID = input("Masukan ID Karyawan yang ingin anda lihat datanya : ")
    for karyawan in listKaryawan:
        if karyawan["IDKaryawan"] == certainID:
            print("""\n\t\t\tDaftar Karyawan PT Hidup Senang Selalu
    
|ID Karyawan\t| Nama\t| Jenis \t| Umur\t| Jabatan\t| Gaji\t\t| Admin\t|
|\t\t|\t| Kelamin\t|\t|\t\t|\t\t|\t|""")
            print("| {}\t| {}\t|  {}\t\t|  {}\t| {}\t| {}\t| {}\t|".format(karyawan["IDKaryawan"], karyawan["Nama"], karyawan["Jenis Kelamin"], karyawan["Umur"], karyawan["Jabatan"], karyawan["Gaji"], karyawan["adminRight"]))
            break
    if certainID != karyawan["IDKaryawan"]:
        print("ID Karyawan yang anda masukan tidak terdaftar")

def admin_tambahKaryawan():
    idBaru = input("Masukan id karyawan sesuai format (tahun masuk - urutan masuk) : ")
    for karyawan in listKaryawan:
        if karyawan["IDKaryawan"] == idBaru:
            print("ID Karyawan sudah ada, masukan ID yang lain.")
            return
    namaBaru = input("Masukan nama karyawan baru : ")
    jenisKBaru = input("Masukan jenis kelamin karyawan baru(Pria=M / Wanita=F) : ")
    umurBaru = int(input("Masukan umur karyawan baru : "))
    jabatanBaru = input("Masukan jabatan pekerjaan karyawan baru : ")
    gajiBaru = int(input("Masukan jumlah gaji karyawan baru : "))
    adminBaru = input("Apakah karyawan baru diberikan hak akses admin (True/False) : ").lower() == "true"       
    if adminBaru:       #Membuat password untuk Admin
        passBaru = "admin" + idBaru[3:]
    else:
        passBaru = ""
    karyawanBaru = {
        "IDKaryawan": idBaru,
        "Nama": namaBaru,
        "Jenis Kelamin": jenisKBaru,
        "Umur": umurBaru,
        "Jabatan": jabatanBaru,
        "Gaji": gajiBaru,
        "adminRight": adminBaru,
        "Password" : passBaru,
        "trueAdmin" : False}
    
    print("""\n\t\t\tKaryawan Baru PT Hidup Senang Selalu
    
|ID Karyawan\t| Nama\t| Jenis \t| Umur\t| Jabatan\t| Gaji\t\t| Admin\t|
|\t\t|\t| Kelamin\t|\t|\t\t|\t\t|\t|""")
    print("| {}\t| {}\t|  {}\t\t|  {}\t| {}\t| {}\t| {}\t|".format(idBaru, namaBaru, jenisKBaru, umurBaru, jabatanBaru, gajiBaru, adminBaru))
    confirm = input("Apakah anda yakin untuk menyimpan data baru berikut? (Y/N) : ")       #Konfirmasi sebelum data disimpan
    while True:
        if confirm.upper() == "Y":
            listKaryawan.append(karyawanBaru)
            admin_showDataKaryawan()
            print("\nData karyawan baru telah berhasil dimasukan.")
            if adminBaru:
                print("Mohon ganti password anda di menu Update")
            break
        elif confirm.upper() == "N":
            break
        else:
            print("Input tidak dikenal, kembali ke menu sebelumnya")
            break

def admin_updateKaryawan():
    admin_showDataKaryawan()
    idUpdate = input("Masukan ID karyawan yang akan diupdate : ")

    for karyawan in listKaryawan:
        if karyawan["IDKaryawan"] == idUpdate:
            updateKey = input("Masukan nama key yang ingin diubah valuenya : ")
            if updateKey in karyawan.keys():                                #cek apakah ada key yang dicari pada tiap-tiap Key dictionary Karyawan
                updateVal = input("Masukan value baru : ")                                
                confirm = input("Apakah anda yakin untuk menyimpan data baru berikut? (Y/N) : ")
                while True:
                    if confirm.upper() == "Y":
                        karyawan[updateKey] = updateVal
                        admin_showDataKaryawan()
                        print("Data karyawan dengan ID {} telah berhasil diupdate.".format(idUpdate))
                        break
                    elif confirm.upper() == "N":
                        break
                    else:
                        print("Input tidak dikenal, kembali ke menu sebelumnya")
                        break
                break    
            else:
                print("Key tidak ditemukan")
                break
    else:
        print("ID karyawan tidak terdaftar")

def admin_hapusKaryawan():
    admin_showDataKaryawan()
    idHapus = input("Masukan ID karyawan yang akan dihapus : ")
    for index, karyawan in enumerate(listKaryawan):     #enumerate digunakan untuk mencari index dari ID Karyawan yang dicari
        if karyawan["IDKaryawan"] == idHapus:
            if karyawan["trueAdmin"] == True:
                print("CEO tidak dapat dihapus dari List Karyawan")
                break
            else:
                confirm = input("Apakah anda yakin untuk menghapus data karyawan berikut? (Y/N) : ")
                while True:
                    if confirm.upper() == "Y":
                        listKaryawan.pop(index)
                        admin_showDataKaryawan()
                        print("Data karyawan dengan ID {} telah berhasil dihapus.".format(idHapus))
                        break
                    elif confirm.upper() == "N":
                        break
                    else:
                        print("Input tidak dikenal, kembali ke menu sebelumnya")
                        break
                break
    else:
        print("ID karyawan {} tidak ditemukan, silahkan masukan kembali.".format(idHapus))

def diagnosisMF():
    totalMale = 0
    totalFemale = 0
    totalKaryawan = len(listKaryawan)

    for karyawan in listKaryawan:
        if karyawan["Jenis Kelamin"] == "M":
            totalMale += 1
        elif karyawan["Jenis Kelamin"] == "F":
            totalFemale += 1
        
    persenM = (totalMale/totalKaryawan)*100
    persenF = (totalFemale/totalKaryawan)*100

    print("Persentase karyawan Pria adalah {}, dan persentase karyawan Wanita adalah {}".format(persenM, persenF))

def diagnosisUmur():
    rangeUmur = {
    "20 - 30": 0,
    "31 - 40": 0,
    "41 - 50": 0,
    "51 tahun ke atas": 0}

    for karyawan in listKaryawan:
        umurKaryawan = karyawan["Umur"]
        if 20 <= umurKaryawan <= 30:
            rangeUmur["20 - 30"] += 1
        elif 31 <= umurKaryawan <= 40:
            rangeUmur["31 - 40"] += 1
        elif 41 <= umurKaryawan <= 50:
            rangeUmur["41 - 50"] += 1
        else:
            rangeUmur["51 tahun ke atas"] += 1
    
    print(rangeUmur)

#Struktur Menu Pilihan
while True:
    mainMenu = input("""\nSelamat datang di Sistem Informasi PT Hidup Senang Selalu
    
    Menu Utama:
    1. Tampilkan Daftar Karyawan
    2. Menambahkan Karyawan Baru [Admin Only]
    3. Update Data Karyawan [Admin Only]
    4. Menghapus Karyawan dari Daftar Karyawan [Admin Only]
    5. Diagnosis Data Karyawan
    6. Exit Program
    
    Silahkan masukan index angka pilihan anda : """)

    if mainMenu == "1":
        while True:
            readMenu = input("""\nRead Menu - Tampilkan Daftar Karyawan :
                         1. Tampilkan Daftar Karyawan
                         2. Tampilkan Daftar Karyawan sebagai Admin  [Admin Only]
                         3. Kembali ke Menu Utama
                         Silahkan masukan index angka pilihan anda : """)
            if readMenu == "1":
                while True:
                    subReadMenu = input("""\nSub-Read Menu - Tampilkan Daftar Karyawan
                                        1. Tampilkan Seluruh Data Karyawan
                                        2. Tampilkan Data Karyawan Tertentu
                                        3. Kembali ke Read Menu
                                        Silahkan masukan index angka pilihan anda : """)
                    if subReadMenu == "1":
                        showDataKaryawan()
                    elif subReadMenu == "2":
                        showCertainDataKaryawan()
                    elif subReadMenu == "3":
                        break
                    else:
                        print("Index angka tidak ditemukan.\nSilahkan masukan kembali.")
            elif readMenu == "2":
                while True:
                    if checkAdmin():
                        subReadMenu = input("""\nSub-Read Menu - Tampilkan Daftar Karyawan sebagai Admin
                                            1. Tampilkan Seluruh Data Karyawan
                                            2. Tampilkan Data Karyawan Tertentu
                                            3. Kembali ke Read Menu
                                            Silahkan masukan index angka pilihan anda : """)
                        if subReadMenu == "1":
                            admin_showDataKaryawan()
                        elif subReadMenu == "2":
                            admin_showCertainDataKaryawan()
                        elif subReadMenu == "3":
                            break
                        else:
                            print("Index angka tidak ditemukan.\nSilahkan masukan kembali.")
                    else:
                        break
            elif readMenu == "3":
                break
            else:
                print("Index angka tidak ditemukan.\nSilahkan masukan kembali.")
    elif mainMenu == "2":
        while True:
            createMenu = input("""\nCreate Menu - Menambahkan Karyawan Baru :
                         1. Menambahkan Karyawan Baru sebagai Admin  [Admin Only]
                         2. Kembali ke Menu Utama
                         Silahkan masukan index angka pilihan anda : """)
            if createMenu == "1":
                if checkAdmin():
                    admin_tambahKaryawan()
            elif createMenu == "2":
                break
            else:
                print("Index angka tidak ditemukan.\nSilahkan masukan kembali.")
    elif mainMenu == "3":
        while True:
            updateMenu = input("""\nUpdate Menu - Update Data Karyawan :
                         1. Update Data Karyawan sebagai Admin  [Admin Only]
                         2. Kembali ke Menu Utama
                         Silahkan masukan index angka pilihan anda : """)
            if updateMenu == "1":
                if checkAdmin():
                    admin_updateKaryawan()
            elif updateMenu == "2":
                break
            else:
                print("Index angka tidak ditemukan.\nSilahkan masukan kembali.")
    elif mainMenu == "4":
        while True:
            deleteMenu = input("""\nDelete Menu - Menghapus Data Karyawan :
                         1. Menghapus Karyawan dari Daftar Karyawan sebagai Admin  [Admin Only]
                         2. Kembali ke Menu Utama
                         Silahkan masukan index angka pilihan anda : """)
            if deleteMenu == "1":
                if checkAdmin():
                    admin_hapusKaryawan()
            elif deleteMenu == "2":
                break
            else:
                print("Index angka tidak ditemukan.\nSilahkan masukan kembali.")
    elif mainMenu == "5":
        while True:
            diagMenu = input("""\nDiagnosis Menu - Diagnosis Data Karyawan :
                         1. Persentase Karyawan Pria dan Wanita
                         2. Range Umur Karyawan
                         3. Kembali ke Menu Utama
                         Silahkan masukan index angka pilihan anda : """)
            if diagMenu == "1":
                diagnosisMF()
            if diagMenu == "2":
                diagnosisUmur()
            elif diagMenu == "3":
                break
    elif mainMenu == "6":
        break
    else:
        print("Index angka tidak ditemukan.\nSilahkan masukan kembali.")