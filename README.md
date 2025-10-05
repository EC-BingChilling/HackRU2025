# 🧠 EduAid — AI Study Companion

**HackRU Fall 2025 Project**
*A personalized AI study assistant that summarizes, speaks, and remembers your notes.*

---

## 📘 Overview

**EduAid** helps students **learn faster and remember more** by turning study material into concise, spoken summaries.
It’s built to make studying conversational and efficient using accessible AI technologies.

**Key Features (Goal Vision):**

* 🧠 Summarize text intelligently (via Gemini)
* 🔊 Speak summaries aloud (via ElevenLabs)
* 🗂️ Store and retrieve learning sessions (via Snowflake)
* 💻 Clean, minimal, distraction-free UI (Next.js / React)

> 🔗 **Live Frontend:** [https://hack-ru-2025.vercel.app/](#)
> *(Deployed via Vercel — replace with actual URL once confirmed)*

---

## 📖 Current Status

**Status:** ⚙️ *MVP functional / Backend deployment pending*

EduAid currently runs with:

* ✅ **Live frontend on Vercel**
* ✅ **Working local MVP FastAPI backend** (`eduaid_mvp/`)
* ⚠️ **Full backend (`eduaid_backend/`)** under development (Gemini, ElevenLabs, and Snowflake integration in progress)

---

## 🧩 Project Structure

```
.
├── eduaid_backend/            # Full backend (unfinished integration)
├── eduaid_mvp/                # Minimal working FastAPI backend (MVP)
│   ├── main.py
│   ├── requirements.txt
│   └── start.sh
├── study-app/                 # React / Next.js frontend (deployed on Vercel)
│   ├── pages/
│   ├── components/
│   └── ...
├── README.md
└── other supporting files
```

---

## 🧪 What Works (MVP)

| Component                     | Status     | Description                                                            |
| ----------------------------- | ---------- | ---------------------------------------------------------------------- |
| Frontend (Vercel)             | ✅ Live     | Deployed, fully functional UI connected to backend locally or via API. |
| `/summarize`                  | ✅ Working  | Accepts text and returns AI-style summary (mocked Gemini response).    |
| `/history`                    | ✅ Working  | Stores recent summaries in memory (resets on restart).                 |
| Local FastAPI backend         | ✅ Working  | Lightweight MVP server running on `localhost:8000`.                    |
| Frontend ↔ Backend connection | ✅ Verified | Tested end-to-end locally.                                             |
| Voice (ElevenLabs)            | ⚠️ Planned | Placeholder; not yet integrated.                                       |

---

## 🚧 What’s Broken / Not Yet Implemented

| Area                    | Status            | Notes                                                               |
| ----------------------- | ----------------- | ------------------------------------------------------------------- |
| Backend deployment      | ❌ Not yet live    | Render / Railway deployment failing (environment detection issues). |
| Gemini API integration  | 🚧 In progress    | Summaries currently mocked.                                         |
| ElevenLabs voice output | 🚧 In progress    | Placeholder endpoint only.                                          |
| Snowflake database      | ❌ Not implemented | Planned for persistent storage and analytics.                       |
| Authentication          | ❌ Not implemented | Placeholder only.                                                   |
| Error handling / CORS   | ⚠️ Minimal        | Works locally; needs production config.                             |

---

## 🛠 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/EC-BingChilling/HackRU2025.git
cd HackRU2025
```

### 2️⃣ Backend Setup (MVP)

```bash
cd eduaid_mvp
python3 -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Server runs at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 3️⃣ Frontend Setup

```bash
cd ../study-app
npm install
npm run dev
```

Frontend runs at [http://localhost:3000](http://localhost:3000)

> 🧩 Make sure the frontend `.env.local` file contains:
> `NEXT_PUBLIC_API_URL=http://localhost:8000`

---

## 📡 API Endpoints (MVP Only)

| Method | Path         | Description                                                |
| ------ | ------------ | ---------------------------------------------------------- |
| `GET`  | `/`          | Health / status check                                      |
| `POST` | `/summarize` | Accepts `{ text: string }` → returns `{ summary: string }` |
| `GET`  | `/history`   | Returns in-memory list of `{ input, summary }`             |

**Example Response:**

```json
{
  "history": [
    {
      "input": "Photosynthesis is how plants make energy...",
      "summary": "Plants convert light to energy using chlorophyll."
    }
  ]
}
```

---

## 🧭 Future Roadmap

| Milestone                    | Goal                              | Status         |
| ---------------------------- | --------------------------------- | -------------- |
| ✅ MVP (Local API + Frontend) | Functional demo                   | ✅ Complete     |
| 🧩 Gemini API                | Real summarization                | 🚧 In progress |
| 🔊 ElevenLabs                | Voice synthesis                   | 🚧 Planned     |
| 💾 Snowflake DB              | Persistent storage                | 🚧 Pending     |
| ☁️ Backend Deployment        | Cloud hosting (Render / Railway)  | ❌ Failed       |
| 🔐 Auth System               | User accounts                     | 🔜 Future      |
| 📊 Learning Dashboard        | Progress metrics & study insights | 🔜 Future      |

---

## 💬 Summary

EduAid started from a simple question:

> “What if studying felt like talking to an AI tutor?”

In just 48 hours, the team built a working prototype that **summarizes, speaks, and remembers** your notes.
The backend didn’t quite launch — but the **vision and foundation are solid** and ready to grow.

> “It might not have launched... but it *learned* faster than we did.” 💡
