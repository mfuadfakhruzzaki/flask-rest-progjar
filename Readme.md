# REST API Flask

Ini adalah API RESTful Flask yang dikembangkan sebagai **tugas kelompok** untuk mata kuliah Pemrograman Jaringan di Semester 5.

## Anggota Kelompok

- Muhammad Fuad Fakhruzzaki
- Nezta Misgi Febyandanu
- Firman Gani Heriansyah
- Bagus Panggalih
- Listyawan Femil Anaki

## Base URL

Base URL pada http://localhost:5000/api

## Endpoint

### Rute Users

- `POST /users/register` - Mendaftarkan pengguna baru.
- `POST /users/login` - Masuk ke akun pengguna.
- `POST /users/logout` - Keluar dari akun pengguna.
- `POST /users/reset_password` - Mereset kata sandi pengguna.
- `DELETE /users/delete_user` - Menghapus akun pengguna.
- `PUT /users/update_user` - Memperbarui akun pengguna.

### Rute Stock

- `POST /stocks/add` - Menambahkan stok.
- `GET /stocks/check` - Memeriksa stok yang ada.
- `POST /stocks/Remove` - Mengambil barang dari stok.
- `DELETE /stocks` - Menghapus stok keseluruhan barang.
