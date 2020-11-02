print()
print("This program needs three parameters:")
print("- the path of the folder where your original images are saved")
# e.g: /Documents/data-augmentation/images/
print("- the path of the folder where your transformed images will be saved")
# e.g: /Documents/data-augmentation/generated_dataset/
print("- the number of transformation by image")
# e.g: 50
print()

from os import listdir
from os.path import isfile, join
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
from tqdm import tqdm
from pathlib import Path

# Parameters
original_images_path = input("Path of the folder with image(s) to transform: ")
transformed_images_path = input("Path of the folder for transformed image(s): ")
transformed_images_total = input("Number of transformations by image: ")

# Add '/' at the end of the paths to avoid error
if original_images_path[-1] != '/':
    original_images_path = original_images_path + '/'

if transformed_images_path[-1] != '/':
    transformed_images_path = transformed_images_path + '/'

# Save all original images paths in original_folder list
original_folder = [(original_images_path+f) for f in listdir(original_images_path)
            if isfile(join(original_images_path, f))]

# Remove .DS_Store file created (sometimes) by MacOS
if Path(original_images_path + '.DS_Store').exists():
    original_folder.remove(original_images_path + '.DS_Store')

# Count how many images must be transformed
print()
print("{} image(s) will be transformed".format(len(original_folder)))
print()

print("Generating image(s)...")
print()

for original_image in tqdm(original_folder):
    # Transform image into numpy array
    image = load_img(original_image)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # Initialize the image generator
    aug = ImageDataGenerator(
        rotation_range=30,
        zoom_range=0.15,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.15,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode="nearest")

    # Initialize total of transformations
    total = 0

    # Construct the image generator
    imageGen = aug.flow(image, batch_size=1, save_to_dir=transformed_images_path,
        save_prefix="image", save_format="jpg")

    for image in imageGen:
        # Increment counter
        total += 1

        # Break loop when total of transformations is reached
        if total == int(transformed_images_total):
            break

print("... Generating done!")
print()

# Save all transformed images paths in transformed_folder list
transformed_folder = [(transformed_images_path+f) for f in listdir(transformed_images_path)
            if isfile(join(transformed_images_path, f))]

# Remove .DS_Store file created (sometimes) by MacOS
if Path(transformed_images_path + '.DS_Store').exists():
    transformed_folder.remove(transformed_images_path + '.DS_Store')

# Count how many images are saved in transformed_folder
print("{} image(s) created".format(len(transformed_folder)))
print()
