#At first,you will need to install putube.You can install pytube by executing this command "pip install pytube"
from pytube import YouTube
linkofthevideo = input("Enter the url of the video of which you wanna download:\t")
urlofvideo = YouTube(linkofthevideo)
video = url.streams.first()
video.download()
print("Head over to your gallery and view your downloaded video.")