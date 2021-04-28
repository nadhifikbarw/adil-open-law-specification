# Adil Open Law Specification

Adil Open Law Specification merupakan upaya untuk mendefinisikan spesifikasi terbuka dari representasi dokumen digital perundang-undangan Indonesia.

Spesifikasi ini mengedepankan representasi peraturan perundang-undangan yang berbasis plaintext dengan pemanfaatan markup HTML yang diharapkan dapat menjadi bentuk representasi yang terstruktur, mudah diakses, dan mudah diproses menggunakan teknik komputasi lebih lanjut.

Spesifikasi ini juga mengedepankan struktur representasi dokumen dengan tingkat kedetailan segranular mungkin untuk mendukung sifat referenceable baik ke seluruh atau sebagian dari suatu dokumen.

Spesifikasi ini berfokus pada data dan bersifat stlye-agnostic yang berarti bahwa representasi dari dokumen tidak boleh mengandung informasi mengenai bagaimana dokumen tersebut harus ditampilkan.

File `uud1945.html` merupakan contoh penerapan spesifikasi pada format HTML

## Spesifikasi
* Satu dokumen legislasi direpresentasikan pada satu file dengan format tertentu

### Spesifikasi Khusus (HTML)

#### Struktur Dokumen
* Setiap dokumen wajib memiliki hanya satu tag `<html>`.
* `<html>` tag tersebut wajib memiliki masing-masing satu node bertipe `<head>` dan `<body>`.

#### `<head>` Node
* Node `<head>` hanya dibolehkan memiliki 2 tipe node sebagai anak node yaitu `<title>` serta `<meta>`.
* `<meta>` digunakan mencatat metadata dari dokumen terkait.

#### `<body>` Node
* Setiap dokumen wajib memiliki satu node `<article>` dan tidak memiliki node lain sebagai anak node `<body>`.
* Setiap node `<section>` wajib memiliki atribut `data-section-type`.
* Setiap anak node `<section>` pada `<article>` wajib memiliki satu node dengan atribut `data-block-type`.
* Semua node `<article>`, `<section>`, dan, block node wajib memiliki atribut `data-identifier`.

## Latar Belakang

Upaya ini berangkat dari konsep [5-Star Open Data](https://5stardata.info/en/) yang dicetuskan oleh Tim Berners-Lee untuk mengkategorikan tingkat keterbukaan format sebuah data.

Faktanya, format data yang paling umum digunakan untuk membagikan dokumen digital peraturan perundang-undangan adalah PDF atau DOC(X). Format ini digunakan karena dirasa paling mudah dan familiar bagi masyarakat umum, namun tingkat fleksibilitas dari format ini justru dapat menimbulkan masalah untuk melakukan pemrosesan komputasi lebih lanjut. Oleh karena itu PDF sendiri merupakan format file 1-star.

Dengan mengubah representasi tersebut menjadi format plaintext dan memanfaatkan markup HTML/XML diharapkan dapat mempermudah

## Kontribusi

Inisiatif ini masih sangat awam dan perlu banyak pengembangan lebih lanjut. Kontribusi dari berbagai dimensi baik dari segi dokumentasi, koreksi tata bahasa, pengembangan spesifikasi, pemecahan konflik, aspek kehukuman, dan lain-lain sangat diharapkan.

## Referensi Terkait

[1] Indrati, Maria Farida, and Maria Farida. "Ilmu Perundang-Undangan, Proses dan Teknik Pembentukannya." Yogyakarta: Kanisius (2007).


