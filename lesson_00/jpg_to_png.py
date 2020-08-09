import PIL.Image as Img

im0 = Img.open('../resources/coast.jpg')
print(im0.size, im0.mode)

im1 = im0.convert('L')
im1.thumbnail((1000, 1000))
print(im1.size, im1.mode)

im1.save('../resources/coast.png')
