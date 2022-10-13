# Tugas 6: Javascript dan AJAX

Nama : Muhammad Hafizha Dhiyaulhaq

NPM : 2106750723

Kelas : D

Herokuapp link: https://assignment-pbp2.herokuapp.com/todolist

User heroku:
```
username = pengguna1
password = YAFPptnYq6E63jR

username = pengguna2
password = 386bNuytV2Z9itY
```

1. Asynchronous vs Synchronous Programming
    
    a. Asynchronous Programming adalah *non-blocking architecture* yang artinya tidak melakukan *blocking* pada proses selanjutnya yang akan dijalankan ketika sedang melakukan proses yang saat ini dijalankan. Dengan asynchronous programming, kita dapat melakukan beberapa tasks secara bersamaan tanpa harus menunggu task yang lain selesai dijalankan. Pada web development, hal ini berarti kita masih bisa berinteraksi dengan web page tanpa menunggu web tersebut melakukan load data.

    b. Synchronous Programming adalah *blocking architecture* yang mana akan melakukan *blocking* pada operasi yang lain ketika operasi saat ini sedang dijalankan. Pada web development, hal ini berarti kita harus menunggu sebuah web untuk melakukan load data ketika kita ingin melakukan operasi yang lain.

    Sumber:
    https://courses.cs.washington.edu/courses/cse154/12au/lectures/slides/lecture22-ajax.shtml

    https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/

2. Event-driven Programming
    
    Merupakan suatu paradigma pemrograman dimana pengguna bisa menentukan alur jalannya suatu program dengan melakukan *event* yang dipanggil.

    Contoh pada tugas ini adalah ketika pengguna melakukan click pada button yang akan memanggil fungsi pada `<script>` yang telah dibuat.

3. Penerapan Asynchronous Programming pada AJAX

    Penerapan asynchronous programming pada AJAX dapat diterapkan saat user akan menambahkan task. Ketika user menekan tombol `Create Task` makan program akan memanggil fungsi `addTask` yang ada pada `<script>`. Setelah user menambahkan task, maka page secara asynchronus akan ter-refresh dan menampilkan task yang baru ditambahkan

4. Implementasi Tugas 6

    a. Membuat view baru yang mengembalikan data dalam bentuk JSON dan difilter berdasarkan user yang sedang login.
    implementasi fungsi `show_json` pada `views.py` dan tambahkan path pada `urls.py`
    
    ```py
    def show_json(request):
    user = request.user
    if user.is_authenticated:
        todolist = Task.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", todolist), content_type="application/json")
    # Jika belum login return data kosong
    return HttpResponse(serializers.serialize("json", {}), content_type="application/json")

    ```

    b. Implementasikan AJAX GET untuk menampilkan data todolist berdasarkan data json yang telah diimplementasi sebelumnya menggunakan javascript dan ditulis pada `todolist.html` pada tag `<script>`. Fungsi `getTodo()` akan mengambil data berupa json dan fungsi `refreshTodo()` akan menampilkan data yang telah diambil pada `todolist.html`

    c. Membuat modal untuk menambahkan data baru

    d. Membuat fungsi `add_task` pada `views.py` untuk menambahkan task dan tambahkan path pada `urls.py`

    e. Membuat fungsi javascript pada tag `<scrip>` di `todolist.html` yang digunakan untuk menambahkan task. Setelah berhasil menambahkan task, maka page secara asynchronus akan meng-update task yang baru saja ditambahkan. Tambahkan potongan kode berikut agar ketika menekan tombol `Create Task` akan memanggil fungsi `addTask()`

    ```javascript
    ...
    document.getElementById("button-add").onclick = addTask
    ...
    ```
