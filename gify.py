import os
import re
from PIL import Image

folder_ze_zdjeciami = "./frog_1"

pliki = [f for f in os.listdir(folder_ze_zdjeciami) if f.endswith(('.png', '.jpg', '.jpeg'))]

def wyciagnij_iteracje(nazwa_pliku):
    znalezione = re.findall(r'(\d+)\.[^.]+$', nazwa_pliku)
    return int(znalezione[0]) if znalezione else 0

pliki = sorted(pliki, key=wyciagnij_iteracje)
print("Sprawdzam kolejność pierwszych 5 plików:")
for p in pliki[:5]:
    print(p)
print("-" * 30)
obrazy = [Image.open(os.path.join(folder_ze_zdjeciami, f)) for f in pliki]

if obrazy:
    obrazy[0].save(
        "frog_1.gif",
        save_all=True,
        append_images=obrazy[1:],
        duration=250, 
        loop=1 
    )
    print("done")
else:
    print("błąd")