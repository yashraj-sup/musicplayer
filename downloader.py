import yt_dlp
def download(url,output_folder):
    try:
        ydl_opts={"format":"bestaudio/best","outtmpl":output_folder +"/%(title)s.%(ext)s","postprocessors":[{"key":"ffmpegExtractAudio", "preferredcodec":"mp3"}]}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
            print(f"Download failed:{e}")
    except yt_dlp.utils.ExtractorError as e:
            print(f"Invalid url:{e}")
    except Exception as e:
            print(f"Unexpected error:{e}")
download("https://youtu.be/dXZYOqqg6Kk?si=kT-LfuDstd3S2qgj","/home/yash/Desktop/musicplayer")


