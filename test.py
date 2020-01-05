import os.path
from demo_opts import get_device
from PIL import Image
import qrcode

device = get_device()
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 40), "Hello World", fill="white")
sleep(10)
