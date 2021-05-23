from pytube import YouTube

# Getting a link from a user
link = input('Insert your link:\n')
yt = YouTube(link)

# Printing information about the video on the screen
print('Author:', yt.author)
print('Name:', yt.title)
print('Views:', yt.views)
print('Duration:', str(yt.length // 60) + ':' + str((yt.length % 60) // 10) + str(yt.length % 60))

# Getting the highest resolution stream
ys = yt.streams.get_highest_resolution()

# Downloading the video
print('Wait a sec, your video is downloading...')
ys.download('D:/Useless/Youtube_videos') # insert your path in here
print('Done :)')
