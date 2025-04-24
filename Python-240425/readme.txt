PYTHON CASTING

Chapter ini menjelaskan tentang apa itu Python Casting

berikut penjelasan dari AI:

Berikut penjelasan lengkap dan mudah dipahami tentang **Python Casting** atau penentuan tipe variabel:

---

### **Apa itu Casting?**
Casting adalah proses mengubah tipe data suatu nilai menjadi tipe data lain secara eksplisit. Python menggunakan **constructor functions** (fungsi pembangun) seperti `int()`, `float()`, dan `str()` untuk melakukan ini. Hal ini diperlukan karena Python tidak mengubah tipe data secara otomatis (seperti JavaScript), sehingga kita harus melakukannya manual.

---

### **Kenapa Casting Dibutuhkan?**
- Saat menerima input pengguna (selalu dalam bentuk string), tetapi ingin diolah sebagai angka.
- Saat ingin menggabungkan angka dengan string (harus diubah ke string dulu).
- Saat memastikan perhitungan matematis menggunakan tipe data yang benar.

---

### **1. Casting ke Integer (`int()`)**
Mengubah nilai menjadi tipe data **integer** (bilangan bulat).

**Contoh:**
```python
x = int(1)    # 1 (dari integer → tetap 1)
y = int(2.8)  # 2 (dari float → dibulatkan ke bawah)
z = int("3")  # 3 (dari string angka)
```

**Aturan:**
- Jika sumbernya **float**, nilai akan dipotong/dihilangkan bagian desimalnya.
- Jika sumbernya **string**, isinya harus berupa angka bulat (contoh: `"5"`), bukan desimal atau teks.
  - ❌ Error: `int("3.5")` atau `int("lima")`.

---

### **2. Casting ke Float (`float()`)**
Mengubah nilai menjadi tipe data **float** (bilangan desimal).

**Contoh:**
```python
x = float(1)     # 1.0 (dari integer → ditambah .0)
y = float(2.8)   # 2.8 (dari float → tetap sama)
z = float("3")   # 3.0 (dari string angka bulat)
w = float("4.2") # 4.2 (dari string angka desimal)
```

**Aturan:**
- Jika sumbernya **integer**, nilai akan diubah ke desimal (ditambah `.0`).
- Jika sumbernya **string**, isinya harus berupa angka (bisa bulat atau desimal).
  - ❌ Error: `float("dua")`.

---

### **3. Casting ke String (`str()`)**
Mengubah nilai menjadi tipe data **string** (teks).

**Contoh:**
```python
x = str("s1")  # "s1" (dari string → tetap sama)
y = str(2)     # "2"  (dari integer → diubah ke teks)
z = str(3.0)   # "3.0" (dari float → diubah ke teks)
```

**Aturan:**
- Bisa digunakan pada semua tipe data, termasuk boolean.
- Berguna untuk menggabungkan angka dengan teks menggunakan `+`:
  ```python
  usia = 20
  print("Usia saya: " + str(usia))  # Output: Usia saya: 20
  ```

---

### **Contoh Kasus Error dan Solusi**
1. **Error karena string tidak valid:**
   ```python
   int("5a")  # ❌ ValueError: invalid literal for int()
   ```
   Solusi: Pastikan string hanya berisi angka.

2. **Casting bertahap:**  
   Jika ingin mengubah string desimal (`"3.5"`) ke integer:
   ```python
   nilai = float("3.5")  # Ubah ke float dulu → 3.5
   nilai_int = int(nilai) # Baru ke integer → 3
   ```

---

### **Ringkasan Fungsi Casting**
| Fungsi   | Contoh Input          | Hasil Output       | Keterangan                          |
|----------|-----------------------|--------------------|-------------------------------------|
| `int()`  | `int("10")`           | `10` (integer)     | String harus angka bulat            |
| `float()`| `float("7")`          | `7.0` (float)      | Bisa dari integer, float, atau string angka |
| `str()`  | `str(True)`           | `"True"` (string)  | Mengubah apa pun menjadi teks       |

---

### **Kapan Harus Casting?**
- Saat membaca input pengguna dengan `input()` (selalu string).
- Saat melakukan operasi matematika yang membutuhkan tipe data tertentu.
- Saat menyiapkan data untuk ditampilkan dalam bentuk teks.

Dengan memahami casting, Anda bisa lebih fleksibel mengontrol tipe data dalam program Python! 🐍




#Apakah casting dalam Python dapat dilakukan di semua tipe data? atau hanya int, float, dan str?

Berikut penjelasan lengkapnya:

---

### **Casting di Python Tidak Hanya untuk int, float, dan str!**
Python memungkinkan casting ke **berbagai tipe data**, tetapi **tergantung kompatibilitas data sumber** dan **konstruktor yang tersedia**. Selain `int()`, `float()`, dan `str()`, ada banyak tipe data lain yang bisa di-cast, seperti `list`, `tuple`, `bool`, `set`, `dict`, dan bahkan tipe data kustom.

---

### **Contoh Casting ke Tipe Data Lain**

#### 1. **Casting ke Boolean (`bool()`)**
Mengubah nilai menjadi `True` atau `False`.
```python
a = bool(0)      # False (angka 0 → False)
b = bool(3)      # True (angka non-0 → True)
c = bool("")     # False (string kosong → False)
d = bool("Hi")   # True (string tidak kosong → True)
e = bool([])     # False (list kosong → False)
```

#### 2. **Casting ke List (`list()`)**
Mengubah iterable (seperti string, tuple, atau set) menjadi list.
```python
x = list("halo")      # ['h', 'a', 'l', 'o']
y = list((1, 2, 3))   # [1, 2, 3]
z = list({4, 5, 6})   # [4, 5, 6] (urutan bisa berubah karena set)
```

#### 3. **Casting ke Tuple (`tuple()`)**
Mengubah iterable menjadi tuple.
```python
x = tuple([1, 2, 3])   # (1, 2, 3)
y = tuple("abc")       # ('a', 'b', 'c')
```

#### 4. **Casting ke Set (`set()`)**
Mengubah iterable menjadi set (unik dan tidak berurut).
```python
x = set([1, 2, 2, 3])  # {1, 2, 3}
y = set("hello")       # {'h', 'e', 'l', 'o'}
```

#### 5. **Casting ke Dictionary (`dict()`)**
Mengubah pasangan key-value (seperti list of tuples) menjadi dictionary.
```python
x = dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}
```

---

### **Batasan dan Error yang Umum**
Tidak semua casting bisa dilakukan. **Konversi harus masuk akal** secara logika, atau Python akan menampilkan `TypeError`/`ValueError`.

**Contoh Error:**
```python
int("3.14")       # ❌ ValueError (bukan bilangan bulat)
list(123)         # ❌ TypeError (integer tidak bisa di-iterasi)
dict("hello")     # ❌ ValueError (string tidak berisi pasangan key-value)
```

**Solusi untuk Kasus Sulit:**
- Jika ingin mengubah integer ke list, konversi ke string dulu:
  ```python
  angka = 123
  list_angka = list(str(angka))  # ['1', '2', '3']
  ```

---

### **Tabel Ringkasan Casting di Python**
| Fungsi     | Contoh Input           | Hasil Output           | Syarat                     |
|------------|------------------------|------------------------|----------------------------|
| `int()`    | `int("42")`            | `42` (integer)         | String harus angka bulat   |
| `float()`  | `float([3])`           | ❌ Error               | Tidak bisa dari list       |
| `str()`    | `str([1, 2, 3])`       | `"[1, 2, 3]"` (string) | Selalu berhasil            |
| `bool()`   | `bool("False")`        | `True`                 | String tidak kosong → True |
| `list()`   | `list({"a": 1})`       | `['a']`                | Ambil keys dari dictionary |
| `tuple()`  | `tuple({1, 2, 3})`     | `(1, 2, 3)`            | Iterable                   |
| `set()`    | `set([1, 1, 2])`       | `{1, 2}`               | Hapus duplikat             |
| `dict()`   | `dict([(1, "a")])`     | `{1: 'a'}`             | Input harus pasangan key-value |

---

### **Kesimpulan**
- **Casting bisa dilakukan ke hampir semua tipe data**, selama ada konstruktor yang sesuai dan data sumber kompatibel.
- **Tipe data primitif** (`int`, `float`, `str`, `bool`) paling sering digunakan.
- **Tipe data koleksi** (seperti `list`, `dict`) memerlukan input yang bisa di-iterasi atau sesuai struktur.
- **Tidak semua konversi masuk akal**, jadi pastikan data sumber valid untuk menghindari error.

Dengan memahami ini, Anda bisa lebih fleksibel memanipulasi tipe data di Python! 🚀