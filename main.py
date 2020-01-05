import os.path
from demo_opts import get_device
from PIL import Image, ImageDraw, ImageFont
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

def displayQR(qrstr):
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

def displayText(textstr):
    img = Image.new('RGBA', device.size)

    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((10,10), textstr,font=fnt, fill=(0,0,0))
    displayIMG(img)

def main():
    while True:
        displayText("Hey")
        input()

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
