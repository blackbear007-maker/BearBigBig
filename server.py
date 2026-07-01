"""
熊大大 PWA — Railway 伺服器
FastAPI 同時負責：
  1. 靜態檔案（index.html / story.json / manifest.json / sw.js / icons）
  2. GET /tts  ← edge-tts 語音合成端點
"""
import asyncio
import os

import edge_tts
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="熊大大 API")

# CORS（讓本機開發也能呼叫）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

# ── 語音對應表 ──────────────────────────────────────────────
VOICES = {
    "male-warm":   "zh-TW-YunJheNeural",      # 溫柔磁性台灣男聲
    "male-news":   "zh-CN-YunyangNeural",      # 沉穩新聞普通話男聲
    "female-soft": "zh-TW-HsiaoChenNeural",   # 輕柔台灣女聲
}


async def _synthesize(text: str, voice: str) -> bytes:
    communicate = edge_tts.Communicate(text, voice)
    chunks: list[bytes] = []
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            chunks.append(chunk["data"])
    return b"".join(chunks)


# ── TTS 端點 ────────────────────────────────────────────────
@app.get("/tts")
async def tts(
    text: str = Query(..., max_length=700),
    voice: str = Query("male-warm"),
):
    voice_id = VOICES.get(voice)
    if not voice_id:
        raise HTTPException(status_code=400, detail=f"未知聲優 key: {voice}")
    if not text.strip():
        raise HTTPException(status_code=400, detail="text 不能為空")

    audio = await _synthesize(text.strip(), voice_id)
    return Response(
        content=audio,
        media_type="audio/mpeg",
        headers={"Cache-Control": "public, max-age=86400"},
    )


# ── 健康檢查 ─────────────────────────────────────────────────
@app.get("/healthz")
async def health():
    return {"status": "ok"}


# ── 靜態檔案（放最後，避免攔截 /tts）───────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/", StaticFiles(directory=BASE_DIR, html=True), name="static")
