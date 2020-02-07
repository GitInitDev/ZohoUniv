import pyqrcode as qr
urlInput = raw_input("Enter The URL : ")
url = qr.create(urlInput)
print(url.terminal(quiet_zone=1))
