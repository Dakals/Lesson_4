from PIL import Image

image = Image.open("monro.jpg")
shift = 50

red, green, blue = image.split()

coordinates = (shift, 0, image.width, image.height)
cropped_red = red.crop(coordinates)
coordinates = (shift/2, 0, image.width - shift/2, image.height)
cropped_red_middle = red.crop(coordinates)
image_blend_red = Image.blend(cropped_red, cropped_red_middle, 0.5)

coordinates = (0, 0, image.width - shift, image.height)
cropped_blue = blue.crop(coordinates)
coordinates = (shift/2, 0, image.width - shift/2, image.height)
cropped_blue_middle = blue.crop(coordinates)
image_blend_blue = Image.blend(cropped_blue, cropped_blue_middle, 0.5)

coordinates = (shift/2, 0, image.width - shift/2, image.height)
cropped_green = green.crop(coordinates)

image_final = Image.merge('RGB', (image_blend_red, cropped_green, image_blend_blue))
image_final.save('image_final.jpg')
image_final.thumbnail((80, 80))
image_final.save('image_final_avatar.jpg')
