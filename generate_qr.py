import qrcode
import sys
import os

url = sys.argv[1]
print(f"Generating QR code for: {url}")

img = qrcode.make(url)
output_path = os.path.join(os.getcwd(), "connection_qr.png")
img.save(output_path)
print(f"QR code saved to {output_path}")
