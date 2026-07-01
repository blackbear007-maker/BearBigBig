"""
edge-tts Netlify Function
Accepts: ?text=...&voice=zh-TW-YunJheNeural
Returns: audio/mpeg (base64-encoded)
"""
import asyncio
import base64
import json
import os

try:
    import edge_tts
    HAS_EDGE_TTS = True
except ImportError:
    HAS_EDGE_TTS = False

ALLOWED_VOICES = {
    "male-warm":   "zh-TW-YunJheNeural",
    "male-news":   "zh-CN-YunyangNeural",
    "female-soft": "zh-TW-HsiaoChenNeural",
}

async def synthesize(text: str, voice: str) -> bytes:
    communicate = edge_tts.Communicate(text, voice)
    chunks = []
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            chunks.append(chunk["data"])
    return b"".join(chunks)


def handler(event, context):
    # CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
            },
            "body": "",
        }

    if not HAS_EDGE_TTS:
        return {
            "statusCode": 503,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "edge-tts not installed"}),
        }

    params = event.get("queryStringParameters") or {}
    text = (params.get("text") or "").strip()[:600]  # limit per chunk
    voice_key = params.get("voice") or "male-warm"
    voice = ALLOWED_VOICES.get(voice_key, ALLOWED_VOICES["male-warm"])

    if not text:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "text is required"}),
        }

    try:
        audio = asyncio.run(synthesize(text, voice))
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "audio/mpeg",
                "Access-Control-Allow-Origin": "*",
                "Cache-Control": "public, max-age=86400",
            },
            "body": base64.b64encode(audio).decode("utf-8"),
            "isBase64Encoded": True,
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)}),
        }
