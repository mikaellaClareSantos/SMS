from PIL import Image

im = Image.open('1.png')
print(im.size)

new_size = im.resize((100, 100))
new_size.show()