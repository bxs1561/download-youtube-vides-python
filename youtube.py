import pytube


def download_youtube_video():
    save = '/Users/bikramsubedi/PycharmProjects/youtube-download/save music'
    link = 'https://www.youtube.com/watch?v=v56I3tYAlnQ'
    youtube = pytube.YouTube(link)
    mp4 = youtube.streams.filter(progressive=True, file_extension='mp4')
    # video = youtube.streams.get_highest_resolution()
    video = mp4.get_highest_resolution()
    video.download(save)

    # Display all formats this video available
    # print(youtube.streams.all())

    # print(youtube.views)


def main():
    download_youtube_video()


# run program
if __name__ == '__main__':
    main()

