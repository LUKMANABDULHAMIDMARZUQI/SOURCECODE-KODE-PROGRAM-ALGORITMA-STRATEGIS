def knapsack_greedy_interaktif():
    print("\n" + "="*50)
    print("==== KNAPSACK PROBLEM (GREEDY) ====")
    print("NIM: 23533767")
    print("="*50)
    
    try:
        jumlah_objek = int(input("\nMasukkan jumlah objek: "))
        if jumlah_objek <= 0:
            print("Jumlah objek harus lebih dari 0. Proses dibatalkan.")
            return

        daftar_berat = []
        daftar_profit = []
        
        print("\n--- Masukkan Berat (Weight) untuk setiap objek ---")
        for i in range(jumlah_objek):
            berat = int(input(f"  Berat Objek ke-{i+1} : "))
            if berat <= 0:
                print("Berat harus positif. Proses dibatalkan.")
                return
            daftar_berat.append(berat)
        
        print("\n--- Masukkan Profit untuk setiap objek ---")
        for i in range(jumlah_objek):
            profit = int(input(f"  Profit Objek ke-{i+1} : "))
            if profit < 0:
                print("Profit tidak boleh negatif. Proses dibatalkan.")
                return
            daftar_profit.append(profit)
        
        kapasitas = int(input("\nMasukkan kapasitas knapsack: "))
        if kapasitas <= 0:
            print("Kapasitas knapsack harus positif. Proses dibatalkan.")
            return

    except ValueError:
        print("\nInput tidak valid. Harap masukkan angka. Proses dibatalkan.")
        return
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}. Proses dibatalkan.")
        return

    daftar_objek = []
    for i in range(len(daftar_berat)):
        daftar_objek.append({
            'id': i + 1,
            'berat': daftar_berat[i],
            'profit': daftar_profit[i],
            'rasio': daftar_profit[i] / daftar_berat[i]
        })

    daftar_objek.sort(key=lambda x: x['rasio'], reverse=True)

    total_profit = 0
    total_berat = 0
    objek_terpilih = []

    print("\n" + "-"*50)
    print("Objek yang Tersedia (sudah diurutkan berdasarkan Profit/Weight Ratio):")
    print("-" * 50)
    print(f"{'No.':<5}{'Berat':<10}{'Profit':<10}{'Rasio P/B':<15}")
    print("-" * 50)
    for objek in daftar_objek:
        print(f"{objek['id']:<5}{objek['berat']:<10}{objek['profit']:<10}{objek['rasio']:.2f}")
    print("-" * 50)

    print(f"\nKapasitas Knapsack Maksimal: {kapasitas}")
    print("\n--- Proses Pemilihan Item ---")
    sisa_kapasitas = kapasitas
    for objek in daftar_objek:
        if objek['berat'] <= sisa_kapasitas:
            objek_terpilih.append(objek)
            sisa_kapasitas -= objek['berat']
            total_profit += objek['profit']
            total_berat += objek['berat']
            print(f"  Memilih Objek ke-{objek['id']} (B: {objek['berat']}, P: {objek['profit']})")
            print(f"    Kapasitas Tersisa: {sisa_kapasitas:<3}, Total Berat: {total_berat:<3}, Total Profit: {total_profit:<4}")
        else:
            print(f"  Tidak dapat memilih Objek ke-{objek['id']} (B: {objek['berat']}) karena melebihi kapasitas.")
            print(f"    Sisa Kapasitas: {sisa_kapasitas}")
        print("-" * 20)

    print("\n" + "="*50)
    print("===== Hasil Knapsack Problem (Greedy) =====")
    print("Item yang Terpilih:")
    if not objek_terpilih:
        print("  Tidak ada item yang dipilih.")
    else:
        print(f"{'Item':<10}{'Berat':<10}{'Profit':<10}")
        print("-" * 30)
        for objek in objek_terpilih:
            print(f"{objek['id']:<10}{objek['berat']:<10}{objek['profit']:<10}")
        print("-" * 30)
    print(f"\nTotal Berat Item Terpilih: {total_berat}")
    print(f"Total Keuntungan Maksimal: {total_profit}")
    print("==============================================")


def penukaran_koin():
    print("\n" + "="*50)
    print("==== PENUKARAN KOIN (GREEDY) ====")
    print("NIM: 23533767")
    print("="*50)
    try:
        jumlah_jenis = int(input("\nMasukkan jumlah jenis koin: "))
        if jumlah_jenis <= 0:
            print("Jumlah jenis koin harus lebih dari 0. Proses dibatalkan.")
            return

        daftar_koin = []
        print("\n--- Masukkan nilai setiap jenis koin ---")
        for i in range(jumlah_jenis):
            koin = int(input(f"Koin ke-{i+1}: "))
            if koin <= 0:
                print("Nilai koin harus positif. Proses dibatalkan.")
                return
            daftar_koin.append(koin)
        
        nilai_tukar = int(input("\nMasukkan nilai yang ingin ditukarkan: "))
        if nilai_tukar < 0:
            print("Nilai yang ingin ditukarkan tidak boleh negatif. Proses dibatalkan.")
            return

    except ValueError:
        print("\nInput tidak valid. Harap masukkan angka. Proses dibatalkan.")
        return
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}. Proses dibatalkan.")
        return

    daftar_koin.sort(reverse=True)
    jumlah_keping = {}
    sisa = nilai_tukar

    print("\n--- Proses Penukaran Koin ---")
    for koin in daftar_koin:
        if sisa >= koin:
            banyak = sisa // koin
            sisa -= banyak * koin
            jumlah_keping[koin] = banyak
            print(f"  Mengambil {banyak:<3} keping koin {koin}-an. Sisa nilai: {sisa}")
        else:
            jumlah_keping[koin] = 0
            print(f"  Tidak mengambil keping koin {koin}-an. Sisa nilai: {sisa}")
    print("-" * 50)

    print("\n" + "="*50)
    print("===== Hasil Penukaran Koin =====")
    print(f"Nilai yang ditukarkan: {nilai_tukar}")
    print("\nDetail Keping Koin:")
    for koin in sorted(jumlah_keping.keys(), reverse=True):
        print(f"  Jumlah Keping {koin:<4}-an sebanyak {jumlah_keping[koin]}")
    
    if sisa > 0:
        print(f"\nSisa yang tidak bisa ditukar: {sisa}")
    print("==============================================")


def merge_sort_proses(data, level=0):
    indentasi = "  " * level
    if len(data) <= 1:
        return data

    tengah = len(data) // 2
    kiri = data[:tengah]
    kanan = data[tengah:]

    print(f"{indentasi}Membagi: {data} -> Kiri: {kiri}, Kanan: {kanan}")

    kiri_urut = merge_sort_proses(kiri, level + 1)
    kanan_urut = merge_sort_proses(kanan, level + 1)

    hasil_gabungan = gabung(kiri_urut, kanan_urut)
    print(f"{indentasi}Menggabungkan: Kiri Terurut: {kiri_urut}, Kanan Terurut: {kanan_urut} -> Hasil: {hasil_gabungan}")
    return hasil_gabungan

def gabung(kiri, kanan):
    hasil = []
    i = j = 0

    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    while i < len(kiri):
        hasil.append(kiri[i])
        i += 1
    while j < len(kanan):
        hasil.append(kanan[j])
        j += 1
    return hasil

def jalankan_merge_sort():
    print("\n" + "="*50)
    print("==== MERGE SORT (DIVIDE AND CONQUER) ====")
    print("NIM: 23533767")
    print("="*50)
    try:
        masukan = input("\nMasukkan angka-angka untuk diurutkan (pisahkan dengan spasi): ")
        data = list(map(int, masukan.split()))
        
        if not data:
            print("Tidak ada data yang dimasukkan untuk diurutkan. Proses dibatalkan.")
            return

        print(f"\nData sebelum diurutkan: {data}")
        print("\n--- Proses Merge Sort ---")
        hasil = merge_sort_proses(data) 
        print("\n--- Proses Selesai ---")
        print(f"\nData setelah Merge Sort: {hasil}")
        print("==============================================")
    except ValueError:
        print("\nInput tidak valid. Harap masukkan angka yang dipisah spasi. Proses dibatalkan.")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}. Proses dibatalkan.")


def main():
    print("="*50)
    print("      PROGRAM TUGAS BESAR PRA UAS ALGORITMA STRATEGIS         ")
    print("="*50)
    print("Oleh: Lukman Abdul Hamid Marzuqi")
    print("NIM: 23533767")
    print("-" * 50)

    while True:
        print("\n====== MENU UTAMA ======")
        print("1. Knapsack Problem (Greedy)")
        print("2. Penukaran Koin (Greedy)")
        print("3. Merge Sort (Divide and Conquer)")
        print("0. Keluar")
        print("-" * 25)
        pilihan = input("Pilih menu (0-3): ")
        print("-" * 50)

        if pilihan == '1':
            knapsack_greedy_interaktif()
        elif pilihan == '2':
            penukaran_koin()
        elif pilihan == '3':
            jalankan_merge_sort()
        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan program.")
            print("Oleh: Lukman Abdul Hamid Marzuqi")
            print("NIM: 23533767")
            print("==============================================")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
