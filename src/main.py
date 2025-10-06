from flask import Flask, jsonify
from flask import request
from typing import Dict
import uvicorn
from utils.transcriber import transcribe_youtube_video
app = Flask(__name__)


@app.route('/api/v1/youtube/transcribe',methods=['POST'])
def transcribe_youtube():
    print("Transcribe YouTube endpoint hit")
    data: Dict[str, str] = request.json or {}
    if not data or "url" not in data or "lang" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    caption = transcribe_youtube_video(data["url"], data["lang"])
    return caption

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
