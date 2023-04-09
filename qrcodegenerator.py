import qrcode
import image
qr = qrcode.QRCode(
    version = 7, #15 means the verion of the qr code high number bigger the code image and complicated picture
    box_size = 10, # Size of the box where qr code will be displayed
    border = 4 # It is the white part of image -- border in all 4 sides with white color
)

data = "https://www.youtube.com/@rykers_charan8169"
# As i have given the path and it will create qr code related / using path.


qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color="black",back_color = "white")
img.save("qrcode.png")

