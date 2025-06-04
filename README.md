# 🚀 GitHub Webhook Dashboard

This project captures GitHub webhook events (like pushes, pull requests, and merges) and displays them in a live frontend dashboard. It's built using **Flask**, **MongoDB**, **React + Vite**, and **ngrok** to tunnel webhooks during development.

---

## 📌 Features

- Receives GitHub webhooks via Flask
- Stores events in MongoDB
- Polls database every 15 seconds and displays:
  - Pushes
  - Pull Requests
  - Merges
- Works with local development via ngrok

---

## 🛠️ Tech Stack

- 🔙 **Backend**: Flask + MongoDB
- 🔚 **Frontend**: React + Vite
- 🌐 **Webhook Tunnel**: ngrok

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sudhiitg/web-hook.git
cd web-hook
