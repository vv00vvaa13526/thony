from PIL import Image

image1 = Image.open('1.jpg')
width_image1 = image1.width
height_image1 = image1.height
new_image1 = image1.crop((0,0,height_image1,height_image1))
new_image1.save("new_1.jpg")
image1.close()
new_image1.close()

image2 = Image.open('22.jpg')
width_image2 = image2.width
height_image2 = image2.height
new_image2 = image2.crop((0,0,width_image2, width_image2))
new_image2.save("new_22.jpg")
image2.close()
new_image2.close()

image3 = Image.open('333.jpg')
width_image3 = image3.width
height_image3 = image3.height
new_image3 = image3.crop((0,0,height_image3, height_image3))
new_image3.save("new_333.jpg")
image1.close()
new_image3.close()