"""
peminjaman.py

Implementasi Queue FIFO manual
untuk sistem peminjaman buku.

Fitur:
- Tambah antrian peminjaman
- Proses peminjaman
- Melihat antrian
"""

from src.core.node import QueueNode


class QueuePeminjaman:
    """
    Implementasi Queue menggunakan Node.
    FIFO:
    First In First Out
    Data yang disimpan:
    - nama peminjam
    - id buku
    """

    def __init__(self):

        # node awal
        self.front = None

        # node terakhir
        self.rear = None

    # ======================================
    # ENQUEUE
    # ======================================

    def tambah_antrian(self, data):
        """
        Menambahkan data ke belakang queue.
        """

        node_baru = QueueNode(data)

        # jika queue kosong

        if self.rear is None:
            self.front = node_baru
            self.rear = node_baru

        else:
            self.rear.next = node_baru
            self.rear = node_baru

        print("Peminjaman berhasil masuk antrian.")

    # ======================================
    # DEQUEUE
    # ======================================

    def proses_peminjaman(self):
        """
        Mengambil data paling depan.
        Data pertama masuk
        akan diproses pertama.
        """

        if self.front is None:
            print("Antrian kosong.")

            return None
        data = self.front.data
        self.front = self.front.next

        # jika queue menjadi kosong

        if self.front is None:
            self.rear = None

        return data

    # ======================================
    # LIHAT ANTRIAN
    # ======================================

    def tampilkan_antrian(self):
        """
        Menampilkan semua antrean.
        """

        if self.front is None:
            print("Tidak ada antrian peminjaman.")
            return

        current = self.front

        print("\n===== ANTRIAN PEMINJAMAN =====")

        nomor = 1

        while current:
            print(f"{nomor}. {current.data}")
            nomor += 1
            current = current.next

    # ======================================
    # CEK KOSONG
    # ======================================

    def kosong(self):
        return self.front is None
