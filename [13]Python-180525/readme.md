# Chapter Python - String Concatenation

## Berikut adalah penjelasan dari AI:

## Daftar Isi
- [Apa Itu String Concatenation](#apa-itu-string-concatenation)
- [Contoh Dasar](#contoh-dasar-penggabungan-string)
- [Cara Kerja Operator +](#cara-kerja-operator-)

Berikut penjelasan lengkap dan mudah dipahami tentang **String Concatenation (Penggabungan String)** di Python:

---

### **Apa Itu String Concatenation?**
String Concatenation adalah proses menggabungkan dua atau lebih string menjadi satu string utuh. Di Python, kita menggunakan operator `+` untuk melakukan ini.

---

### **Contoh Dasar Penggabungan String**
#### **1. Menggabungkan Dua String Tanpa Spasi**
```python
a = "Hello"
b = "World"
c = a + b
print(c)  # Output: HelloWorld
```

#### **2. Menambahkan Spasi Antara String**
Untuk menyisipkan spasi atau karakter lain, tambahkan string spasi (`" "`) di antara keduanya:
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Output: Hello World
```

---

### **Cara Kerja Operator `+`**
- Operator `+` bertindak seperti **lem** yang menyambungkan string.
- Urutan penulisan memengaruhi hasil:
  ```python
  print("A" + "B")  # Output: AB
  print("B" + "A")  # Output: BA
  ```

---

### **Contoh Lain Penggunaan Concatenation**
#### **1. Gabungkan String Langsung (Tanpa Variabel)**
```python
nama_depan = "John"
nama_lengkap = nama_depan + " Doe"
print(nama_lengkap)  # Output: John Doe
```

#### **2. Gabungkan dengan Angka (Harus Diubah ke String)**
```python
umur = 20
# print("Umur: " + umur)  # ❌ Error (karena umur bertipe integer)
print("Umur: " + str(umur))  # ✅ Output: Umur: 20
```

---

### **Tabel Ilustrasi Concatenation**
| Kode                     | Output           | Penjelasan                          |
|--------------------------|------------------|-------------------------------------|
| `"Py" + "thon"`          | `"Python"`       | Gabungkan 2 string                 |
| `"Hi" + "!" * 3`         | `"Hi!!!"`        | Gabungkan dengan operator `*`      |
| `"A" + " " + "B" + "C"` | `"A BC"`         | Multiple concatenation             |

---

### **Penting untuk Diingat!**
1. **String Bersifat Immutable**  
   Setiap operasi concatenation menghasilkan **string baru**.  
   Contoh:  
   ```python
   a = "Hello"
   a = a + " World!"  # Membuat string baru, bukan mengubah a
   ```

2. **Hanya untuk Tipe Data String**  
   Jika ingin menggabungkan string dengan tipe data lain (seperti integer), harus diubah ke string terlebih dahulu dengan `str()`:  
   ```python
   print("Hari ke-" + str(3))  # Output: Hari ke-3
   ```

3. **Alternatif Concatenation**  
   Untuk menggabungkan banyak string, bisa menggunakan **f-string** (format string) yang lebih fleksibel:  
   ```python
   nama = "Andi"
   umur = 20
   print(f"{nama} berusia {umur} tahun")  # Output: Andi berusia 20 tahun
   ```

---

### **Kapan Harus Menggunakan Concatenation?**
- Saat membangun pesan dinamis dari beberapa variabel.
- Saat mengolah data teks dari sumber berbeda.
- Untuk menghasilkan output yang terformat rapi.

---

### **Contoh Kasus Nyata**
1. **Membuat URL dari Komponen**  
   ```python
   domain = "https://example.com"
   endpoint = "/api/data"
   url = domain + endpoint
   print(url)  # Output: https://example.com/api/data
   ```

2. **Menyusun Kalimat dari Input Pengguna**  
   ```python
   nama = input("Nama: ")
   pekerjaan = input("Pekerjaan: ")
   bio = nama + " adalah seorang " + pekerjaan
   print(bio)
   ```

---

### **Kesimpulan**
- Operator `+` adalah cara termudah untuk menggabungkan string.
- Selalu pastikan semua komponen bertipe string sebelum digabungkan.
- Untuk kasus kompleks, pertimbangkan menggunakan **f-string** atau `join()`.

Dengan menguasai concatenation, Anda bisa membuat teks dinamis dengan mudah! 🐍✨