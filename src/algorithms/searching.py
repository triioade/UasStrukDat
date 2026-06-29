"""
searching.py

Implementasi Searching Engine
Sistem Perpustakaan Digital

Metode:
1. Linear Search berdasarkan nama/judul buku
2. Binary Search berdasarkan ID buku
"""

class SearchingEngine:
    """
    Class untuk algoritma pencarian buku.
    """
    # ======================================
    # LINEAR SEARCH BY NAME
    # ======================================
    def linear_search_name(self, data_buku, nama_buku):
        """
        Linear Search berdasarkan judul buku.
        Karakteristik:
        - Tidak membutuhkan data terurut
        - Mengecek buku satu per satu
        Return:
        List buku yang memiliki nama sesuai keyword
        """

        hasil = []

        for buku in data_buku:
            if nama_buku.lower() in buku.judul.lower():
                hasil.append(buku)

        return hasil

    # ======================================
    # BINARY SEARCH BY ID
    # ======================================

    def binary_search_id(self, data_buku, id_buku):
        """
        Binary Search berdasarkan ID buku.
        Syarat:
        Data harus sudah terurut berdasarkan ID.
        Return:
        Object Buku jika ditemukan
        """

        kiri = 0
        kanan = len(data_buku) - 1

        while kiri <= kanan:
            tengah = (kiri + kanan) // 2
            id_tengah = data_buku[tengah].id_buku

            # data ditemukan

            if id_tengah == id_buku:
                return data_buku[tengah]

            # pencarian ke kanan

            elif id_buku > id_tengah:
                kiri = tengah + 1

            # pencarian ke kiri

            else:
                kanan = tengah - 1

        return None
