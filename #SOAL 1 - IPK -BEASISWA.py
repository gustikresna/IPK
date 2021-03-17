#SOAL 1 - IPK -BEASISWA
nim = list(map(int,input('Masukkan NIM (jika lebih dari satu, pisahkan dengan koma): ').split(',')))
nama = input('Masukkan Nama (jika lebih dari satu, pisahkan dengan koma): ').split(',')
alamat = input('Masukkan Alamat (jika lebih dari satu, pisahkan dengan koma): ').split(',')
asl_sklh = input('Masukkan Asal Sekolah (jika lebih dari satu, pisahkan dengan koma): ').split(',')
kode_prod = input('Masukkan Kode Prodi (jika lebih dari satu, pisahkan dengan koma): ').split(',')
nilai_ipk_awl = list(map(int,input('Masukkan IPK Awal (jika lebih dari satu, pisahkan dengan koma): ').split(',')))
nilai_uts = list(map(int,input('Masukkan UTS (jika lebih dari satu, pisahkan dengan koma): ').split(',')))
nilai_uas = list(map(int,input('Masukkan UAS (jika lebih dari satu, pisahkan dengan koma): ').split(',')))
nilai_tm = list(map(int,input('Masukkan TM (jika lebih dari satu, pisahkan dengan koma): ').split(',')))

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
print('| NIM\t', '| Nama\t\t', '| Alamat\t', '| Asal Sekolah\t', '| Kode Prodi\t', '| IPK\t\t', '| Beasiswa\t|') #print header
for i in range(len(nim)) : #print data
    print('| ', nim[i],'\t',
    '| ', nama[i],'\t',
    '| ', alamat[i],'\t',
    '| ', asl_sklh[i],'\t',
    '| ', kode_prod[i],'\t',
    '| ', nilai_ipk[i],'\t',
    '| ', beasiswa_list[i],'\t|')