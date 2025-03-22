<div align="center">
  <img src="https://github.com/user-attachments/assets/dff43aaa-91fb-4fb5-9a2b-25214815b1e4" alt="RipBase" height="200">
</div>

<p align="center">
  <a href="https://discord.gg/xboxmods">
    <img src="https://discord.com/api/guilds/319560327719026709/widget.png?style=shield" alt="Discord Server">
  </a>
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Red-Discordbot">
  </a>
</p>

# Rip Seekbase API Wrapper

Rip Seekbase is a lightweight Flask-based API wrapper that interacts with the Seekbase API and Supabase authentication services. It provides several endpoints to fetch user information, update profiles, and perform various searches (email, Steam, Xbox, and graph searches) using the Seekbase API.

---

## The Start

This started with intercepting the api response finding out we can give ourself unlimited credits
<div align="center">
  <img src="https://github.com/user-attachments/assets/9c7a6d4f-d0d8-41db-bca6-8cd7cda1070e" alt="RipBase">
</div>

## More Digging

Then we started reversing the js
```python
import requests, jsbeautifier

def js_beautifier(url):
    response  = requests.get(url=url)
    if response.ok:
        return jsbeautifier.beautify(response.text)
 
with open("swag.js", "w", encoding="utf-8") as clean_js:
    clean_js.write(js_beautifier("https://seekbase.shop/assets/index-DRHhzkfw.js"))
```

<div align="center">
  <img src="https://github.com/user-attachments/assets/9b0a2e11-cfe1-4203-a456-19345d92ff7b" alt="RipBase" >
</div>

This lead to the conclusion that the api might only be checked client side via the frontend

---
# 🔥 Features

- 🧠 Auto-authentication via token endpoint
- 📧 Email info lookup
- 🎮 Steam and Xbox info lookup
- 🧑‍💼 User profile fetch and update
- 📈 Graph generation by keyword
- 🌐 Local API hosted via Flask + Waitress

## 🛠️ Installation

```bash
git clone https://github.com/BarcodeBimbo/RipbaseAPI.git
cd RipbaseAPI
pip install -r requirements.txt
```

Or manually install:

```bash
pip install flask requests waitress
```

## 🚀 Running the API

```bash
python RipbaseAPI.py
```

The API will start on: `http://127.0.0.1:5000`

## 📡 API Endpoints

| Method | Endpoint                       | Description                          |
|--------|--------------------------------|--------------------------------------|
| GET    | `/`                            | Shows available endpoints            |
| GET    | `/token`                       | Retrieves access token               |
| GET    | `/me`                          | Gets authenticated user info         |
| GET    | `/search?email=`              | Searches email info                  |
| GET    | `/search?steamId=`            | Searches Steam user info             |
| GET    | `/search?xboxId=`             | Searches Xbox user info              |
| GET    | `/search?term=`               | Generates a graph from search term   |
| GET    | `/update?username=&avatar_url=`| Updates user profile                 |

## 🧑‍💻 Developer

- **Name:** Joshua & Furix
- **Contact:** @BarcodeBimbo
- **Version:** 1.0.0
- **Updated:** March 22, 2025

## ⚠️ Disclaimer

This is a reverse-engineered, unofficial API tool intended for educational purposes. Use responsibly and ethically.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

---

### 🌟 Leave a star on GitHub if you find this helpful!








