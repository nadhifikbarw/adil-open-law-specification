# Adil Open Law Specification

Adil Open Law Specification merupakan upaya untuk mendefinisikan spesifikasi terbuka representasi dokumen digital produk legislasif di Indonesia.

Spesifikasi ini mengedepankan representasi yang menggunakan format file terbuka yang berbasis plaintext, pada repository ini bentuk format file yang digunakan untuk menyimpan konten produk legislatif memanfaatkan sintaks HTML, namun untuk pengembangan kedepan tidak membatasi format file yang digunakan.

Dengan mengubah cara menyimpan dan membagikan produk legislatif ini menggunakan format file yang lebih terbuka diharapkan bentuk representasi ini menyediakan dokumen yang lebih terstruktur, mudah diakses, untuk diproses menggunakan teknik komputasi lebih lanjut.

Spesifikasi ini juga mengedepankan struktur dokumen dengan tingkat kedetailan segranular mungkin untuk mendukung sifat referenceable baik ke untuk seluruh atau sebagian dari suatu dokumen.

Spesifikasi ini berfokus pada data dan konten produk legislatif sehingga pendekatannya bersifat stlye-agnostic yang berarti representasi dari dokumen tidak disarankan untuk mengandung informasi mengenai bagaimana dokumen tersebut harus ditampilkan / distyling.

File `UUD1945_SatuNaskah.html` merupakan contoh penerapan spesifikasi ini untuk dokumen legislatif UUD 1945 dengan ,menggunakan sintaks HTML.

## Spesifikasi

* Satu dokumen legislasi harus direpresentasikan pada satu file dengan menggunakan format file yang terbuka, berbasi plaintext, dan mendukung struktur / hirarki dokumen.

* Apabila terdapat variasi dari satu dokumen legislasi yang sama, misal: UUD 1945 Satu Naskah dan UUD 1945 Amandemen Terbaru maka kedua kedua lagislasi tersebut harus direpresentasikan pada dua file yang terpisah.

### Struktur Dokumen HTML
* Setiap dokumen wajib memiliki hanya satu tag `<html>`.
* `<html>` tag tersebut wajib memiliki masing-masing satu node bertipe `<head>` dan `<body>`.
* Selanjutnya Node `<head>` akan disebut dengan Kepala Dokumen dan Node `<body>` akan disebut dengan Isi Dokumen
* Berikut adalah stuktur umum dari suatu dokumen:

```html
<html>
    <!-- Kepala Dokumen -->
    <head>
        <title>Document Title</title>
        <meta name="metadata_1" content="Metadata 1">
        <meta name="metadata_2" content="Metadata 2">
        <meta name="metadata_3" content="Metadata 3">
    </head>
    <!-- Badan Dokumen -->
    <body>
        <!-- Konten Dokumen -->
        <article>
            <section>
            </section>
        </article>
    </body>
</html>
```

### Struktur Kepala Dokumen
* Kepala Dokumen hanya dibolehkan berisi 2 tipe node sebagai anak node yaitu `<title>` serta `<meta>`.
* Satu Node `<meta>` merepresentasikan satu metadata dokumen terkait.

### Struktur Badan Dokumen
* Setiap dokumen wajib memiliki satu node `<article>` yang disebut dengan Konten Dokumen dan tidak memiliki node lain sebagai anak dari Badan Dokumen.
* Konten Dokumen berisi sekumpulan Section Dokumen yang mendefinisikan struktur dari dokumen menggunakan Node `<section>`
* Untuk konten dokumen yang berupa judul direpresentasikan menggunakan Node `<h1>`-`<h6>` dan paragraf / ayat / penjelasan menggunakan Node `<p>`, Node node ini disebut dengan Block Node
* Section Dokumen dapat memiliki anak Node `<section>` untuk mendefinisikan subsection dari section tersebut.
* Setiap Section Dokumen wajib memiliki judul untuk section tersebut yang direpresentasikan menggunakan Node `<h1>`


### Metadata dan Attirbute Node
* Setiap Node `<section>` wajib memiliki atribut `data-section-type`.
* Setiap Block Node di dalam Konten Dokumen wajib memiliki atribut `data-block-type`.
* Seluruh node `<article>`, `<section>`, dan Block Node wajib memiliki atribut `data-identifier`.

## Latar Belakang

Upaya ini berangkat dari konsep [5-Star Open Data](https://5stardata.info/en/) yang dicetuskan oleh Tim Berners-Lee untuk mengkategorikan tingkat keterbukaan format sebuah data.

Faktanya, format data yang paling umum digunakan untuk membagikan dokumen legislasi adalah PDF atau DOC(X). Format ini digunakan karena dirasa paling mudah dan familiar bagi masyarakat umum, namun tingkat fleksibilitas dari format ini sulitu untuk melakukan pemrosesan komputasi lebih lanjut. Oleh karena itu PDF sendiri merupakan format file 1-star.

Dengan mengubah representasi tersebut menjadi format plaintext dan memanfaatkan markup HTML/XML diharapkan dapat mempermudah

## Kontribusi

Inisiatif ini masih sangat awam dan perlu banyak pengembangan lebih lanjut. Kontribusi dari berbagai dimensi baik dari segi dokumentasi, koreksi tata bahasa, pengembangan spesifikasi, pemecahan konflik, aspek kehukuman, dan lain-lain sangat diharapkan.

## Referensi Terkait

[1] Indrati, Maria Farida, and Maria Farida. "Ilmu Perundang-Undangan, Proses dan Teknik Pembentukannya." Yogyakarta: Kanisius (2017).


