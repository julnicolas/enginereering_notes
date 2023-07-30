""" Shows how to issue a qrcode with default config. """

import qrcode

img = qrcode.make('some data')
img.save('test_qrcode.png')

