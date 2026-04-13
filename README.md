## 📖 About this Project
This project aims to automate the sentiment analysis process for Instagram comments, making it easier to monitor public opinion and accurately identify audience emotions. The application utilizes Selenium to scrape data from social media, and applies **Support Vector Machine (SVM)** for the text classification process.

## 🛠️ Technologies Used
This project is built with a modern full-stack architecture that decouples the frontend and backend, while integrating machine learning models for data processing and analysis.

### Frontend
![Vue.js](https://img.shields.io/badge/Vue.js%203-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white) ![Axios](https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white) ![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white) ![SweetAlert2](https://img.shields.io/badge/SweetAlert2-8A2BE2?style=for-the-badge)

* **Framework:** Vue.js 3 (Options API)
* **Language:** JavaScript
* **Styling:** Tailwind CSS
* **Data Visualization:** Chart.js (Sentiment distribution charts)
* **Data Fetching:** Axios (Backend REST API communication)
* **Notifications:** SweetAlert2 (Interactive UI alerts and loading states)

---

### Backend & Machine Learning
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Python](https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

* **Framework:** FastAPI (Python)
* **Language:** Python 3.12+
* **Machine Learning:** Scikit-Learn (Support Vector Machine algorithms)
* **Data Scraping:** Selenium (Instagram comment extraction automation)
* **Data Processing:** Pandas & Openpyxl (DataFrame manipulation and Excel exporting)

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

## 💻 Installation and Usage
**1. Clone the Repository:**
```bash
git clone https://github.com/ardywrks10/instasent-web-app.git
```
**2. Create Virtual Environment**
```bash
python -m venv my_env
source my_env/bin/active # di Windows, gunakan my_env\Scripts\activate
```
**3. Install Depedencies:**
```bash
pip install -r requirements.txt
```
**4. Make .env to connect to database client**
```bash
cd backbone
cp .env.example .env
```
**5. Fill .env value**
```bash
INSTAGRAM_USERNAME =
INSTAGRAM_PASSWORD =

DEFAULT_MAX_SCROLL = 30 # recommended
```
**6. Run the Uvicorn Server**
```bash
uvicorn app.main:app --reload
```
