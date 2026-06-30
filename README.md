# Sistem Perpustakaan Digital

Sistem manajemen perpustakaan digital yang dibangun dengan Python menggunakan berbagai struktur data dan algoritma. Project ini adalah tugas UAS Struktur Data Semester 3.


##  Cara Menggunakan

## Video Dokumentasi
https://youtu.be/PLdEEXf4HMg

## Persyaratan

Sebelum menjalankan program, pastikan perangkat sudah memiliki:

* Sistem Operasi Windows
* Python versi 3.7 atau lebih baru
* Tidak membutuhkan library eksternal tambahan
Cek versi Python:
```bash
python --version
```
### Langkah Menjalankan Opsi 1

* Clone Repository Menggunakan Git

1. Buka Terminal atau Command Prompt:
2. git clone https://github.com/triioade/UasStrukDat.git
3. Masuk ke folder project:
4. cd UasStruDat
5. Jalankan program:

```bash
python main.py
```



### Langkah Menjalankan Opsi 2

* File project sudah didownload https://drive.google.com/drive/folders/1xPjd-GaiM5mPMaCCmHufC5DuZzq1PY9R

1. Ekstrak file ZIP project ke folder yang diinginkan.
2. Buka folder hasil ekstraksi.
3. Jalankan file:

```bash
python main.py
```
4. Program akan langsung menampilkan menu utama:

```
========================================
 SISTEM PERPUSTAKAAN DIGITAL 
========================================

[1] Kelola Buku
[2] Peminjaman
[3] Pengembalian
[4] Searching Engine
[5] Sorting Engine
[6] Operasi Tree
[7] Laporan Sistem
[8] Fitur Tambahan
[0] Keluar

Pilih menu :
```

### Contoh Penggunaan Fitur

#### 1️ Tambah Buku
```
Menu [1] → [1] Tambah Buku
- ID Buku : 1
- Judul : Algoritma dan Struktur Data
- Penulis : Rinaldi Munir
- Kategori : Pemrograman
- Tahun : 2020
```

#### 2️ Peminjaman Buku
```
Menu [2]
- Nama peminjam : Budi
- ID Buku : 1
✓ Buku berhasil masuk antrian
✓ Status buku berubah menjadi "Dipinjam"
```

#### 3️ Pencarian Buku
```
Menu [4]
→ [1] Linear Search (cari berdasarkan judul)
   Masukkan nama/judul buku : Algoritma
   
→ [2] Binary Search (cari berdasarkan ID)
   Masukkan ID Buku : 1
```

#### 4️ Sorting Buku
```
Menu [5]
- Pilih metode : 5 (Merge Sort)
✓ Menampilkan daftar buku yang sudah terurut
```

#### 5️ Visualisasi BST
```
Menu [8] → [4] Visualisasi BST
Menampilkan tree dalam format ASCII:
    ┌── 5
└── 3
    └── 7
```

#### 6️ Simpan Data JSON
```
Menu [8] → [1] Simpan Data JSON
- Nama file : my_library
✓ Data berhasil disimpan di data/my_library.json
```



## Fitur Utama

### 1. Kelola Buku (Single Linked List)
- Tambah buku baru
- Hapus buku berdasarkan ID
- Tampilkan semua buku
- Cari buku

### 2. Peminjaman (Queue FIFO)
- Sistem antrian peminjaman
- Pencatatan peminjam otomatis
- Update status buku menjadi "Dipinjam"

### 3. Pengembalian Buku
- Proses pengembalian buku
- Update status buku kembali ke "Tersedia"

### 4. Searching Engine
- Linear Search: Pencarian berdasarkan judul/nama buku (O(n))
- Binary Search: Pencarian berdasarkan ID buku (O(log n))

### 5. Sorting Engine
Mendukung 6 algoritma sorting:
- Bubble Sort - O(n²)
- Insertion Sort - O(n²)
- Selection Sort - O(n²)
- Quick Sort - O(n log n)
- Merge Sort - O(n log n)
- Shell Sort - O(n log² n)

### 6. Operasi Tree (Binary Search Tree)
- Inorder Traversal (Kiri - Root - Kanan)
- Preorder Traversal (Root - Kiri - Kanan)
- Postorder Traversal (Kiri - Kanan - Root)
- Pencarian berdasarkan ID

### 7. Riwayat Aktivitas (Double Linked List)
- Pencatatan semua aktivitas sistem
- Tampilkan dari awal (Forward)
- Tampilkan dari akhir (Backward)

### 8. Buku Favorit (Circular Singly Linked List)
- Tambah buku ke favorit
- Hapus dari favorit
- Tampilkan daftar favorit

### 9. Rekomendasi Buku (Circular Doubly Linked List)
- Navigasi rekomendasi (Next/Previous)
- Tambah/Hapus rekomendasi

### 10. Laporan Sistem
- Statistik buku (total, tersedia, dipinjam)
- Riwayat aktivitas terbaru
- Daftar buku favorit
- Rekomendasi saat ini

### 11. Fitur Tambahan
- Simpan Data JSON - Export data ke file JSON
- Muat Data JSON - Import data dari file JSON
- Statistik Perpustakaan - Dashboard analytics lengkap
- Visualisasi BST - Tampilkan tree dalam ASCII art

## Struktur Folder

```
UAS/
├── src/                          # Source code dengan modularisasi
│   ├── __init__.py
│   ├── algorithms/               # Algoritma pencarian & sorting
│   │   ├── __init__.py
│   │   ├── searching.py          # Linear & Binary Search
│   │   └── sorting.py            # 6 Algoritma Sorting
│   │
│   ├── core/                     # Inti sistem
│   │   ├── __init__.py
│   │   ├── models.py             # Class Buku
│   │   └── node.py               # Semua definisi Node
│   │
│   ├── structures/               # Struktur data
│   │   ├── __init__.py
│   │   ├── buku.py               # Single Linked List
│   │   ├── peminjaman.py         # Queue (FIFO)
│   │   ├── riwayat.py            # Double Linked List
│   │   ├── favorit.py            # Circular Singly LL
│   │   ├── rekomendasi.py        # Circular Doubly LL
│   │   └── tree.py               # Binary Search Tree
│   │
│   ├── services/                 # Layanan tambahan
│   │   ├── __init__.py
│   │   ├── json_manager.py       # Load/Save JSON
│   │   ├── analytics.py          # Statistik & Analytics
│   │   └── tree_visualizer.py    # Visualisasi BST ASCII
│   │
│   └── reports/                  # Laporan
│       ├── __init__.py
│       └── laporan.py            # Laporan Sistem
│
├── data/                         # Database lokal
│   └── books.json                # File data buku (contoh)
│
├── readme/                       # Dokumentasi
│   └── README.md                 # Dokumentasi lengkap
│
├── main.py                       # Program utama
└── README.md                     # File ini
```


##  Struktur Data yang Digunakan

| Fitur         | Struktur Data         | Karakteristik                 |
|---------------|-----------------------|-------------------------------|
| Kelola Buku   | Single Linked List    | Sequential access, Dynamic    |
| Peminjaman    | Queue (FIFO)          | First In First Out            |
| Riwayat       | Double Linked List    | Bidirectional traversal       |
| Favorit       | Circular Singly LL    | Circular, Sequential          |
| Rekomendasi   | Circular Doubly LL    | Circular, Bidirectional       |
| Tree          | Binary Search Tree    | Hierarchical, Sorted          |

##  Algoritma Pencarian

### Linear Search
- **Waktu Kompleksitas**: O(n)
- **Ruang Kompleksitas**: O(1)
- **Keuntungan**: Data tidak perlu terurut
- **Kerugian**: Lambat untuk data besar
- **Digunakan untuk**: Pencarian berdasarkan judul

### Binary Search
- **Waktu Kompleksitas**: O(log n)
- **Ruang Kompleksitas**: O(1)
- **Keuntungan**: Sangat cepat untuk data besar
- **Syarat**: Data harus terurut
- **Digunakan untuk**: Pencarian berdasarkan ID

##  Algoritma Sorting

| Algoritma         | Terbaik       | Rata-rata    | Terburuk      | Space     | Stabil |
|------------------ |-------------- |--------------|---------------|-----------|------- |
| Bubble Sort       | O(n)          | O(n²)        | O(n²)         | O(1)      | ✅    |
| Insertion Sort    | O(n)          | O(n²)        | O(n²)         | O(1)      | ✅    |
| Selection Sort    | O(n²)         | O(n²)        | O(n²)         | O(1)      | ❌    |
| Quick Sort        | O(n log n)    | O(n log n)   | O(n²)         | O(log n)  | ❌    |
| Merge Sort        | O(n log n)    | O(n log n)   | O(n log n)    | O(n)      | ✅    |
| Shell Sort        | O(n log n)    | O(n log² n)  | O(n²)         | O(1)      | ❌    |

##  Node Types

```python
# Single Linked List
Node(data)
├── data
└── next

# Queue
QueueNode(data)
├── data
└── next

# Double Linked List
DoubleNode(data)
├── data
├── prev
└── next

# Circular Singly LL
CircularNode(data)
├── data
└── next (→ circular)

# Circular Doubly LL
CircularDoubleNode(data)
├── data
├── prev (→ circular)
└── next (→ circular)

# Binary Search Tree
TreeNode(data)
├── data
├── left
└── right
```

##  Format File JSON

```json
{
  "books": [
    {
      "id_buku": 1,
      "judul": "Algoritma dan Struktur Data",
      "penulis": "Rinaldi Munir",
      "kategori": "Pemrograman",
      "tahun": 2020,
      "status": "Tersedia"
    }
  ]
}
```

##  Analytics & Statistik

Dashboard analytics menampilkan:
- Total jumlah buku
- Jumlah buku tersedia
- Jumlah buku dipinjam
- Persentase peminjaman
- Kategori paling populer
- Buku terbaru
- Penulis terbanyak

## Pembelajaran Struktur Data

### Single Linked List
- Operasi: Insert, Delete, Search, Display
- Waktu: O(n) untuk search & delete
- Aplikasi: Kelola Buku

### Queue (FIFO)
- Operasi: Enqueue, Dequeue
- Waktu: O(1) untuk enqueue & dequeue
- Aplikasi: Antrian Peminjaman

### Double Linked List
- Operasi: Insert, Delete, Forward/Backward Traversal
- Waktu: O(n) untuk traversal
- Aplikasi: Riwayat Aktivitas

### Circular Linked List
- Operasi: Traversal melingkar, Insert, Delete
- Aplikasi: Favorit, Rekomendasi

### Binary Search Tree
- Operasi: Insert, Delete, Search, Traversal (Inorder/Preorder/Postorder)
- Waktu: O(log n) - O(n) tergantung struktur
- Aplikasi: Operasi Tree

## Integrasi Sistem

```
main.py
  ├── LinkedListBuku (kelola buku)
  ├── QueuePeminjaman (antrian)
  ├── DoublyLinkedHistory (riwayat)
  ├── CircularFavorite (favorit)
  ├── CircularRecommendation (rekomendasi)
  ├── BinarySearchTree (tree)
  ├── SearchingEngine (cari)
  ├── SortingEngine (sort)
  ├── JSONManager (import/export)
  ├── Analytics (statistik)
  └── TreeVisualizer (visualisasi)
```

##  Teknis

### Validasi Input
-  Error handling untuk input invalid
-  Cek duplikasi saat load JSON
-  Validasi format JSON

### Performance
-  Algoritma optimal untuk setiap operasi
-  Memory efficient (tidak menggunakan library berat)
-  Real-time processing

##  Catatan Penting

1. **Data Persistence**: Data tersimpan dalam memori selama program berjalan
2. **JSON Export**: Gunakan fitur "Simpan Data JSON" untuk menyimpan data permanen
3. **Status Buku**: 
   - "Tersedia" = Buku dapat dipinjam
   - "Dipinjam" = Buku sedang dipinjam, tidak bisa dipinjam lagi
4. **Riwayat**: Otomatis tercatat setiap aktivitas (tambah, hapus, pinjam, dll)
5. **Tree Search**: Menggunakan Binary Search Tree untuk performa optimal

##  Troubleshooting

### Error: "Data tidak ditemukan"
- Pastikan file JSON ada di folder `data/`
- Periksa nama file (case-sensitive)

### Buku tidak muncul di tree
- Buku hanya ditambahkan ke tree saat ditambahkan melalui "Kelola Buku"
- Tree tidak terupdate jika load dari JSON, perlu tambah buku baru

### Visualisasi BST tidak menampil
- Tree masih kosong, tambahkan beberapa buku terlebih dahulu

##  Referensi

Struktur data diimplementasikan dari:
- Introduction to Algorithms (CLRS)
- Data Structures and Algorithms in Python
- Algorithms 4th Edition (Sedgewick & Wayne)

##  Kontribusi

Project ini adalah hasil pembelajaran Struktur Data Semester 3.

---

**Terakhir diupdate**: 2026-06-29  
**Status**: ✅ Selesai & Teruji  
**Python Version**: 3.7+  
**License**: Educational Purpose

---

**Selamat menggunakan Sistem Perpustakaan Digital! ✨**
