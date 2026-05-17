# DarkWatcher: Dark Web Monitoring and Threat Detection System

A simulation-based **dark web monitoring and threat intelligence system** that detects leaked credentials and sensitive data from web sources, stores them in databases, indexes them for search, and triggers real-time alerts.

---

# 🚀 Features

* 🔍 Web scraping (Tor + HTTP sources)
* 🧠 Keyword-based leak detection
* 📦 MongoDB storage for raw and parsed data
* 🔎 Elasticsearch indexing for search & analytics
* 📧 Email alert system for sensitive data detection
* 📊 Dashboard-ready data pipeline (Flask compatible)
* 🐳 Fully containerized using Docker & Docker Compose
* 🔐 Supports simulated dark web environments

---

# 🧱 Tech Stack

* Python 3.10+
* Docker & Docker Compose
* MongoDB 6
* Elasticsearch 8.x
* Tor Proxy
* Flask (Dashboard)
* Requests / BeautifulSoup
* SMTP (Email alerts)

---

# 📁 Project Structure

```
DarkWatcher/
│
├── main.py
├── docker-compose.yml
├── requirements.txt
├── .env
│
├── core/
│   ├── scraper.py
│   ├── analyzer.py
│   ├── parser.py
│   ├── tor_client.py
│
├── database/
│   ├── mongo_handler.py
│   ├── elastic_handler.py
│
├── alerts/
│   ├── email_alert.py
│   ├── notifier.py
│
├── utils/
│   ├── helpers.py
│   ├── logger.py
│
├── config/
│   ├── settings.py
│   ├── tor_config.py
│
├── dashboard/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   │   └── login.html
│   ├── static/
│       ├── style.css
│
├── data/
│   ├── keywords.txt
│
├── ml/
│   ├── anomaly_detector.py
│
├── test_sites/
│   ├── leak1.html
│   ├── leak2.html
│   ├── leak3.html
│   ├── leak4.html
│   ├── leak5.html
│   ├── leak6.html
│   ├── leak7.html
│   ├── leak8.html
│
├── utils/
│   ├── helpers.py
│   ├── logger.py
│
└── docker/
    └── Dockerfile
    └── torrc
    └── wait-for-it.sh

```

---

# ⚙️ Setup & Installation

## 🐳 1. Clone the repository

```bash
git clone https://github.com/your-repo/DarkWatcher.git
cd DarkWatcher
```

---

## 📦 2. Configure environment variables

Create a `.env` file:

```env
MONGO_URI=mongodb://mongodb:27017/
ELASTIC_HOST=http://elasticsearch:9200

ALERT_EMAIL=your_email@gmail.com
ALERT_PASSWORD=your_app_password
```

---

## 🚀 3. Run with Docker

```bash
docker compose down -v
docker compose up --build
```

---

## 📊 4. Access Services

| Service       | URL                                            |
| ------------- | ---------------------------------------------- |
| Dashboard     | [http://localhost:5000](http://localhost:5000) |
| Elasticsearch | [http://localhost:9200](http://localhost:9200) |
| MongoDB       | mongodb://localhost:27017                      |

---

# 🔎 How It Works

1. Scraper fetches data from configured URLs
2. Parser extracts emails, passwords, and credit cards
3. Analyzer checks against keyword list
4. Data stored in MongoDB
5. Elasticsearch indexes data
6. Alerts triggered via email
7. Dashboard displays results

---

# 🧪 Testing Setup

Simulate leak pages locally:

```bash
python3 -m http.server 8000
```

Use:

```
http://host.docker.internal:8000/leak1.html
http://host.docker.internal:8000/leak1.html
.
.
.
http://host.docker.internal:8000/leakn.html
```

---

# ⚠️ Known Issues & Fixes

## ❌ dotenv not found

```bash
pip install python-dotenv
```

## ❌ Docker container exits immediately

Ensure main.py runs in loop.

## ❌ Elasticsearch version mismatch

Use:

```bash
elasticsearch==8.11.0
```

## ❌ host.docker.internal not working (Linux)

Add:

```yaml
extra_hosts:
  - "host.docker.internal:host-gateway"
```

---

# 🔐 Security Notes

* Use Gmail App Passwords
* Educational / simulation only
* Do not use on unauthorized sources

---

# 📈 Future Enhancements

* Real-time WebSocket dashboard
* AI threat scoring
* Telegram alerts
* Celery + Redis architecture
* Grafana monitoring

---

# 👨‍💻 Author

Dark Web Monitoring System Prototype

---

# 📜 License

Educational use only.
