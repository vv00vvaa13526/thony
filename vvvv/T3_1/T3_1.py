from PIL import Image

image = Image.open('sus.jpeg')

icon_image = image.resize((150, 150), Image.LANCZOS)

icon_image.save("icon_sus.jpeg")

image.close()

icon_image.close()


image = Image.open('sas.webp')

icon_image = image.resize((150, 150), Image.LANCZOS)

icon_image.save("icon_sas.webp")

image.close()

icon_image.close()