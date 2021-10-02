from requests_html import HTMLSession
from random import randint
import time
import os

item = "car"
s = HTMLSession()
r = s.get(f"https://www.google.com/search?q={item}&hl=en&tbm=isch")
r.html.render(timeout=10, scrolldown=2500)
time.sleep(4)

images = r.html.find('img[jsname="Q4LuWd"]')
image_url_list = []

try:
    for image in images:
        if "data" not in image.attrs["src"]:
            image_url_list.append(image.attrs["src"])
except:
    pass

for i, link in enumerate(image_url_list):
    response = s.get(link)

    newpath = f"{item}"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    with open(f"{newpath}/{i}.png", "wb") as w:
        w.write(response.content)

    print(link)

print(len(image_url_list))


next_link = r.html.find('a[jslog="11106"]')

for link in next_link:
    if link:
        if len(image_url_list) < 1001:
            response = s.get(f"https://www.google.com/{link.attrs['href']}")
            r.html.render(timeout=10, scrolldown=2500)
            time.sleep(4)

            images = r.html.find('img[jsname="Q4LuWd"]')

            try:
                for image in images:
                    if "data" not in image.attrs["src"]:
                        image_url_list.append(image.attrs["src"])
            except:
                pass

            for link in image_url_list:
                response = s.get(link)

                newpath = f"{item}"
                with open(f"{newpath}/{randint(10,10000)}.png", "wb") as w:
                    w.write(response.content)

                print(link)

            print(len(image_url_list))
    else:
        break    
    
