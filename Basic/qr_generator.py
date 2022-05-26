import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

data = "http://klanting.ga:8080/"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='white')
img.save('site.png')
