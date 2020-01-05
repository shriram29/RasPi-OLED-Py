import os.path
from demo_opts import get_device
from PIL import Image
import qrcode

device = get_device()
background="test"
device.display(background.convert(device.mode))
