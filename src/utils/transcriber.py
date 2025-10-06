from pytubefix import YouTube

def transcribe_youtube_video(url: str, caption_language: str = "en"):
    try:
        yt = YouTube(url)
        title = yt.title
        desc = yt.description
        duration = yt.length 
        if yt.length > 54000:
            print("Video too long (>15h).")
            return {"error":"Video too long (>15h)."}

        for code in [caption_language, f"a.{caption_language}", "en", "a.en"]:
            caption = yt.captions.get_by_language_code(code)
            if caption:
                print(f"Using captions: {code}")
                try:
                    return {"transcribe":caption.generate_srt_captions(),"title":title,"desc":desc,"duration":duration}
                except Exception:
                    print("Failed to generate SRT, using XML captions instead.")
                    return {"transcribe":caption.xml_captions,"title":title,"desc":desc,"duration":duration}

        print("No captions found for this video.")
        return {"error":"No captions found for this video."}

    except Exception as e:
        print(f"Error downloading video: {e}")
        return {"error":"No captions found for this video."}
