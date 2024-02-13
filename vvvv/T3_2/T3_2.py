from PIL import Image

image1 = Image.open('sus.jpeg')
new_image1 = image1.crop((0,0,960,1920))
new_image1.save("new_sus1.jpeg")
image1.close()
new_image1.close()


image2 = Image.open('sus.jpeg')
new_image2 = image2.crop((960,0,1920,1920))
new_image2.save("new_sus2.jpeg")
image2.close()
new_image2.close()

