#!/usr/bin/env python3

# import dependencies
import pyqrcode

# text which you want to convert to QRCode
QRtext = input('Enter text to generate QR: ')

# filename that will be saved
QRimg = input('Enter image name to save: ')

# image extension
QRimg = QRimg + '.svg'

# Generating Final QRCode with high error correction level
FinalQR = pyqrcode.create(QRtext, error='H')

# Showing the QR code
FinalQR.show()

# Saving the QR code as an SVG file with appropriate scale
FinalQR.svg(QRimg, scale=1000)
