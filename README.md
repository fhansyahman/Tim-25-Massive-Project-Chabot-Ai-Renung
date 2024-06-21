<h1 align="center">  Chatbot Ruang Damai</h1>

<p align="center"> 
Berikut library yang digunakan dalam pembuatan chatbot
</p>

<div align="center">
    <!-- Your badges here -->
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
    <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white">
    <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white">
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white">
    <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB">
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">

</div>

## Teams

- Kheisa Gading (Scrum Master/
Design Researcher)
- Putri Riani Setyo Wulandari (Data Engineer)
- Ardian Fikri Abdulah (Machine Learning Engineer)
- Farhan Firmansyah (Machine Learning Ops)

## Idea Background

### 1. Theme
Tema : Kesahatan Mental

### 2. Problem
Masalah : Mengatasi hambatan
aksesibilitas dan keterjangkauan dalam perawatan
kesehatan mental

### 3. Solution
Solusi : Membuat chat bot untuk
konseling, terapi melalui video, dukungan berupa
webinar, serta informasi bermanfaat melalui artikelartikel..

## Dataset and Algorithm

### 1. Dataset
- Data Collection <br />
Kami menemukan data kami di Kaggle.
Link Kaggle (Mental Health Conversational Data & Mental Health FAQ for Chatbot):
https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot <br />
https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data
- Data Cleaning <br />
Kami menggunakan pandas untuk membersihkan data. Berikut tabel contoh data yang belum dibersihkan dan yang sudah: <br />
Sebelum:

Sesudah:

Pada dataset sendiri disini dilakukan penerjemahan kemudian dua data yang berbada tersebut digabung menjadi satu data

### 2. Algorithm

- Framework <br />
Dalam pengembangan sistem chatbot ruang damai untuk kesehatan mental,
kami memilih untuk menggunakan TensorFlow, Keras (yang terintegrasi dengan
TensorFlow), dan Scikit-Learn sebagai framework utama untuk implementasi AI

- Pembangunan Model <br />
EPOCHS=50 dan BATCH_SIZE=32 diatur untuk pelatihan model, yang dilatih dengan model.fit(X, y_encoded, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_data=(X, y_encoded)). Model disimpan sebagai 'my_model_NLP.h5', tokenizer disimpan dalam 'tokenizer.json', dan label encoder disimpan dalam 'label_encoder.json'. Output pelatihan: 8 batch, 106ms per langkah, training loss 0.5214, accuracy 0.8902, validation loss 0.4939, accuracy 0.9106.

- Model Evaluation <br />
Berdasarkan hasil evaluasi model, model menunjukkan performa yang cukup
baik, dengan loss pelatihan sebesar 0.5214, akurasi pelatihan 0.8902, loss validasi
0.4939, dan akurasi validasi 0.9106. Waktu pelatihan per langkah sekitar 106ms,
menunjukkan bahwa model tidak terlalu kompleks. 

## Prototype


1.Data Collection (Pengumpulan Data)<br />
Dari data sendiri Kami menemukan data kami di Kaggle.
Link Kaggle (Mental Health Conversational Data & Mental Health FAQ for Chatbot):<br />
https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot<br />
https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data

2. Building Model (Membangun Model)<br />
Model AI yang kami kembangkan untuk chatbot ruang damai dalam
kesehatan mental menggunakan arsitektur LSTM (Long Short-Term Memory).
LSTM dipilih karena kemampuannya untuk mengelola dan memahami pola
dalam data berurutan seperti teks percakapan, yang sangat relevan dalam
konteks interaksi pengguna dengan chatbot terkait kesehatan mental.

3. Data Cleaning and Augmentation (Pembersihan dan Augmentasi
Data)<br />
Dari data disini telah dilakukan pembersihan di awal sehingga selanjutnya
ke tahap load data

5. Data Splitting (Pemecahan Data)<br />
langkah pertama adalah memisahkan data menjadi data
latih dan data uji menggunakan fungsi train_test_split dengan proporsi 80% untuk
pelatihan dan 20% untuk pengujian

6. Pre-Proccesing Data (Pra-Pemrosesan Data)<br />
Pada preprocessing data tersebut, pertama-tama data dari kolom 'intents' diambil
dan dipisahkan menjadi dua list, yaitu 'X' untuk pola (patterns) dan 'y' untuk respons
(responses). 

7. Model Training (Pelatihan Model)<br />
Pada tahap ini, pertama-tama diatur hyperparameters EPOCHS = 50 dan
BATCH_SIZE = 32 untuk menentukan jumlah epoch dan ukuran batch selama pelatihan
model. Model dilatih menggunakan model.fit(X, y_encoded, epochs=EPOCHS,
batch_size=BATCH_SIZE, validation_data=(X, y_encoded)), di mana data X dan label
y_encoded digunakan untuk pelatihan dan validasi. Setelah pelatihan selesai, model
disimpan dalam format HDF5 dengan nama my_model_NLP.h5 menggunakan
model.save('my_model_NLP.h5'). S

8. Model Evaluation (Evaluasi Model)<br />
Pada tahap ini dilakukan untuk mengevaluasi model yang telah dilatih
sebelumnya agar mengetahui akurasi dan lossnya.

9. Model Prediction (Prediksi Model)<br />
MPada tahap ini, teks masukan diproses oleh model deep learning yang dimuat dari 'content/my_model_NLP.h5', menggunakan tokenizer untuk pra-pemrosesan, memprediksi niat dengan probabilitas tertinggi, memetakan indeks ke label niat dengan label_encoder, dan mengembalikan label niat untuk aplikasi seperti chatbot, asisten virtual, dan sistem rekomendasi.


## Integration
integrasi AI dalam proyek chatbot untuk kesehatan mental melibatkan
beberapa tahap, mulai dari pembuatan model hingga deployment dan
integrasi ke tampilan web.

1.Pembuatan Model dengan Google Collab<br />
○ Pengumpulan Data: Langkah pertama adalah mengumpulkan
data yang relevan untuk melatih model AI. 
○ Pelatihan Model: Menggunakan Google Collab, yang
menyediakan lingkungan pemrograman berbasis cloud dengan akses
ke GPU untuk pelatihan model yang lebih cepat. 
○ Evaluasi dan Validasi: Setelah model dilatih, langkah
berikutnya adalah mengevaluasi kinerjanya menggunakan data uji.

2. Deployment dengan Docker Hub dan Code Engine<br />
○ Dockerization: Setelah model siap, kita mengemasnya ke
dalam sebuah container menggunakan Docker.
○ Push ke Docker Hub: Docker image yang sudah dibuat
kemudian di-push ke Docker Hub, yang merupakan repository untuk
menyimpan dan mendistribusikan Docker images.
○ Code Engine Deployment: Menggunakan IBM Cloud Code
Engine atau platform serupa untuk mendeploy Docker container ke
dalam lingkungan produksi. 

3. Integrasi ke Tampilan Web:<br />
○ Pengembangan Frontend: Membangun antarmuka pengguna
(UI) untuk chatbot di web. 
○ Integrasi Endpoint: Menghubungkan frontend dengan
endpoint AI yang dihasilkan oleh Code Engine.
○ Testing dan Iterasi: Menguji integrasi secara menyeluruh
untuk memastikan bahwa chatbot berfungsi dengan baik di antarmuka

## Deployment
Pada bagian ini, untuk platform yang digunakan untuk memberikan akses model
AI melalui proses deployment, yang melibatkan Docker Hub dan Code Engine untuk
menghasilkan endpoint API yang dapat diakses oleh aplikasi web.


## Result
1. AI model performance metrics<br />
Gambar tersebut menunjukkan metrik kinerja model AI selama pelatihan dan
validasi. Model dilatih selama 50 epoch dengan 8 batch per epoch. Selama proses
pelatihan, nilai "loss" terus menurun dari sekitar 0.8293 di epoch 42 hingga 0.5105 di
epoch 50, menandakan bahwa model semakin baik dalam memprediksi data pelatihan.
Akurasi pelatihan berkisar antara 0.8821 hingga 0.8943, menunjukkan model memiliki
tingkat prediksi yang cukup konsisten. Nilai "val_loss" (kerugian validasi) juga
menurun dari 0.7777 menjadi 0.4812, menunjukkan peningkatan performa model
terhadap data yang belum pernah dilihat sebelumnya. Akurasi validasi tetap stabil
pada nilai 0.9106 setelah epoch 41, menandakan model memiliki generalisasi yang
baik dan tidak terjadi overfitting.

2. Visualization of result data<br />
Pada visualisasi diatas menunjukkan tren dan pola yang signifikan, di mana
model memiliki performa yang cukup baik dengan loss pelatihan sebesar 0.5214 dan
akurasi pelatihan 0.8902, serta loss validasi 0.4939 dan akurasi validasi 0.9106.
Waktu pelatihan per langkah sekitar 106ms menunjukkan bahwa model tidak terlalu
kompleks. Namun, terdapat indikasi overfitting karena akurasi validasi lebih tinggi
dibandingkan akurasi pelatihan.

3. Achievement of project goals<br />
Proyek kami telah selesai pada tahap akhir yaitu deployment. Saat ini, model
tersebut berhasil di-deploy dan diintegrasikan ke dalam tampilan web. Sebelumnya,
kami menghadapi beberapa kendala seperti endpoint yang tiba tiba mati. Meskipun
demikian, masalah tersebut telah teratasi dan penggunaan chatbot yang
diintegrasikan telah bisa digunakan sesuai harapan, meskipun masih perlu beberapa
perbaikan.

4. Limitations and challenges faced<br />
A. Kendala waktu : waktu yang diberikan cukup terbatas
B. Kendala sumber daya : Sumber Daya Manusia yang kurang anak IT dan
keterbatasan penggunaan collab dan ibm cloud.
C. Kendala teknis : Kesulitan mencari dataset yang sesuai dan berbahasa indonesia
serta beberapa tahapan tidak berjalan namun dapat di handle dengan yang lain.

## Conclusion
1. Summary of important points
A. Proyek ini bertujuan untuk membantu individu mengatasi gangguan
kesehatan mental dan beberapa gejala terkait.
B. Dari berbagai model yang telah kami kembangkan, model ini dianggap lebih
unggul karena memiliki tingkat akurasi dan presisi yang cukup tinggi.
C. Tantangan yang kami hadapi dalam proyek ini mencakup keterbatasan waktu,
sumber daya yang terbatas, serta beberapa kendala teknis yang perlu diatasi.

2. Contribution to science and technology<br />
Proyek kami, sebuah platform untuk kesehatan mental, memberikan
kontribusi dalam pengembangan ilmu pengetahuan dan teknologi dengan cara
menyediakan akses terhadap informasi terbaru seputar kesehatan mental. Lebih dari
sekadar itu, kami juga menghadirkan sebuah platform interaktif yang membantu
pengguna untuk mengelola dan memahami kondisi kesehatan mental mereka dengan
lebih baik.

3. Future project development plans<br />
A. Kami berencana untuk menambahkan fitur-fitur baru ke proyek ini, seperti
input voice dan output voice.
B. Kami juga ingin proyek ini bisa digunakan di ponsel.
C. Selain itu, kami akan terus memperbarui data kami sesuai dengan
perkembangan dunia nyata, untuk meningkatkan keakuratan dan efektivitas
proyek ini.
