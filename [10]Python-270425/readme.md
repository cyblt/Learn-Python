PYTHON STRING

Chapter ini menjelaskan tentang String di Python

Berikut penjelasan dari AI:

Berikut penjelasan lengkap dan mudah dipahami tentang **Python Strings**:

---

### **Apa Itu String?**
String adalah tipe data yang digunakan untuk menyimpan teks. Di Python, string ditulis dengan diapit **tanda kutip tunggal** (`' '`) atau **ganda** (`" "`).  
Contoh:  
```python
nama = 'Budi'
alamat = "Jakarta"
```

---

### **Aturan Dasar String**
1. **Tanda Kutip Harus Sesuai Pasangan**  
   Jika string diawali kutip tunggal, harus ditutup kutip tunggal, dan sebaliknya.  
   ❌ Salah: `"Hello'`  
   ✅ Benar: `'Hello'` atau `"Hello"`.

2. **Kutip di Dalam String**  
   Gunakan kutip berbeda untuk teks yang mengandung kutip:  
   ```python
   print("It's raining!")      # Output: It's raining!
   print('Dia berkata, "Halo!"')  # Output: Dia berkata, "Halo!"
   ```

---

### **String Multiline (Teks Berbanyak Baris)**
Gunakan **tiga kutip** (tunggal `'''` atau ganda `"""`) untuk membuat string yang mencakup beberapa baris.  
Contoh:  
```python
puisi = """Hai bulan,
Kau bersinar terang,
Di langit malam."""
print(puisi)
```
Output:  
```
Hai bulan,
Kau bersinar terang,
Di langit malam.
```

---

### **String Sebagai Array**
String di Python mirip **array karakter**, di mana setiap karakter memiliki indeks (dimulai dari 0).  

#### **Mengakses Karakter**  
Gunakan **kurung siku** `[]` untuk mengambil karakter berdasarkan indeks:  
```python
kata = "Python"
print(kata[0])  # Output: P
print(kata[3])  # Output: h
```

#### **Looping melalui String**  
Gunakan perulangan `for` untuk mengakses setiap karakter:  
```python
for huruf in "Python":
    print(huruf)
```
Output:  
```
P
y
t
h
o
n
```

---

### **Fungsi `len()` untuk Panjang String**
Gunakan `len()` untuk mengetahui jumlah karakter dalam string:  
```python
kata = "Hello, World!"
print(len(kata))  # Output: 13
```

---

### **Memeriksa Substring dengan `in` dan `not in`**
1. **`in`**: Mengecek apakah suatu kata/karakter ada dalam string.  
2. **`not in`**: Mengecek apakah suatu kata/karakter **tidak** ada dalam string.  

#### Contoh:
```python
teks = "Hidup itu sederhana jika tidak dipersulit."

# Cek apakah "sederhana" ada di teks
print("sederhana" in teks)  # Output: True

# Cek apakah "rumit" tidak ada di teks
print("rumit" not in teks)  # Output: True
```

#### **Penggunaan dalam `if` Statement**  
```python
teks = "Belajar Python itu menyenangkan."

if "Python" in teks:
    print("Terdapat kata 'Python'!")  # Akan dieksekusi

if "Java" not in teks:
    print("Tidak ada kata 'Java'!")   # Akan dieksekusi
```

---

### **Tabel Perbandingan Operasi String**
| Operasi               | Contoh Kode                     | Hasil          | Keterangan                     |
|-----------------------|---------------------------------|----------------|--------------------------------|
| Akses karakter        | `"Python"[2]`                  | `'t'`          | Indeks dimulai dari 0          |
| Panjang string        | `len("Hello")`                 | `5`            | Jumlah karakter                |
| Cek substring         | `"free" in "life is free"`     | `True`         | Case-sensitive                 |
| Cek tidak ada substring | `"mahal" not in "free"`        | `True`         |                                |

---

### **Penting untuk Diingat!**
1. **String Tidak Bisa Diubah (Immutable)**  
   Setelah string dibuat, isinya tidak bisa diubah.  
   Contoh:  
   ```python
   kata = "Python"
   kata[0] = "J"  # ❌ Error: 'str' object does not support item assignment
   ```

2. **Case-Sensitive**  
   Python membedakan huruf besar dan kecil:  
   ```python
   print("Budi" == "budi")  # Output: False
   ```

---

### **Contoh Kasus Nyata**
1. **Membuat Pesan yang Dinamis**  
   ```python
   nama = "Andi"
   umur = 20
   pesan = f"Nama: {nama}, Umur: {umur} tahun"
   print(pesan)  # Output: Nama: Andi, Umur: 20 tahun
   ```

2. **Validasi Input Pengguna**  
   ```python
   email = input("Masukkan email: ")
   if "@" not in email:
       print("Email tidak valid!")
   ```

---

### **Kesimpulan**
- String adalah tipe data teks yang fleksibel di Python.
- Bisa dibuat dengan kutip tunggal, ganda, atau tiga kutip untuk teks panjang.
- Operasi seperti akses karakter, perulangan, dan pengecekan substring sangat mudah dilakukan.

Dengan memahami konsep ini, Anda bisa mulai membangun program yang memproses teks, seperti validasi data atau pembuatan laporan! 🚀