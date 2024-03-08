from pytube import YouTube

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.Download()
    except:
        print("error")
    print("Download berhasil!")

link = input("Masukan link video youtube: ")
download(link)
