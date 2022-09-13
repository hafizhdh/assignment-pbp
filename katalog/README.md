# Tugas 2: Pengenalan Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Nama: Muhammad Hafizha Dhiyaulhaq

NPM : 2106750723

Kode Asdos: FAR

Heroku App link: https://assignment-pbp2.herokuapp.com/katalog/

## 1. Bagan Proses *Application* Django
<img src=/images/tugas2pbp.png width="720" height="720">

## 2. *Virtual Environment*
*Virtual environment* merupakan sebuah *environment* yang dibuat dalam projek kita untuk memisahkan dengan projek yang lainnya pada device yang sama. *Virtual environment* ini dibuat bertujuan agar tidak terjadi perbedaan *package* antar projek yang dibuat. Dikarenakan tidak semua projek yang kita buat memerlukan *package* yang sama atau versi yang sama. Sehingga jika terjadi perbedaan tersebut, kita masih tetap bisa menjalankan seperti biasa.

Kita masih bisa membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*.

## 3. Implementasi Pembuatan Django App

### a. Implementasi fungsi views.py 

views.py merupakan kode yang digunakan untuk menerima *request* dari *client* dan mengembalikan response dengan merender `katalog.html` pada folder templates dan context berupa *dictionary* yang berisi data yang sudah diambil dari database dengan memanfaatkan Class pada `models.py`.

### b. Routing

Ketika user meminta *request* pada browser, Django akan mencocokan pattern antara URL dengan path yang sudah ditulis pada `urls.py`. Apabila path yang diminta sesuai dengan path yang ada, Django akan memamnggil fungsi yang ada pada `views.py`.

### c. Pemetaan data

Sebelum menjalankan aplikasi katalog yang kita buat, kita perlu membuat data terlebih dahulu yang nantinya akan disimpan ke dalam database. Data pada aplikasi katalog ini berada pada `initial_catalog_item.json` yang ada pada folder fixtures. Kemudian kita perlu melakuan migrasi agar data kita dapat disimpan dalam database. Kemudian ketika user meminta *request*, kita akan mengambil data tersebut dengan memanggil fungsi pada `views.py` dan memetakan ke dalam `katalog.html`. `katalog.html` inilah yang akan di render dan di eksekusi kemudian ditampilkan kepada *client* pada web browser. 

### d. Deployment

Setelah Django app kita telah berhasil dibuat, kita perlu melakukan deployment agar web yang kita buat dapat diakses secara publik. Pada tugas ini, kita akan melakukan deployment pada aplikasi [heroku](www.heroku.com). Sebelum melakukan deployment, kita perlu membuat `Procfile` terlebih dahulu dan membuat `dpl.yml` pada folder `.github/workflws`. Setelah itu kita perlu mengatur *Repository Secret* yang berisi nama aplikasi dan API key Heroku kita. Maka, projek kita akan otomatis ter-deploy pada aplikasi heroku. Kita dapat mengakses aplikasi yang telah kita buat pada `https://<nama-aplikasi-heroku>.herokuapp.com`.





