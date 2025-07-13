# 📒 Contact Book - Django App

A simple yet powerful Contact Book web application built using **Django**.  
Users can **sign up**, **log in**, manage their **personal contacts**, and also view public **API-based contact data**.

---

## 🌟 Features

- ✅ User Authentication (Signup, Login, Logout)
- ✅ Add, Edit, Delete personal contacts
- ✅ View a few global contacts from [JSONPlaceholder API](https://jsonplaceholder.typicode.com/users)
- ✅ Contacts are private and user-specific
- ✅ Search functionality to filter contacts
- ✅ Beautiful and responsive UI with custom CSS
- ✅ Deployed on [Render](https://render.com)

---

## 📸 Screenshots

| Login & SignUp Pages | Dashboard |
|----------------------|-----------|
| ![Login](https://github.com/user-attachments/assets/3f642875-52ae-4e64-8f5e-24d77ecf030c)<br>![SignUp](https://github.com/user-attachments/assets/9d08236d-5412-40ff-a168-6a89f03d110b) | ![Dashboard](https://github.com/user-attachments/assets/e0326481-a2c5-40b5-9e54-1dd89fed33a9) |


---

## 🚀 Live Demo

🔗 [Live Link](https://contactbook-usingdjango.onrender.com/)

> 📝 Create a free account to manage your own contacts!

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (custom)
- **Backend:** Python, Django
- **Database:** SQLite (default for dev)
- **Deployment:** Render
- **External API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/users)

---

## ⚙️ Getting Started (Run Locally)

```bash
git clone https://github.com/yourusername/ContactBook.git
cd ContactBook
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

Then create a .env file in the root:
SECRET_KEY=your-django-secret-key
DEBUG=True

Now run the server:
python manage.py migrate
python manage.py runserver
```
✍️ Author
Ayush — Learning Full Stack with Python

📄 License
This project is licensed under the MIT License.
