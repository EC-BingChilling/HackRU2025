# 🚀 HackRU F25 Project — EduAid Pro

## 🎯 Overview
**EduAid Pro** is an **Education-focused AI platform** that transforms messy lecture notes into structured **flashcards, quizzes, and audio study guides**.  
It’s designed for students, educators, and lifelong learners who want to turn unorganized notes into usable, interactive learning material — instantly.

### 🏷️ Track
**Education**

### 🏆 Superlatives / Prize Categories
- 🖼️ Best UI/UX Design  
- 🌐 Best .Tech Domain Name (MLH)  
- 🧠 Best Use of Gemini API (MLH)  
- ❄️ Best Use of Snowflake API (MLH)  
- 🔊 Best Use of ElevenLabs (MLH)  
- 💼 Best Entrepreneurial Hack (IDEA)  
- 🌱 (Stretch) Best Newbie Hack (if rules allow)  
- 💀 (Fallback) Best Failure to Launch (if anything breaks)

---

## 🧩 Core Features (MVP)
1. **Text Upload**
   - Paste or upload lecture notes → stored in DB (Snowflake).  
2. **AI Analysis (Gemini)**
   - Converts notes into structured flashcards + quizzes in JSON format.  
3. **Results Output**
   - Display generated flashcards and quizzes in a simple UI.  
4. **UI Dashboard**
   - Clean interface: textarea input + “Education” mode dropdown + result cards.  
5. **Deployment**
   - Hosted on Vercel and live at a `.tech` domain.  

---

## 🌟 Stretch Features
1. **Snowflake Integration**
   - Store and retrieve uploaded notes from Snowflake DB.  
2. **ElevenLabs Integration**
   - Convert AI summaries into natural audio files.  
   - “Play Study Guide” button on UI.  
3. **UI/UX Polish**
   - Responsive, minimalist dashboard with audio player.  
4. **Entrepreneurial Layer**
   - Pitch deck: Problem → Solution → Demo → Market → Monetization.  
   - SaaS framing: EduAid for students, schools, and edtech platforms.  

---

## 👥 Team Roles

### 🧑‍💻 You — Backend Lead (Captain)
- Build the **FastAPI backend** (`/upload`, `/analyze`, `/results`).  
- Integrate **Gemini**, **Snowflake**, and **ElevenLabs APIs**.  
- Debug and ensure system stability.  
- Mentor teammates when stuck.  
- **Deliverable by 8 PM Saturday:** stable backend tested with Postman.

---

### 🤖 Teammate A — AI Prompt & Integration Wrangler
- Write Gemini prompts:  
  *“Turn these lecture notes into 5 flashcards and 3 quiz questions in JSON.”*  
- Integrate Gemini API into `/analyze`.  
- Add ElevenLabs API for audio summary generation.  
- Create sample notes for demo testing.  
- **Deliverable by 8 PM Saturday:** working Gemini → JSON + audio output.

---

### 🎨 Teammate B — UI/UX & Deployment Lead
- Build the frontend (React or V0):  
  - Textarea for note input.  
  - Dropdown for mode selection.  
  - Cards for displaying flashcards and quiz questions.  
  - Audio player for ElevenLabs summary.  
- Deploy to Vercel and attach a `.tech` domain.  
- Design Canva slides for pitch.  
- **Deliverable by 8 PM Saturday:** deployed frontend calling backend successfully.

---

## 🕒 Timeline

### **Saturday**
| Time | Tasks | Goal |
|------|--------|------|
| 12–3 PM | Backend skeleton, Gemini prompt draft, UI scaffold | End-to-end MVP (ugly but functional) |
| 3–8 PM | Add Snowflake + ElevenLabs, refine prompts, deploy frontend | All features in place by dinner |
| 8–11 PM | Debug integrations, record backup demo, create slides | Stable demo ready |
| 12–6 AM | Sleep | 💤 Recharge for polish day |

### **Sunday**
| Time | Tasks | Goal |
|------|--------|------|
| 6–9 AM | Fix bugs, polish UI, finalize prompts | Working demo with sponsor APIs |
| 9–10:30 AM | Record final demo, submit to Devpost | ✅ Submission done |
| 10:30–11 AM | Freeze code, hydrate, prep for judging | Ready for demo |
| 1–3 PM | Judging | 🏁 Deliver confident pitch |

---

## ⚙️ Tech Stack
**Backend:** FastAPI, Python  
**Frontend:** React / V0  
**Database:** Snowflake (fallback: SQLite)  
**AI APIs:** Gemini (Google), ElevenLabs (MLH Sponsor)  
**Deployment:** Vercel + `.tech` domain  
**Design:** Canva (pitch deck), Figma (optional wireframes)  

---

## 🧱 Setup Instructions

### **Backend**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate     # (Windows)

# Install dependencies
pip install fastapi uvicorn requests snowflake-connector-python python-dotenv

# Run server
uvicorn main:app --reload
