# Sistem Perpustakaan Digital

Sistem manajemen perpustakaan digital yang dibangun dengan Python menggunakan berbagai struktur data.

## Fitur Utama

### 1. Kelola Buku (Single Linked List)
- Tambah buku baru
- Hapus buku berdasarkan ID
- Tampilkan semua buku
- Cari buku

### 2. Peminjaman (Queue FIFO)
- Sistem antrian peminjaman
- Pencatatan peminjam
- Status real-time buku

### 3. Pengembalian Buku
- Proses pengembalian
- Update status buku

### 4. Searching Engine
- **Linear Search**: Pencarian berdasarkan judul/nama buku
- **Binary Search**: Pencarian berdasarkan ID buku

### 5. Sorting Engine
Mendukung 6 algoritma sorting:
- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort
- Merge Sort
- Shell Sort

### 6. Operasi Tree (Binary Search Tree)
- Inorder Traversal
- Preorder Traversal
- Postorder Traversal
- Pencarian berdasarkan ID

### 7. Riwayat Aktivitas (Double Linked List)
- Pencatatan semua aktivitas
- Tampilkan maju (dari awal)
- Tampilkan mundur (dari akhir)

### 8. Buku Favorit (Circular Singly Linked List)
- Tambah ke favorit
- Hapus dari favorit
- Tampilkan daftar favorit

### 9. Rekomendasi Buku (Circular Doubly Linked List)
- Navigasi rekomendasi
- Tambah/Hapus rekomendasi

### 10. Laporan Sistem
- Statistik buku (total, tersedia, dipinjam)
- Riwayat aktivitas terbaru
- Daftar buku favorit
- Rekomendasi saat ini

## Struktur Folder

```
UAS/
├── src/                 # Folder untuk semua fitur/modul
│   ├── __init__.py
│   ├── models.py       # Class Buku
│   ├── node.py         # Definisi semua Node
│   ├── buku.py         # Single Linked List
│   ├── peminjaman.py   # Queue
│   ├── riwayat.py      # Double Linked List
│   ├── favorit.py      # Circular Singly Linked List
│   ├── rekomendasi.py  # Circular Doubly Linked List
│   ├── tree.py         # Binary Search Tree
│   ├── searching.py    # Searching Engine
│   ├── sorting.py      # Sorting Engine
│   └── laporan.py      # Laporan Sistem
│
├── data/               # Folder untuk database
│   └── books.json      # Database buku lokal
│
├── readme/             # Folder untuk dokumentasi
│   ├── README.md       # File ini
│   └── (untuk PDF, video demo, dll)
│
└── main.py            # Program utama
```

## Cara Menggunakan

### 1. Menjalankan Program
```bash
python main.py
```

### 2. Menu Utama
Program akan menampilkan menu dengan pilihan:
- [1] Kelola Buku
- [2] Peminjaman
- [3] Pengembalian
- [4] Searching Engine
- [5] Sorting Engine
- [6] Operasi Tree
- [7] Laporan Sistem
- [0] Keluar

### 3. Contoh Penggunaan Fitur

**Tambah Buku:**
- Pilih menu [1] → [1] Tambah Buku
- Masukkan ID, judul, penulis, kategori, dan tahun

**Peminjaman Buku:**
- Pilih menu [2]
- Masukkan nama peminjam dan ID buku

**Pencarian:**
- Pilih menu [4]
- [1] Linear Search (cari berdasarkan judul)
- [2] Binary Search (cari berdasarkan ID)

**Sorting:**
- Pilih menu [5]
- Pilih metode sorting (1-6)

## Struktur Data yang Digunakan

| Fitur | Struktur Data |
|-------|---------------|
| Kelola Buku | Single Linked List |
| Peminjaman | Queue (FIFO) |
| Riwayat | Double Linked List |
| Favorit | Circular Singly Linked List |
| Rekomendasi | Circular Doubly Linked List |
| Tree | Binary Search Tree |

## Algoritma Pencarian

### Linear Search
- **Waktu:** O(n)
- **Keuntungan:** Data tidak perlu terurut
- **Digunakan untuk:** Pencarian berdasarkan judul

### Binary Search
- **Waktu:** O(log n)
- **Syarat:** Data harus terurut
- **Digunakan untuk:** Pencarian berdasarkan ID

## Algoritma Sorting

| Algoritma | Waktu Terbaik | Waktu Rata-rata | Waktu Terburuk | Space |
|-----------|---------------|-----------------|----------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Shell Sort | O(n log n) | O(n log² n) | O(n²) | O(1) |

## Catatan Penting

1. **Database Lokal:** Data buku tersimpan di `data/books.json`
2. **Riwayat:** Otomatis tercatat setiap aktivitas
3. **Status Buku:** 
   - "Tersedia" = Buku dapat dipinjam
   - "Dipinjam" = Buku sedang dipinjam
4. **Tree Search:** Untuk pencarian dengan ID menggunakan Binary Search Tree

## Kontak & Support

Untuk pertanyaan atau bug report, silahkan hubungi developer.

---
*Dibuat sebagai Tugas UAS Struktur Data - Semester 3*
