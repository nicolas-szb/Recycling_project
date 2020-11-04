# Recycling Project with Yolov3
With the different categories of trash in our homes, waste sorting can be complicated. The aim of this project is to create a model which allows to differentiate 
the categories of waste and which returns to the user the corresponding waste category to use.


## First Step: Create dataset
The model needs labeled images of trash for training - glass bottles, plastic bottles, metal cans, paper, etc.

I begun with only one category (or classe) in order to make a quick prototype of the model. This first category is "glass" which mostly includes wine or beer bottles and glasses, like example below.


| ![example](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/example.jpg) |
|---|


I create my dataset with the following four steps.

### Collecting images
OIDv4_ToolKit allows to download pre-labeled images from https://storage.googleapis.com/openimages/web/index.html which contains a lot of categories. 
But every subcategories don't exist and in the "bottle" category you can find glass or plastic bottles.
Don't hesitate to download more thant the number of needed picture because some won't be interesting.

I downloaded about 1000 images for this first test.

More information about OIDv4_ToolKit in [Tools folder](https://github.com/nicolas-szb/Recycling_project/tree/master/Tools).

### Resizing images
You can resize images in order to reduce the final weight of the pictures folder with the following command in terminal. You only must choose the maximum dimension value and the other dimension will be proportional:
```bash
# In the folder containing images_resize.py
python images_resize.py
```

The modified dimension is always the width so a rotate will be performed on the picture if it was portrait oriented.

I chosen a maximum dimension egals to 1280 and found good results.<br/>
Example of resized picture:

| ![original_image](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/original_image.jpeg) | ![resized_image](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/resized_image.jpeg) |
|---|---|


| Picture | Size | Weight |
|---|---|---|
| Original on left | 3024x4032 | 1,8Mo |
| Resized on right | 1280x960 | 102ko |

You can find the code in [Tools folder](https://github.com/nicolas-szb/Recycling_project/blob/master/Tools/images_resize.py).

### Performing data augmentation
If you don't have enough pictures, you can perform a data augmentation. It can be very interesting because you should preferably have 2000 different images per classe if you want a well trained model. 
```bash
# In the folder containing images_augmentation.py
python images_augmentation.py
```

In the example below, I choosen the previous resized picture and applied 4 transformations on it:

| ![augmented_1_image](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/augmented_1_image.jpg) | ![augmented_2_image](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/augmented_2_image.jpg) |
|---|---|
| ![augmented_3_image](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/augmented_3_image.jpg) | ![augmented_4_image](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/augmented_4_image.jpg) |


You can find the code in [Tools folder](https://github.com/nicolas-szb/Recycling_project/blob/master/Tools/images_augmentation.py).

### Creating images annotations
labelImg is a great tool to label your custom images. OIDv4_ToolKit downloads images and associated labels but when your custom category is not in the "predefini" list, you have to manually annotate images.

In my case, "Glass" is not a category so I created by myself as following:

| ![labeled_image](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/labeled_image.jpeg) |
|---|


This is a very long activity when about 2000 pictures per classe are needed.

More information about labelImg in [Tools folder](https://github.com/nicolas-szb/Recycling_project/tree/master/Tools).

### Conclusion
I finally collected and labeled 721 images which will be used for a first one-classe Yolov3 model.
