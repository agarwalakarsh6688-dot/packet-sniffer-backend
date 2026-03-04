# 🔌 Packet Sniffer Backend API

Backend service for the **Live TCP Packet Sniffer dashboard**.

This API simulates TCP packet traffic and provides packet data to the frontend monitoring interface.

---

## 🌐 API Endpoint

```
GET /packets
```

Returns a simulated TCP packet.

Example Response

```json
{
  "src_ip": "192.168.1.42",
  "src_port": 42123,
  "dst_ip": "10.0.0.15",
  "dst_port": 443
}
```

---

## ⚙️ Technology Stack

* Python
* Flask
* REST API
* Hosted on Render

---

## 🚀 Deployment

Backend is deployed on Render:

https://packet-sniffer-backend.onrender.com

---

## 📂 Project Structure

```
packet-sniffer-backend
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

The API randomly generates simulated TCP packet data including:

* Source IP
* Source Port
* Destination IP
* Destination Port

The frontend fetches this endpoint continuously to simulate **live network traffic monitoring**.

---

## 👨‍💻 Author

**Akarsh Agarwal**

© 2026 Akarsh Agarwal
