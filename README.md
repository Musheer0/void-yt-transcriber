# 🎥 YouTube Transcription API

A simple API to **fetch and transcribe YouTube video captions** into text (SRT format).
Built for devs who just want the damn subtitles — fast, clean, and in any supported language.

---

## 🚀 Endpoint

```
POST /api/v1/youtube/transcribe
```

### 📦 Request Body

```json
{
  "url": "YOUR_YOUTUBE_VIDEO_URL",
  "lang": "en"
}
```

| Field  | Type     | Required | Description                                    |
| ------ | -------- | -------- | ---------------------------------------------- |
| `url`  | `string` | ✅        | Full YouTube video URL                         |
| `lang` | `string` | ✅        | Caption language code (e.g., `en`, `hi`, `es`) |

---

## 💻 Example (curl)

```bash
curl -X POST https://your-published-url.replit.app/api/v1/youtube/transcribe \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=VIDEO_ID", "lang": "en"}'
```

---

## 🌍 Supported Languages

Supports **tons of languages**, including:

* English (`en`)
* Hindi (`hi`)
* Spanish (`es`)
* French (`fr`)
* Chinese (`zh`)
* Arabic (`ar`)
* * many more...

Check out the [`caption-codes.json`](./caption-codes.json) file for the **full list** of supported language codes.

---

## 📤 Response

### ✅ Successful Response

```json
{
  "transcribe": "WEBVTT\n00:00:00.000 --> 00:00:05.000\nThis is a caption example...",
  "title": "How Load Balancing Works in Nginx",
  "desc": "In this video, we’ll learn how Load Balancing works using Nginx...",
  "duration": 542
}
```

| Field        | Type     | Description                   |
| ------------ | -------- | ----------------------------- |
| `transcribe` | `string` | Captions in SRT / text format |
| `title`      | `string` | YouTube video title           |
| `desc`       | `string` | Video description             |
| `duration`   | `number` | Video duration in seconds     |

---

## ⚠️ Error Responses

| Status | Message                 | Meaning                                      |
| ------ | ----------------------- | -------------------------------------------- |
| `400`  | `Invalid YouTube URL`   | The URL is missing or incorrect              |
| `404`  | `Captions not found`    | No captions available for the given language |
| `500`  | `Internal Server Error` | Something went wrong on the server           |

---

## 🧠 Notes

* Transcriptions depend on YouTube’s **auto-generated captions** — accuracy may vary.
* The API **doesn’t download videos**; it only fetches caption data.

---

## 🧰 Tech Stack

* **Python 3.11+**
* **Flask / FastAPI** (depending on your setup)
* **pytubefix** for YouTube data fetching

---

## 🧑‍💻 Example Integration (Node.js)

```js
const res = await fetch("https://your-published-url.replit.app/api/v1/youtube/transcribe", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    url: "https://www.youtube.com/watch?v=VIDEO_ID",
    lang: "en"
  })
});

const data = await res.json();
console.log(data.transcribe);
```

---

## 📜 License

MIT — do whatever you want, just don’t sell it as your “AI-powered transcription startup”.
(rn this has no auth check or internal auth check make sure to implement one of your publishing if just for mvp then fk auth)
---
