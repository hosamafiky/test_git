from pytube import Playlist, YouTube

url = input('Enter your YOUTUBE url : ')

if(url.__contains__('list')):
    yt_playlist = Playlist(url)
    url = input('Enter the output folder path : ')
    wantDownloadSrt = input('want to download subtitle ? (y/n) : default is no : ')

    for video in yt_playlist.videos:
        yt_video = YouTube(video.watch_url)
        if(wantDownloadSrt == 'y'):
            captions = yt_video.captions
            yt_video_caption = yt_video.captions.get_by_language_code(lang_code='en')
            if(captions.__contains__(yt_video_caption)) :
                yt_video_caption.download(output_path= f'{url}\{yt_playlist.title}', title= yt_video.title)
        print(f'{yt_video.title} is being downloaded....')
        yt_video.streams.get_highest_resolution().download(f'{url}\{yt_playlist.title}')
        print(f'{yt_video.title} is downloaded successfully.')

    print(f'{yt_playlist.title} is downloaded successfully.')
else:
    yt_video = YouTube(url)
    url = input('Enter the output folder path :')
    wantDownloadSrt = input('want to download subtitle ? (y/n) : default is no : ')
    if(wantDownloadSrt == 'y'):
        captions = yt_video.captions
        yt_video_caption = yt_video.captions.get_by_language_code(lang_code='en')
        if(captions.__contains__(yt_video_caption)) :
            yt_video_caption.download(output_path= f'{url}', title= yt_video.title)
    print(f'{yt_video.title} is being downloaded....')
    yt_video.streams.get_highest_resolution().download(f'{url}')
    print(f'{yt_video.title} is downloaded successfully.')


     