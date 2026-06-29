"""
analytics.py

Modul analisis data perpustakaan.

Menghasilkan statistik:
- jumlah buku
- status buku
- kategori populer
- buku terbaru
- penulis terbanyak
"""


class Analytics:
    def __init__(
        self,
        daftar_buku
    ):
        """
        Parameter:
        daftar_buku:
            Single Linked List buku
        """

        self.daftar_buku = daftar_buku

    # =====================================
    # AMBIL DATA BUKU
    # =====================================

    def get_books(self):
        """
        Mengubah Linked List
        menjadi list biasa.
        Digunakan untuk analisis.
        """

        data = []
        current = self.daftar_buku.head

        while current:
            data.append(
                current.data
            )
            current = current.next
        return data

    # =====================================
    # TOTAL BUKU
    # =====================================

    def total_buku(self):
        return len(
            self.get_books()
        )

    # =====================================
    # STATISTIK STATUS
    # =====================================

    def statistik_status(self):

        """
        Menghitung:
        - tersedia
        - dipinjam
        """
        tersedia = 0
        dipinjam = 0

        for buku in self.get_books():

            if buku.status == "Tersedia":
                tersedia += 1

            else:
                dipinjam += 1
        return (
            tersedia,
            dipinjam
        )



    # =====================================
    # KATEGORI TERBANYAK
    # =====================================

    def kategori_terpopuler(self):

        kategori = {}

        for buku in self.get_books():
            nama = buku.kategori
            if nama in kategori:
                kategori[nama] += 1
            else:
                kategori[nama] = 1
        if not kategori:
            return None
        return max(
            kategori,
            key=kategori.get
        )



    # =====================================
    # BUKU TERBARU
    # =====================================


    def buku_terbaru(self):
        data = self.get_books()
        if not data:
            return None

        terbaru = data[0]

        for buku in data:
            if buku.tahun > terbaru.tahun:
                terbaru = buku
        return terbaru


    # =====================================
    # PENULIS TERBANYAK
    # =====================================


    def penulis_terbanyak(self):
        penulis = {}
        for buku in self.get_books():
            nama = buku.penulis
            if nama in penulis:
                penulis[nama] += 1
            else:
                penulis[nama] = 1
        if not penulis:
            return None
        return max(
            penulis,
            key=penulis.get
        )

    # =====================================
    # DASHBOARD ANALYTICS
    # =====================================

    def tampilkan_dashboard(self):
        total = self.total_buku()
        tersedia, dipinjam = (
            self.statistik_status()
        )

        print("\n")
        print("="*45)
        print(
            "       ANALYTICS PERPUSTAKAAN"
        )
        print("="*45)

        print(
            f"Total Buku       : {total}"
        )
        print(
            f"Buku Tersedia    : {tersedia}"
        )
        print(
            f"Buku Dipinjam    : {dipinjam}"
        )
        if total > 0:
            persen = (
                dipinjam / total
            ) * 100
            print(
                f"Persentase Pinjam: {persen:.2f}%"
            )
        kategori = (
            self.kategori_terpopuler()
        )
        print(
            "\nKategori Terpopuler:"
        )

        if kategori:
            print(
                f"- {kategori}"
            )

        else:
            print(
                "Tidak ada data"
            )
        terbaru = (
            self.buku_terbaru()
        )
        print(
            "\nBuku Terbaru:"
        )


        if terbaru:
            print(
                f"- {terbaru.judul}"
            )
            print(
                f"  Tahun: {terbaru.tahun}"
            )


        penulis = (
            self.penulis_terbanyak()
        )
        print(
            "\nPenulis Terbanyak:"
        )


        if penulis:
            print(
                f"- {penulis}"
            )
        print("\n")
        print("="*45)