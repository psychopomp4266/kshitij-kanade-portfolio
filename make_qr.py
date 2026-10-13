"""Make a print-ready QR code for your portfolio.

Usage:   python make_qr.py https://YOUR-SITE-URL
Needs:   pip install segno
Output:  qr.svg (vector, best for print) and qr.png (for screens and slides)
"""
import sys
import segno

if len(sys.argv) != 2 or not sys.argv[1].startswith("http"):
    sys.exit("Usage: python make_qr.py https://YOUR-SITE-URL")

url = sys.argv[1]
qr = segno.make(url, error="m")
qr.save("qr.svg", scale=10, border=4, dark="#101917", light="#ffffff")
qr.save("qr.png", scale=16, border=4, dark="#101917", light="#ffffff")
print(f"Saved qr.svg and qr.png for {url}")
