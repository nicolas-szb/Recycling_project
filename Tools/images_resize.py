from PIL import Image
from os import listdir
from os.path import isfile, join
from tqdm import tqdm

mypath_original = input("Path of the folder with image(s) to transform: ")
mypath_resized = input("Path of the folder for resized image(s): ")
target = int(input("Maximum dimension: ")) #1280 is good

print("Generating image(s)...")
print()

imageFiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and (f.endswith("G") or f.endswith("g")) ]

for im in tqdm(imageFiles) :
    im1 = Image.open(join(mypath_original, im))
    originalWidth, originalHeight = im1.size
    ratio = originalWidth / originalHeight
    if ratio > 1 :
        width = target
        height = int(width / ratio)
    else :
        height = target
        width = int(height * ratio)

    im2 = im1.resize((width, height), Image.ANTIALIAS) # linear interpolation in a 2x2 environment
    im2.save(join(mypath_resized, "".join([str(width),"x",str(height),"_",im])))

print("... Generating done!")
print()

# Count how many images are resized
print("{} image(s) resized".format(len(imageFiles)))
print()
