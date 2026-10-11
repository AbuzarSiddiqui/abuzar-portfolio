# One-off: favicon set + 1200x630 social share card. Run from the site root: python scripts/make_icons.py
from PIL import Image, ImageDraw, ImageFont

INK, PAPER, ACCENT = (15, 17, 21), (246, 245, 241), (47, 69, 232)
SERIF_I = 'C:/Windows/Fonts/georgiai.ttf'
SANS, SANS_B = 'C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/segoeuib.ttf'

def mark(size):
    im = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=size * 0.22, fill=INK)
    f = ImageFont.truetype(SERIF_I, int(size * 0.72))
    d.text((size / 2, size * 0.53), 'A', font=f, fill=PAPER, anchor='mm')
    return im

mark(512).resize((180, 180), Image.LANCZOS).save('apple-touch-icon.png')
mark(512).resize((192, 192), Image.LANCZOS).save('icon-192.png')
mark(512).save('icon-512.png')
mark(256).save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])

# Social card
W, H = 1200, 630
card = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(card)
photo = Image.open('abuzar-siddiqui-headshot.jpg').convert('RGB').resize((360, 360), Image.LANCZOS)
m = Image.new('L', (360, 360), 0); ImageDraw.Draw(m).ellipse((0, 0, 359, 359), fill=255)
card.paste(photo, (780, 135), m)
d.ellipse((772, 127, 1148, 503), outline=ACCENT, width=4)
card.paste(mark(72), (80, 72), mark(72))
d.text((168, 108), 'abuzarsiddiqui.in', font=ImageFont.truetype(SANS, 30), fill=(100, 106, 117), anchor='lm')
d.text((80, 250), 'Abuzar Ahmed', font=ImageFont.truetype(SANS_B, 76), fill=INK, anchor='ls')
d.text((80, 340), 'Siddiqui', font=ImageFont.truetype(SANS_B, 76), fill=INK, anchor='ls')
d.text((80, 410), 'AI Product Manager', font=ImageFont.truetype(SERIF_I, 46), fill=ACCENT, anchor='ls')
d.text((80, 470), 'Agentic AI & SaaS · Articles · Free AI courses', font=ImageFont.truetype(SANS, 30), fill=(43, 47, 54), anchor='ls')
d.rectangle((0, H - 14, W, H), fill=ACCENT)
card.save('og-image.jpg', quality=88, optimize=True)
print('icons + og-image.jpg written')
