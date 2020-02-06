import pafy
URL = "https://www.youtube.com/watch?v=U6Cb6-EdaF8"
video = pafy.new(URL)
bestRES = video.getbest(preftype = "mp4")
file = bestRES.download("/root/Codes/2020_NY")
