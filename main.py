import os.path
from demo_opts import get_device
from PIL import Image
import qrcode


def displayIMG(logo):
    logo.thumbnail(device.size,Image.ANTIALIAS)
    fff = Image.new(logo.mode, logo.size, (255,) * 4)
    background = Image.new("RGBA", device.size, "black")
    posn = ((device.width - logo.width) // 2, 0)
    rot = logo.rotate(0, resample=Image.BILINEAR)
    img = Image.composite(rot, fff, rot)
    background.paste(img, posn)
    device.display(background.convert(device.mode))

def main():
    while True:
        qrstr="Hey"
        # qrstr=input("Input String : ")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=0,
        )
        qr.add_data(qrstr)
        qr.make(fit=True)
        img = qr.make_image(fill_color="white", back_color="black")
        logo=img.convert("RGBA")
        displayIMG(logo)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
