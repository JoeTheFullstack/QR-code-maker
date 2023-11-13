import qrcode
img = qrcode.make('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
type(img) # qrcode.image.pil.pilImage
img.save("Some_data2.png")
