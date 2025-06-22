# 🎬 Aminul Movie Site (IMDB Clone)

A professional movie web application built with **Django**, featuring Swiper sliders, dynamic filtering, pagination, user authentication, and more. This project replicates core features of IMDB, tailored for portfolio demonstration and future scalability.

---

## 🚀 Features

- 🎥 Movie listing by genre, language, and release year
- 🔍 Search & filter with pagination
- 👤 User Authentication (Sign Up, Login, Logout)
- 🔐 Password Reset via Email with HTML template
- 🎞️ Movie Detail Page
- 🖼️ Swiper Slider for featured movies
- 📅 Archive view by year
- 🌐 Fully responsive layout (HTML + CSS)
- 📬 Custom password reset email template with button

---

## 📸 Screenshots

### 🏠 Home Page
![Home](images/home.jpg)

### 🔐 Login Page
![Login](images/login.jpg)

### 🎬 Movie Detail Page
![Movie Detail](images/movie-detail.jpg)

---

## 📁 Project Structure

src/
├── movie/                  # 🎬 Main Django app (views, models, URLs, forms)
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/              # 🎨 HTML templates
│   ├── base.html           # Common layout
│   ├── home.html
│   ├── movie_detail.html
│   ├── movie_list.html
│   ├── movie_archive_year.html
│   └── registration/       # 🔐 Auth-related templates
│       ├── login.html
│       ├── logout.html
│       ├── signup.html
│       ├── password_reset_form.html
│       ├── password_reset_done.html
│       ├── password_reset_confirm.html
│       ├── password_reset_complete.html
│       └── password_reset_email.html
│
├── static/                 # ⚙️ Static files (CSS, JS, Images)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── swiper/             # Optional Swiper slider files
│       ├── swiper-bundle.min.js
│       └── swiper-bundle.min.css
│
├── images/                 # 🖼️ Screenshots for GitHub README
│   ├── home.png
│   ├── movie_detail.png
│   └── login_page.png
│
├── db.sqlite3              # 🗄️ SQLite database file (gitignored)
├── requirements.txt        # 📦 Python dependencies
├── .gitignore              # 🚫 Files to ignore in Git
└── README.md               # 📘 Project documentation


## 📦 Requirements

Make sure to activate your virtual environment first:

```bash
# On Windows
.\env\Scripts\activate

cd src
python manage.py runserver

🛠️ Tech Stack
Python 3.12

Django 5.2

HTML5 / CSS3 / Bootstrap

SwiperJS

Email Backend (console/email HTML)

SQLite3 (default)

👤 Author
Aminul Islam Sumon
🔗 GitHub: aminul-portfolio

