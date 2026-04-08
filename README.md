## 📖 About this Project
This project aims to automate the sentiment analysis process for Instagram comments, making it easier to monitor public opinion and accurately identify audience emotions. The application utilizes Selenium and machine learning to scrape data from social media, and applies **Support Vector Machine (SVM)** for the text classification process.

## 📂 Directory Structure
```bash
instasent/
├── backbone/                          # Folder utama Backend
│   ├── app/                           # Modul aplikasi 
│   │   ├── routes/                    # Endpoint API (routing)
│   │   ├── schemas/                   # Data Transfer Objects / Pydantic models
│   │   ├── services/                  # Logika utama (scraper, analyzer, inference)
│   │   └── main.py                    # Entry point utama aplikasi FastAPI
│   ├── core/                          # Text preprocessing
│   ├── data/                          # Dataset latih dan tes
│   ├── model/                         # Penyimpanan model Machine Learning
│   ├── notebooks/                     # Eksperimen data dan training model
│   ├── .gitignore                     
│   └── scraper.txt                    
├── frontliner/                        # Folder utama Frontend 
│   ├── assets/                        # File statis pendukung
│   └── index.html                     # Halaman utama antarmuka pengguna (UI)
├── README.md                          # Dokumentasi utama proyek
└── requirements.txt                   # Daftar dependensi Python yang diperlukan
```
