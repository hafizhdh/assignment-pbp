# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Nama: Muhammad Hafizha Dhiyaulhaq

NPM: 2106750723

Kelas: D

Kode Asdos: FAR

Herokuapp link: https://assignment-pbp2.herokuapp.com/todolist/

## 1. {% csrf_token %} 
csrf_token (*Cross-site request forgery token*) merupakan sebuah token yang digenerate oleh django ke browser ketika kita mengakses halaman tersebut. Token ini berguna untuk mencegah terjadinya tindak penyerangan CSRF yang berbahaya. Pada setiap sesinya, Django akan meng-generate token yang berbeda. Apabila kita tidak menambahkan `{% csrf_token %}` pada sebuah form, django tidak akan mengeksekusi form tersebut dan menolak request kita.

## 2. Pembuatan Form
Kita dapat membuat form secara manual tanpa menggunakan generator. Secara garis besar, kita perlu mengimplementasi sendiri bentuk form kita pada template html sesuai dengan field yang kita definisikan.

## 3. Alur Data
Pertama, user akan mengisi form untuk menambahkan task pada form yang telah kita buat. Informasi dari form tersebut akan diolah menjadi objek dari model `Task` kita dan akan disimpan pada database. Agar task yang baru ditambahkan bisa ditampilkan pada HTML, kita perlu mengambil objek `Task` kita dan difilter berdasarkan pengguna yang sedang login saat ini. Kemudian, kita passing hasil tersebut ke template HTML yang telah kita buat.

## 4. Implementasi Pembuatan Aplikasi todolist
1. Membuat aplikasi todolist dengan memanggil `py manage.py startapp todolist` pada projek kita dan daftarkan aplikasi todolist pada `project_django`
2. Membuat `urls.py` pada aplikasi todolist agar kita bisa melakukan routing sehingga aplikasi kita dapat diakses
3. Membuat sebuah model `Task` pada `models.py` yang berisi atribut sesuai dengan soal. 
4. Membuat form registrasi dengan memanfaatkan fungsi `UserCreationForm()` dari django kemudian menambahkan fungsi `register` dengan parameter request dari user pada `views.py` yang akan membuat form secara otomatis dan menghasilkan akun pengguna berdasarkan input dari form. Setelah itu, kita perlu membuat template HTML agar form registrasi yang kita buat dapat ditambilkan kepada user.
5. Membuat form untuk login dan merestriksi halaman utama kita. Untuk membuat form login, kita perlu membuat fungsi pada `views.py` yang akan meminta username dan password user yang mengakses. Kemudian username dan passowrd akan dicocokan dengan akun yang sudah terdaftar dan memutuskan apakah berhasil login atau tidak. Jangan lupa membuat template untuk login form kita agar bisa ditampilkan kepada user. Untuk restriksi, dilakukan untuk membedakan task antar user yang ada.
6. Membuat fungsi logout pada `views.py`
7. Membuat `todolist.html` sebagai halaman utama kita, yang memuat informasi mengenai user yang sedang login beserta task miliknya dan tombol untuk menambah task baru dan logout.
8. Membuat form baru untuk menambahkan task dengan membuat task secara manual pada `forms.py` dan ditampilkan pada `create-task.html`
9. Melakukan routing dengan mendaftarkan path baru yang kita buat pada `urls.py`
10. Untuk deployment ke heroku, kita hanya perlu melakukan `add`,`commit`, dan `push` pada repository github kita dan akan ter-deploy otomatis pada herokuapp kita.
11. List akun pengguna pada herokuapp

        username = pengguna1
        password = YAFPptnYq6E63jR

        username = pengguna2
        password = 386bNuytV2Z9itY

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

## 1. Perbedaan dari Inline, Internal, dan External CSS
 a. Inline Style merupakan konfigurasi CSS yang diterapkan langsung pada setiap tag HTML seperti `<p style=""></p>`. Style yang didefinisikan hanya berlaku pada tag tersebut saja.

```
Kelebihan:

Digunakan ketika kita ingin melakukan styling hanya pada satu tag saja tanpa harus mengubah konfigurasi yang lain

Kekurangan:

Tidak terlalu efisien untuk styling pada satu atau lebih page HTML.
```
 b. Internal Style merupakan konfigurasi CSS yang diterapkan pada satu page html yang ditulis pada `<head>` tag page tersebut. 
```
Kelebihan:

1. Dapat digunakan pada satu page HTML sehingga lebih efisien dibanding inline.
2. Dapat menggunakan `class` dan `ID selector` sehingga mempermudah penggunaan style pada banyak tag dalam satu page.

Kekurangan:

Dapat memperbesar ukuran web page dan meningkatkan loading time web tersebut
```
 c. External Style merupakan konfigurasi CSS yang diletakkan pada file `.css` yang berbeda dan bisa berlaku untuk lebih dari 1 page.

```
Kelebihan:

Hanya perlu menerapkan satu file `.css` untuk banyak page.

Kekurangan:

Bisa terjadi kesalahan rendering apabila file `.css` kita belum ter-load pada page kita.
```

## 2. Tag HTML5

`<nav>`: Untuk membuat navigation link pada page.

`<footer>`: Untuk membuat page footer.

`<header>`: Untuk membuat page header.

`<svg>`: Untuk menampilkan sebuah SVG (Scalable Vector Graphics) pada page.

`<time>`: Untuk menampilkan waktu atau tanggal.

`<dialog>`: Menampilkan window atau dialog box.

## 3. Tipe-tipe CSS selector

1. Element Selector
Selector ini diterapkan berdasarkan tag yang didefinisikan. Contoh:

```
p {
    color: red;
    ...
}
```
2. ID Selector
Selector ini diterapkan berdasarkan attribut ID dari HTML untuk memilih elemen tertentu. Contoh:
```
#id1{
    color: blue;
    ...
}
```
3. Class Selector
Selector ini akan memilih HTML elemen berdasarkan class attribut tertentu. Contoh:
```
.center {
  color: red;
  ...
}
```
4. Universal Selector
Selector ini akan memilih semua elemen HTML pada sebuah page. Contoh:
```
* {
  color: blue;
  ...
}
```

## 4. Implementasi Tugas 5
1. Untuk tugas 5 kali ini saya menggunakan framework CSS yaitu Bootstrap CSS. Agar dapat digunakan, kita perlu menambahkan barisan kode dibawah ke dalam `base.html` kita agar dapat digunakan ke semua HTML kita.
```HTML
<!-- base.html -->
...
 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  </head>
...
```
2. Melakukan kustomisasi pada halaman create task, login, register, dan todolist menggunakan Bootstrap. Untuk kustomisasi pada todolist, menggunakan class card yang telah disediakan oleh bootstrap.

3. Bootstrap sendiri telah membuat page kita menjadi responsive tanpa kita harus melakukan konfigurasi sendiri.