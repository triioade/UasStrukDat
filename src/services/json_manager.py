"""
json_manager.py

Mengatur import dan export data buku
menggunakan file JSON.

Fitur:
- Load file JSON berdasarkan input user
- Validasi format JSON
- Cek duplikasi judul buku
- Save file JSON ke folder data
"""
import json
import os
from src.core.models import Buku

class JSONManager:

    def __init__(self):
        self.folder = "data"

        # membuat folder jika belum ada

        if not os.path.exists(
            self.folder
        ):
            os.makedirs(
                self.folder
            )



    # =====================================
    # LOAD JSON
    # =====================================


    def load_json(
        self,
        nama_file,
        daftar_buku
    ):
        """
        Membaca file JSON
        dan memasukkan buku baru.
        Parameter:
        nama_file :
            nama file tanpa/sama dengan .json
        daftar_buku :
            list buku yang sudah ada
        """
        if not nama_file.endswith(
            ".json"
        ):
            nama_file += ".json"

        path = os.path.join(
            self.folder,
            nama_file
        )

        # cek file
        if not os.path.exists(path):
            print(
                "Data tidak ditemukan."
            )
            return []

        # baca JSON
        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print(
                "File harus berbentuk JSON."
            )
            print(
                "Format file tidak valid."
            )
            return []

        except Exception:
            print(
                " Gagal membaca file."
            )
            return []

        buku_baru = []
        # mengambil judul yang sudah ada

        judul_lama = []


        for buku in daftar_buku:
            judul_lama.append(
                buku.judul.lower()
            )



        # proses data JSON
        for item in data.get(
            "books",
            []
        ):



            judul = item["judul"]
            if judul.lower() in judul_lama:
                print(
                    f' Buku "{judul}" sudah tersedia,dan akan dilewati.'
                )
                continue

            buku = Buku(

                item["id_buku"],
                item["judul"],
                item["penulis"],
                item["kategori"],
                item["tahun"]
            )

            buku.status = item.get(
                "status",
                "Tersedia"
            )

            buku_baru.append(
                buku
            )

            judul_lama.append(
                judul.lower()
            )

            print(
                f' Buku "{judul}" berhasil ditambahkan.'
            )

        return buku_baru

    # =====================================
    # SAVE JSON
    # =====================================

    def save_json(
        self,
        nama_file,
        daftar_buku
    ):
        """
        Menyimpan data buku
        ke folder data/
        """

        if not nama_file.endswith(
            ".json"
        ):
            nama_file += ".json"

        path = os.path.join(
            self.folder,
            nama_file
        )

        data = {
            "books":[]
        }



        for buku in daftar_buku:

            data["books"].append({

                "id_buku":
                    buku.id_buku,
                "judul":
                    buku.judul,
                "penulis":
                    buku.penulis,
                "kategori":
                    buku.kategori,
                "tahun":
                    buku.tahun,
                "status":
                    buku.status
            })


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(
            " Data berhasil disimpan."
        )

        print(
            f"Lokasi: {path}"
        )