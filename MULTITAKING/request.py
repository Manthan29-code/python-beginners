#request library in pythin is used to downlode image (or many other things) via link of this image 

import requests

url="https://pbs.twimg.com/profile_images/1328238100/bola_bitfarma_200x200.jpg"
responce=requests.get(url)
if responce:
   open("Highresolutionimage.jpg","wb").write(responce.content) # don't forgot to write sutable extension of file
print(responce)