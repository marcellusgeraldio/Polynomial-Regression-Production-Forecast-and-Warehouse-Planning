🧮 **Polynomial Regression – Production Forecast and Warehouse Planning**

Dibuat oleh: **Marcellus Geraldio Florenta (2702262816)**  
Universitas Bina Nusantara – Computer Science  
Mata Kuliah: **Scientific Computing (Assurance of Learning)**  

---

## 📘 Deskripsi Proyek

Program ini bertujuan untuk **memprediksi tren produksi tas EGIER** berdasarkan data historis menggunakan metode **Polynomial Regression**.
Dengan model ini, perusahaan dapat memperkirakan **kapan kapasitas gudang akan mencapai batas maksimum**, serta menentukan waktu yang tepat untuk mulai membangun gudang baru.

Data produksi dibaca dari file **CSV** bernama `aol_data(in).csv`, yang berisi jumlah produksi tas bulanan selama 144 bulan (12 tahun).
Program melakukan fitting polinomial derajat 4 untuk mendapatkan model tren yang sesuai.

---

## 📌 Fitur Utama

✅ Membaca data produksi tas dari file CSV  
✅ Melakukan fitting polinomial derajat 4  
✅ Menghitung **Root Mean Squared Error (RMSE)** untuk mengukur akurasi model  
✅ Menentukan waktu (bulan ke-) ketika produksi mencapai batas maksimum (25.000 tas)  
✅ Menentukan waktu ideal untuk mulai membangun gudang baru (13 bulan sebelumnya)  
✅ Menampilkan grafik hasil prediksi dengan garis kapasitas gudang dan titik perkiraan waktu maksimum  

---

## ⚙️ Alur Program

1. Membaca data dari `aol_data(in).csv`
2. Melakukan konversi data menjadi array numerik
3. Melakukan fitting polinomial menggunakan `np.polyfit`
4. Menghasilkan model `polinomial_model` dan memprediksi nilai Y
5. Menghitung **RMSE** untuk mengukur selisih model dengan data aktual
6. Mencari akar (root) dari fungsi polinomial untuk menentukan kapan produksi mencapai 25.000 tas
7. Menampilkan grafik dan hasil perhitungan

---

## 🧠 Konsep yang Digunakan

* **Polynomial Regression** untuk memodelkan tren data produksi.
* **Root Mean Squared Error (RMSE)** untuk mengevaluasi ketepatan model.
* **fsolve (Scipy)** untuk mencari nilai waktu (x) saat produksi mencapai target tertentu.
* **Matplotlib** untuk visualisasi hasil.
* **NumPy & Pandas** untuk pengolahan data numerik.

---

## 📊 Output Program

Program akan menampilkan:

1. Grafik dengan:

   * Titik kuning: data produksi asli
   * Garis biru: hasil fitting polinomial
   * Garis hijau: batas maksimum gudang (25.000 tas)
   * Garis ungu: perkiraan waktu saat kapasitas tercapai

2. Hasil perhitungan di terminal:

   * Nilai RMSE
   * Bulan ke berapa kapasitas maksimum dicapai
   * Bulan ke berapa sebaiknya pembangunan gudang baru dimulai

---

## 🧾 Contoh Hasil Keluaran (Terminal)

```
Root Mean Squared Error (RMSE): 184.265
[] Perkiraan waktu untuk mencapai kapasitas maksimum gudang = bulan ke-158
[] Waktu untuk memulai pembangunan gudang baru = bulan ke-145
```

---

## 🪜 Langkah Menjalankan Program

1. Pastikan kamu sudah memiliki Python dan library berikut:

   * numpy
   * pandas
   * matplotlib
   * scipy
   * scikit-learn

2. Simpan file Python dengan nama `aol_project.py`

3. Simpan file data `aol_data(in).csv` di folder yang sama

4. Jalankan program melalui terminal atau IDE (seperti VS Code) dengan perintah:

```
python aol_project.py
```

---

## 🎯 Tujuan Pembelajaran

Proyek ini bertujuan untuk:

* Mengaplikasikan konsep **scientific computing** dalam analisis data nyata
* Melatih penggunaan **regresi polinomial** untuk prediksi tren
* Menunjukkan keterkaitan antara analisis matematis dan keputusan bisnis (perencanaan gudang)

---
