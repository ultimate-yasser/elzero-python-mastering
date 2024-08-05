from PIL import Image

pic = Image.open(r'part1\elzero-pillow.png')

l_letter = pic.crop((400, 0, 800, 400))
l_letter = l_letter.convert('L')
l_letter.save(r'part1\l_letter.png')

ero = pic.crop((0, 400, 1200, 800))
ero = ero.convert('L')
ero = ero.rotate(180)
ero.save(r'part1\ero.png')