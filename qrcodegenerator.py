import qrcode 
qr=qrcode.QRCode(
                version=1,
                 border=2,
                 box_size=10 )
qr.add_data("hi this is me the") # here you can add link or anything
qr.make(fit=True)
img=qr.make_image(fill_color="Blue")
img.save("qrcode.png")