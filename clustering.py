import math

# 1. DATASET (24 data mahasiswa kamu)
data_mahasiswa = [
    [7, 2, 1], [7, 0 ,3], [6, 1, 5], [3, 1, 1], [8, 1, 3], [4, 0, 3], 
    [6, 1, 1], [5, 0, 0], [5, 4, 3], [5, 0, 3], [5, 1, 0], [8, 1, 3],
    [3, 2, 3], [4, 2, 2], [2, 0, 3], [5, 1, 3], [2, 3, 2], [6, 1, 2], 
    [6, 0, 6], [9, 0, 3], [6, 0, 3], [5, 1, 3], [9, 1, 1], [5, 2, 2],
    [4, 2, 6]
]

# 2. CENTROID AWAL
centroids = [
    [9, 1, 1],  # C1
    [5, 4, 3],   # C2
    [6, 0, 6],  # C3
    [3, 1, 1]    # C4
]

def hitung_jarak(titik1, titik2):
    return math.sqrt(
        (titik1[0] - titik2[0])**2 + 
        (titik1[1] - titik2[1])**2 + 
        (titik1[2] - titik2[2])**2
    )

def k_means(data, pusat_kelompok, max_iterasi=10):
    for i in range(max_iterasi):
        print(f"\n========================================")
        print(f"             ITERASI {i+1}              ")
        print(f"========================================")
        
        # Penampung cluster
        clusters = [[] for _ in range(len(pusat_kelompok))]
        
        print("\n[PROSES A: Menghitung Jarak Mahasiswa ke Centroid]")
        # LANGKAH A: ASSIGNMENT dengan Cetak Proses Detail
        for idx, mhs in enumerate(data):
            # Hitung jarak mhs ke 4 centroid, bulatkan 2 desimal untuk tampilan proses
            jarak_ke_semua_centroid = [hitung_jarak(mhs, c) for c in pusat_kelompok]
            jarak_tampilan = [round(j, 2) for j in jarak_ke_semua_centroid]
            
            # Cari yang terdekat
            cluster_terdekat = jarak_ke_semua_centroid.index(min(jarak_ke_semua_centroid))
            clusters[cluster_terdekat].append(mhs)
            
            # Cetak jalannya proses per mahasiswa
            print(f"Mhs ke-{idx+1} {mhs} -> Jarak ke [C1, C2, C3, C4]: {jarak_tampilan} -> Masuk Cluster {cluster_terdekat+1}")
        
        print("\n[RINGKASAN ANGGOTA CLUSTER ITERASI INI]")
        for j, c in enumerate(clusters):
            print(f"  * Cluster {j+1}: {len(c)} mahasiswa")

        print("\n[PROSES B: Memperbarui Posisi Centroid (Rata-rata)]")
        new_centroids = []
        for j, group in enumerate(clusters):
            if not group: 
                print(f"  * Centroid {j+1} Kosong! Menggunakan koordinat lama: {pusat_kelompok[j]}")
                new_centroids.append(pusat_kelompok[j])
                continue
            
            rata_sosmed = round(sum(m[0] for m in group) / len(group), 2)
            rata_game = round(sum(m[1] for m in group) / len(group), 2)
            rata_belajar = round(sum(m[2] for m in group) / len(group), 2)
            
            centroid_baru_sekarang = [rata_sosmed, rata_game, rata_belajar]
            print(f"  * Centroid {j+1} Baru (Rata-rata dari {len(group)} data): {centroid_baru_sekarang}")
            new_centroids.append(centroid_baru_sekarang)
        
        # Cek apakah centroid berubah
        if new_centroids == pusat_kelompok: 
            print(f"\n========================================")
            print("KONVERGEN! Centroid sudah tidak berubah lagi.")
            print(f"========================================")
            break
            
        pusat_kelompok = new_centroids

    return clusters, pusat_kelompok

# Jalankan Program
hasil_cluster, centroid_final = k_means(data_mahasiswa, centroids)