"""
laporan.py

Berisi fungsi untuk membuat laporan
keseluruhan sistem perpustakaan.

Mengambil data dari:
- Linked List Buku
- Riwayat
- Favorit
- Rekomendasi
"""


class LaporanSistem:
    """
    Class untuk laporan perpustakaan.
    """

    def __init__(self, daftar_buku, riwayat, favorit, rekomendasi):
        """
        Menerima semua struktur data
        yang digunakan sistem.
        """

        self.daftar_buku = daftar_buku
        self.riwayat = riwayat
        self.favorit = favorit
        self.rekomendasi = rekomendasi

    # ======================================
    # LAPORAN UTAMA
    # ======================================

    def tampilkan_laporan(self):
        """
        Menampilkan laporan lengkap.
        """

        print("\n")
        print("=" * 45)
        print("        LAPORAN SISTEM PERPUSTAKAAN")
        print("=" * 45)

        # Statistik buku

        total = 0
        tersedia = 0
        dipinjam = 0

        current = self.daftar_buku.head

        while current:
            total += 1

            if current.data.status == "Tersedia":
                tersedia += 1

            else:
                dipinjam += 1
            current = current.next

        print(f"\nJumlah Buku       : {total}")
        print(f"Buku Tersedia     : {tersedia}")
        print(f"Buku Dipinjam     : {dipinjam}")

        # Riwayat

        print("\n")
        print("===== RIWAYAT AKTIVITAS =====")
        self.riwayat.tampil_mundur()

        # Favorit

        print("\n")
        print("===== BUKU FAVORIT =====")
        self.favorit.tampilkan()

        # Rekomendasi

        print("\n")
        print("===== REKOMENDASI =====")

        self.rekomendasi.tampilkan()

        print("\n")
        print("=" * 45)
