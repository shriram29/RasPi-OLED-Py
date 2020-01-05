import os.path
from demo_opts import get_device
from PIL import Image
import qrcode



def main():
    while True:
        qrstr=input("Input String : ")
        logo=qrcode.make(qrstr).convert("RGBA")
        fff = Image.new(logo.mode, logo.size, (255,) * 4)
        background = Image.new("RGBA", device.size, "white")
        posn = ((device.width - logo.width) // 2, 0)



if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
