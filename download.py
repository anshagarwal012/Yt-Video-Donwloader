import yt_dlp, sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def download_youtube_video(url, path='downloads', quality='best'):
    ffmpeg_path = resource_path("ffmpeg.exe")
    ydl_opts = {
        'format': quality,
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,
        'noplaylist': True,
        'quiet': False,
        'merge_output_format': 'mp4'
    }

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

    print("\n🎥 Select video quality:")
    print("1. Best available (default)")
    print("2. 720p")
    print("3. 480p")

    choice = input("Enter choice [1-3]: ")

    if choice == '2':
        quality_format = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
    elif choice == '3':
        quality_format = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
    else:
        quality_format = 'bestvideo+bestaudio/best'

    download_youtube_video(video_url, download_path, quality_format)
