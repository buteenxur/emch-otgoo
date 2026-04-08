# 🐴 Эмч Отгоо — Deploy заавар

## Render.com дээр deploy хийх (5 минут)

### 1. GitHub-д repo үүсгэх
- github.com → New Repository → `emch-otgoo`
- Энэ zip-ийн бүх файлыг upload хийх

### 2. Render.com дээр deploy
- render.com → New → Web Service
- GitHub repo холбох
- Settings:
  - Runtime: Python 3
  - Build: `pip install -r requirements.txt`
  - Start: `uvicorn server:app --host 0.0.0.0 --port $PORT`
- Create Web Service

### 3. Бусдад илгээх
URL: `https://emch-otgoo.onrender.com`

Мессеж илгээх:
```
🐴 Эмч Отгоо — Малын эмчийн AI апп
Суулгах: https://emch-otgoo.onrender.com
Нээгээд → ⋮ → "Нүүр хуудсанд нэмэх"
```

## Файлууд
- `server.py` — FastAPI сервер
- `static/index.html` — Апп (бүх мэдээлэлтэй)
- `manifest.json` — PWA тохиргоо
- `sw.js` — Офлайн ажиллагаа
- `requirements.txt` — Python хамаарал
