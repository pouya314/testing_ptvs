from io import BytesIO
from captcha.image import ImageCaptcha
import base64

image = ImageCaptcha()

captcha_text = 'humble'
data = image.generate(captcha_text)
assert isinstance(data, BytesIO)
image.write(captcha_text, 'out.png')

#print('data')
#print(type(data))
#print(type(data.getvalue()))
#print(str(data.getvalue()))

encoded = base64.b64encode(data.getvalue())
print(encoded)


#with open('out.png', 'r') as f:
#    c = f.read()
#    print(c)
