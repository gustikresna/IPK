#SOAL 1 - IPK -BEASISWA
jumlah_data = int(input('Masukkan Jumlah Data Mahasiswa/i yg ingin di-input : '))

#initiate list all data
nim = []
nama = []
alamat = []
asl_sklh = []
kode_prod = []
nilai_ipk_awl = []
nilai_uts = []
nilai_uas = []
nilai_tm = []

for i in range(jumlah_data):
    input_nim = int(input('Masukkan NIM : '))
    input_nama = input('Masukkan Nama : ')
    input_alamat = input('Masukkan Alamat : ')
    input_asl_sklh = input('Masukkan Asal Sekolah : ')
    input_kode_prod = input('Masukkan Kode Prodi : ')
    input_nilai_ipk_awl = int(input('Masukkan IPK Awal : '))
    input_nilai_uts = int(input('Masukkan Nilai UTS : '))
    input_nilai_uas = int(input('Masukkan Nilai UAS : '))
    input_nilai_tm = int(input('Masukkan Nilai TM : '))

    nim.append(input_nim)
    nama.append(input_nama)
    alamat.append(input_alamat)
    asl_sklh.append(input_asl_sklh)
    kode_prod.append(input_kode_prod)
    nilai_ipk_awl.append(input_nilai_ipk_awl)
    nilai_uts.append(input_nilai_uts)
    nilai_uas.append(input_nilai_uas)
    nilai_tm.append(input_nilai_tm)



nilai_ipk = [] #initiate list nilai ipk
beasiswa_list = [] #initiate list untuk beasiswa
for i in range(len(nim)): #looping untuk seluruh inputan
    ips = 0.3 * nilai_uts[i] + 0.3 * nilai_tm[i] + 0.4 * nilai_uas[i] #hitung nilai ips
    ipk = (nilai_ipk_awl[i] + ips) / 2 #update nilai ipk
    nilai_ipk.append(ipk) #tambahkan ke list ipk untuk seluruh inputan

    if kode_prod[i] == 'TI' or kode_prod[i] == 'SI': #jika prodi TI atau SI
        if ipk > 75 and ipk <= 85: #jika nilai 75 < ipk <= 85
            beasiswa = '20%'
        elif ipk > 85 and ipk <= 100 : #jika nilai 85 < ipk <= 100
            beasiswa = '30%'
        else :
            beasiswa = '0%'
    
    elif kode_prod[i] == 'DKV' or kode_prod[i] == 'Teknik Industri': #jika kode prodi DKV atau Tek Industri
        if ipk > 75 and ipk <= 85: #jika nilai 75 < ipk <= 85
            beasiswa = '25%'
        elif ipk > 85 and ipk <= 100 : #jika nilai 85 < ipk <= 100
            beasiswa = '35%'
        else : #jika di bawah 75
            beasiswa = '0%'

    else : #jika diluar kode prodi yg disebutkan
        print('Kode Prodi Tidak Ditemukan')
    
    beasiswa_list.append(beasiswa) #update list beasiswa

#print tabel
print(' ')
print ('| {:<10} | {:<15} | {:<20} | {:<20} | {:<20} | {:<8} | {:<10}|'.format('NIM','Nama','Alamat','Asal Sekolah','Kode Prodi','IPK', 'Beasiswa'))
for i in range(len(nim)):
    print ('| {:<10} | {:<15} | {:<20} | {:<20} | {:<20} | {:<8} | {:<10}|'.format(nim[i], nama[i], alamat[i], asl_sklh[i], kode_prod[i], nilai_ipk[i], beasiswa_list[i]))