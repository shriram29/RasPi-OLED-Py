import os.path
from demo_opts import get_device
from PIL import Image
import qrcode



def main():
    while True:
        size= 128, 64
        qrstr=input("Input String : ")
        logo=qrcode.make(qrstr).convert("RGBA")
        logo.thumbnail(size,Image.ANTIALIAS)
        fff = Image.new(logo.mode, logo.size, (255,) * 4)
        background = Image.new("RGBA", device.size, "white")
        posn = ((device.width - logo.width) // 2, 0)
        rot = logo.rotate(0, resample=Image.BILINEAR)
        img = Image.composite(rot, fff, rot)
        background.paste(img, posn)
        device.display(background.convert(device.mode))



if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
