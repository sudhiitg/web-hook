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

### 2 Install Dependencies 

pip install -r requirements.txt

### 3 Run Backend  

cd api
python app.py

### 5 Run Frontend  

cd client
npm install
npm run dev

### 6 ngrok setup
Download ngrok in your local using this link : https://dashboard.ngrok.com/get-started/setup/windows
Run command : ngrok config add-authtoken<Your_AuthToken>(unique for every user);
then in shell run : ./ngrok http 5000

### 7 Web Hook setup on Github
-Go to GitHub Action-repo repository → Settings > Webhooks
-Click "Add webhook"
-Use your ngrok URL + /github (e.g., [https://abc123.ngrok.io](https://5c1c-2406-7400-61-3200-8409-b4ab-9045-bdc1.ngrok-free.app/github)
-Set content type to application/json
-Select events: push, pull request
-Save webhook
Attached Image of UI
![Dashboard Screenshot](assets/dashboard.png)



