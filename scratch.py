import time
import math

def keluar():
    text0 = " TERIMA KASIH TELAH MENGGUNAKAN APLIKASI KAMI "
    print(text0.center(100, "="))
    exit()

print("\n")
text = " PROGRAM MENGITUNG LUAS PERMUKAAN DAN VOLUME BANGUN RUANG "
time.sleep(2)
print(text.center(100, "="))
head = ("\nBERIKUT DAFTAR BANGUN RUANG YANG KAMI DUKUNG:"
        "\n\n1. KUBUS"
        "\n2. BALOK"
        "\n3. LIMAS SEGIEMPAT"
        "\n4. PRISMA SEGITIGA"
        "\n5. LIMAS SEGITIGA"
        "\n6. TABUNG"
        "\n7. KERUCUT"
        "\n8. BOLA"
        "\n9. KELUAR"
        f"\n\nMOHON UNTUK MEMASUKKAN BANGUN DATAR DI ATAS"
        f"\nMASUKKAN BANGUN DATAR: " f"\33[4mTABUNG"
        "\33[0m")
time.sleep(2)
print(head)

mulai = True
while mulai == True:
    time.sleep(2)
    bangundatar = input("\nMASUKKAN BANGUN RUANG:   ").upper()
    jalan = True

    while jalan == True:

        if bangundatar == "KELUAR":
            keluar()
        if bangundatar == "KUBUS":
            time.sleep(2)
            print("\nMENGHITUNG LUAS PERMUKAAN DAN VOLUME KUBUS")
            rusuk = int(input("MASUKKAN LUAS KUBUS:   "))
            luas = 6*rusuk*rusuk
            volume = rusuk*rusuk*rusuk
            print("LUAS PERMUKAAN KUBUS = ", luas, " DENGAN VOLUME = ", volume)
            masih = True
            while masih == True:
                exit_order = input("\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
                time.sleep(2)
                if exit_order == "YES":
                    mulai = True
                    jalan = False
                    break
                if exit_order == "NO":
                    print("\n")
                    keluar()
                else:
                    print("\nPERINTAH TIDAK DIKENALI")
                    time.sleep(2)
                    masih = True

        elif bangundatar == "BALOK":
            time.sleep(2)
            print("\nMENGHITUNG LUAS PERMUKAAN DAN VOLUME BALOK")
            panjang_balok = int(input("MASUKKAN PANJANG:    "))
            lebar_balok = int(input("MASUKKAN LEBAR:        "))
            tinggi_balok = int(input("MASUKKAN TINGGI:      "))
            luas_balok = (2*panjang_balok*lebar_balok)+(2*panjang_balok*tinggi_balok)+(2*lebar_balok*tinggi_balok)
            volume_balok = panjang_balok*lebar_balok*tinggi_balok
            print("\nLUAS PERMUKAAN BALOK = ", luas_balok, " DENGAN VOLUME = ", volume_balok)
            masih = True
            while masih == True:
                exit_order = input(
                    "\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
                time.sleep(2)
                if exit_order == "YES":
                    mulai = True
                    jalan = False
                    break
                if exit_order == "NO":
                    print("\n")
                    keluar()
                else:
                    print("\nPERINTAH TIDAK DIKENALI")
                    time.sleep(2)
                    masih = True

        elif bangundatar == "LIMAS SEGIEMPAT":
            time.sleep(2)
            print("\nMENGHITUNG LUAS PERMUKAAN DAN VOLUME LIMAS SEGIEMPAT")
            print("\nMASUKKAN TIAP LUAS SISI LIMAS SEGIEMPAT")
            sisi1 = int(input("MASUKKAN LUAS SISI 1:     "))
            sisi2 = int(input("MASUKKAN LUAS SISI 2:     "))
            sisi3 = int(input("MASUKKAN LUAS SISI 3:     "))
            sisi4 = int(input("MASUKKAN LUAS SISI 4:     "))
            sisi5 = int(input("MASUKKAN LUAS SISI 5:     "))
            print("\nMASUKKAN LUAS ALAS DAN TINGGI LIMAS SEGIEMPAT")
            luas_alas = int(input("MASUKKAN LUAS ALAS:   "))
            tinggi_limas = int(input("MASUKKAN TINGGI:   "))
            luas_limas = sisi1+sisi1+sisi3+sisi4+sisi5
            volume_limas = 1/3*luas_alas*tinggi_limas
            print("\nLUAS PERMUKAAN LIMAS SEGIEMPAT = ", luas_limas, " DENGAN VOLUME = ", volume_limas)
            masih = True
            while masih == True:
                exit_order = input(
                    "\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
                time.sleep(2)
                if exit_order == "YES":
                    mulai = True
                    jalan = False
                    break
                if exit_order == "NO":
                    print("\n")
                    keluar()
                else:
                    print("\nPERINTAH TIDAK DIKENALI")
                    time.sleep(2)
                    masih = True
        elif bangundatar == "PRISMA SEGITIGA":
            time.sleep(2)
            print("\nMENGHITUNG LUAS PERMUKAAN, LUAS SISI DAN VOLUME PRISMA SEGITIGA")
            print("\nMASUKKAN TIAP LUAS SISI PRISMA SEGITIGA")
            sisi_ps1 = int(input("MASUKKAN LUAS SISI a:   "))
            sisi_ps2 = int(input("MASUKKAN LUAS SISI b:   "))
            sisi_ps3 = int(input("MASUKKAN LUAS SISI c:   "))
            print("\nMASUKKAN TINGGI PRISMA SEGITIGA")
            tinggi_ps = int(input("MASUKKAN TINGGI:       "))
            print("\nMASUKKAN ALAS PRISMA SEGITIGA")
            alas_ps = int(input("MASUKKAN LUAS ALAS:      "))
            luas_sisi_ps = (sisi_ps1+sisi_ps2+sisi_ps3)*tinggi_ps
            luas_permukaan_ps = (2*alas_ps)+(sisi_ps1+sisi_ps2+sisi_ps3*tinggi_ps)
            volume_ps = alas_ps*tinggi_ps
            hasil = (f"\n\nLUAS PERMUKAAN PRISMA SEGITIGA =  {luas_permukaan_ps}"
                  f"\nDENGAN LUAS SISI = {luas_sisi_ps}"
                  f"\nDAN VOLUME =  {volume_ps}")
            print(hasil)
            masih = True
            while masih == True:
                exit_order = input(
                    "\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
                time.sleep(2)
                if exit_order == "YES":
                    mulai = True
                    jalan = False
                    break
                if exit_order == "NO":
                    print("\n")
                    keluar()
                else:
                    print("\nPERINTAH TIDAK DIKENALI")
                    time.sleep(2)
                    masih = True

        elif bangundatar == "LIMAS SEGITIGA":
            time.sleep(2)
            print("\nMENGHITUNG LUAS PERMUKAAN DAN VOLUME LIMAS SEGITIGA")
            print("\nMASUKKAN LUAS SISI LIMAS SEGTIGA")
            sisiab = int(input("MASUKKAN SISI a:            "))
            sisibb = int(input("MASUKKAN SISI b:            "))
            sisicb = int(input("MASUKKAN SISI c:            "))
            sisidb = int(input("MASUKKAN SISI d:            "))
            print("\nMASUKKAN LUAS ALAS DAN TINGGI LIMAS SEGITIGA")
            luas_alas_ls = int(input("MASUKKAN LUAS ALAS:   "))
            tinggi_ls = int(input("MASUKKAN TINGGI:         "))
            luas_sisi_ls = sisiab + sisibb + sisicb + sisidb
            volume_ls = 1/3*luas_alas_ls*tinggi_ls
            print("\nLUAS PERMUKAAN LIMAS SEGITIGA = ", luas_sisi_ls, " DENGAN VOLUME = ", volume_ls)
            masih = True
            while masih == True:
                exit_order = input(
                    "\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
                time.sleep(2)
                if exit_order == "YES":
                    mulai = True
                    jalan = False
                    break
                if exit_order == "NO":
                    print("\n")
                    keluar()
                else:
                    print("\nPERINTAH TIDAK DIKENALI")
                    time.sleep(2)
                    masih = True

        elif bangundatar == "TABUNG":
            time.sleep(2)
            print("\nMENGHITUNG LUAS SELIMUT, LUAS PERMUKAAN DAN VOLUME TABUNG")
            jari_selinder = int(input("MASUKKAN JARI-JARI:      "))
            tinggi_selinder = int(input("MASUKKAN TINGGI:       "))
            luas_selimut_selinder = 2*(math.pi)*jari_selinder*tinggi_selinder
            volume_selinder = (math.pi)*jari_selinder*jari_selinder*tinggi_selinder
            luas_permukaan_selinder = 2*(math.pi)*jari_selinder*(jari_selinder+tinggi_selinder)
            hasil_silinder = (f"\nLUAS SELIMUT SELINDER = {luas_selimut_selinder}"
                              f"\nDENGAN LUAS PERMUKAAN = {luas_permukaan_selinder}"
                              f"\nDAN VOLUME = {volume_selinder}")
            print(hasil_silinder)
            masih = True
            while masih == True:
                exit_order = input(
                    "\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
                time.sleep(2)
                if exit_order == "YES":
                    mulai = True
                    jalan = False
                    break
                if exit_order == "NO":
                    print("\n")
                    keluar()
                else:
                    print("\nPERINTAH TIDAK DIKENALI")
                    time.sleep(2)
                    masih = True

        elif bangundatar == "KERUCUT":
            time.sleep(2)
            print("\nMENGHITUNG LUAS SELIMUT, LUAS PERMUKAAN DAN VOLUME KERUCUT")
            jari_kerucut = int(input("MASUKKAN JARI-JARI:              "))
            garis_pelukis = int(input("MASUKKAN NILAI GARIS PELUKIS:   "))
            tinggi_kerucut = int(input("MASUKKAN NILAI TINGGI:         "))
            luas_alas_kerucut = 22/7*jari_kerucut*jari_kerucut
            luas_selimut_kerucut = 22/7*jari_kerucut*garis_pelukis
            luas_permukaan_kerucut = 22/7*jari_kerucut*garis_pelukis
            volume_kerucut = 1/3*luas_alas_kerucut*tinggi_kerucut
            hasil2 = (f"\nLUAS SELIMUT KERUCUT = {luas_selimut_kerucut}"
                      f"\nDENGAN LUAS PERMUKAAN = {luas_permukaan_kerucut}"
                      f"\nDAN VOLUME = {volume_kerucut}")
            print(hasil2)
            masih = True
            while masih == True:
                exit_order = input(
                    "\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
                time.sleep(2)
                if exit_order == "YES":
                    mulai = True
                    jalan = False
                    break
                if exit_order == "NO":
                    print("\n")
                    keluar()
                else:
                    print("\nPERINTAH TIDAK DIKENALI")
                    time.sleep(2)
                    masih = True

        elif bangundatar == "BOLA":
            time.sleep(2)
            print("\nMENGHITUNG LUAS DAN VOLUME BOLA")
            jari_bola = int(input("MASUKKAN JARI-JARI:  "))
            luas_bola = 4*22/7*jari_bola*jari_bola
            volume_bola = 4/3*22/7*jari_bola*jari_bola*jari_bola
            print("\nLUAS BOLA = ", luas_bola, " DAN VOLUME = ", volume_bola)
            masih = True
            while masih == True:
                exit_order = input(
                    "\nAPAKAH ANDA INGIN MELANJUTKAN? KETIK 'YES' JIKA IYA DAN 'NO' BILA TIDAK --- ").upper()
                time.sleep(2)
                if exit_order == "YES":
                    mulai = True
                    jalan = False
                    break
                if exit_order == "NO":
                    print("\n")
                    keluar()
                else:
                    print("\nPERINTAH TIDAK DIKENALI")
                    time.sleep(2)
                    masih = True
        else:
            time.sleep(2)
            print("MASUKKAN PERINTAH YANG TERTERA PADA MONITOR!")
            jalan = False
            time.sleep(2)
            bangundatar = input("\nMASUKKAN BANGUN DATAR:   ").upper()
            if bangundatar == "PERSEGI" or "PERSEGI PANJANG" or "JAJAR GENJANG" or "SEGITIGA" or "LAYANG-LAYANG" or "TRAPESIUM" or "BELAH KETUPAT" or "KELUAR" or "LINGKARAN":
                jalan = True

    if mulai == True:
        print("\n")
        kembali = " SELAMAT DATANG KEMBALI "
        print(kembali.center(100, "="))
        time.sleep(2)
        head1 = ("\nBERIKUT DAFTAR BANGUN RUANG YANG KAMI DUKUNG:"
                "\n\n1. KUBUS"
                "\n2. BALOK"
                "\n3. LIMAS SEGIEMPAT"
                "\n4. PRISMA SEGITIGA"
                "\n5. LIMAS SEGITIGA"
                "\n6. TABUNG"
                "\n7. KERUCUT"
                "\n8. BOLA"
                "\n9. KELUAR"
                f"\n\nMOHON UNTUK MEMASUKKAN BANGUN DATAR DI ATAS"
                f"\nMASUKKAN BANGUN DATAR: " f"\33[4mTABUNG"
                "\33[0m")
        time.sleep(2)
        print(head1)



