# stocks_news_crawler


Masalah yang ingin diselesaikan:

Sulitnya mendapatkan informasi saham yang terkumpul dalam satu file tanpa perlu loading halamn website

Walaupun website berita sudah memisahkan berita ekonomi dengan berita kategori lain , tapi belum ada yang membedakan berita penting untuk pergerakan saham dan berita yang sama sekali tidak penting , misal berita tidak penting untuk pergerakan saham :

    https://finance.detik.com/berita-ekonomi-bisnis/d-4710234/sri-mulyani-menyesal-tak-bertemu-robot-sophia
    https://finance.detik.com/berita-ekonomi-bisnis/d-4710568/suap-demi-keterima-jadi-pns-sudah-dianggap-wajar

contoh berita penting:

    https://finance.detik.com/industri/d-4710515/menperin-usul-kakao-dibebaskan-dari-ppn (kemungkinan berpengaruh ke harga saham perusahaan perkebunan)
    https://finance.detik.com/energi/d-4709711/seputar-saudi-aramco-perusahaan-yang-ladang-minyaknya-diserang (kemungkinan berpengaruh terhadap saham perminyakan karena harga minyak terpengaruh)

Tujuan program bisa menjelajahi website -website berita seperti detik.com . beritasatu.com dsb dan bisa HANYA mengambil informasi yang berkaitan dengan saham , sehingga berita yang sama sekali tidak penting untuk pergerakan saham, tidak akan disimpan

Tahap 1 - membuat crawler dan scrapper menyimpan semua berita

Tahap 2 - membuat dataset untuk klasifikasi "penting" dan "tidak penting"

Tahap 3 - menggunakan model klasifikasi untuk menentukan apakah berita "penting" atau "tidak penting" untuk pergerakan saham

output yang dihasilkan adalah file csv berisi berita penting untuk pergerakan saham

