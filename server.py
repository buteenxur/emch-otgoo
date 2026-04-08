from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn, os

app = FastAPI(title="Эмч Отгоо")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/manifest.json")
async def manifest():
    return FileResponse("manifest.json", media_type="application/json")

@app.get("/sw.js")
async def sw():
    return FileResponse("sw.js", media_type="application/javascript")

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
