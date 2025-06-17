# 📝 John's Blog – Demo Flask Web App

Welcome to my personal blog demo site!  
This project was created as a **learning showcase** to demonstrate my skills in:

- 🐍 Python
- 🌐 Flask web framework
- 🎨 Bootstrap frontend design
- 🔗 REST API integration
- 📩 Email handling via SMTP
- 📁 Environment variable management with `python-dotenv`

> ⚠️ **Note:** This is not a production-ready website. It's a demo project built for learning and portfolio purposes only.

---

## 📺 Demo Video

Watch a quick demo of the site in action:  


https://github.com/user-attachments/assets/7d412908-9663-4869-8547-32196375d4b8


---

## 🚀 Features

- View blog posts fetched from an external API
- Read individual blog pages
- Responsive Bootstrap UI
- Contact form with email sending via Gmail SMTP
- `.env` support to manage secret keys and credentials

---

## 🛠️ Technologies Used

| Stack Layer | Tools/Libraries |
|-------------|-----------------|
| Frontend    | Bootstrap 5, HTML, Jinja2 |
| Backend     | Flask (Python) |
| Utilities   | `python-dotenv`, `smtplib`, `requests` |

---

## 📦 How to Run Locally

```bash
git clone https://github.com/yourusername/john-s-blog.git
cd john-s-blog
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
