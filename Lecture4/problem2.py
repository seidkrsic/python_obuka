

import qrcode
img = qrcode.make('https://pypi.org/project/qrcode/')
img.save("qr_code.png") 
