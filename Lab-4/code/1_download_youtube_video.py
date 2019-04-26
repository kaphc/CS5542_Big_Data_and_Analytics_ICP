from pytube import YouTube


def download_video(video_url, file_name):
    yt = YouTube(video_url)

    YouTube(video_url).streams.first().download('data//video', file_name)

    file_path = 'data/youtube_captions/' + file_name + '.txt'
    en_caption = yt.captions.get_by_language_code('en')
    en_caption_convert_to_srt = (en_caption.generate_srt_captions())
    text_file = open(file_path, "w")
    text_file.write(en_caption_convert_to_srt)
    text_file.close()


video_url = "https://www.youtube.com/watch?v=xJUokU3fl58"
file_name = "10900"
download_video(video_url, file_name)
