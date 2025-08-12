import yt_dlp

def download_youtube_video(url, path='downloads', quality='best', postprocessors=None):
    ydl_opts = {
        'format': quality,
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': False,
    }
    if postprocessors:
        ydl_opts['postprocessors'] = postprocessors

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=True)
            print(f"✅ Downloaded: {info['title']}")
        except Exception as e:
            print(f"❌ Error: {e}")

# ---- MAIN ----
if __name__ == '__main__':
    video_url = input("🔗 Enter YouTube video URL: ")
    download_path = input("📁 Enter download folder (default: downloads): ") or 'downloads'

    print("\n🎥 Select quality:")
    print("1. Best available (default)")
    print("2. 720p")
    print("3. 480p")
    print("4. Audio only (mp3)")

    choice = input("Enter choice [1-4]: ")

    if choice == '2':
        quality_format = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
        postprocessors = None
    elif choice == '3':
        quality_format = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
        postprocessors = None
    elif choice == '4':
        quality_format = 'bestaudio/best'
        postprocessors = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        quality_format = 'best'
        postprocessors = None

    download_youtube_video(video_url, download_path, quality_format, postprocessors)
