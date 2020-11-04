# Recycling Project with Yolov3
With the different categories of trash in our homes, waste sorting can be complicated. The aim of this project is to create a model which allows to differentiate 
the categories of waste and which returns to the user the corresponding waste category to use.

## First Step: Create dataset
The model needs labeled images of trash for training - glass bottles, plastic bottles, metal cans, paper, etc.

I begun with only one category in order to make a quick prototype of the model. This first category is "glass" which mostly includes wine or beer bottles and 
glasses, like example below.


![example](https://github.com/nicolas-szb/Recycling_project/blob/master/data/presentation/example.jpg)

### Collecting images
OIDv4_ToolKit allows to download pre-labeled images from https://storage.googleapis.com/openimages/web/index.html which contains a lot of categories. 
But every subcategories don't exist and in the "bottle" category you can find glass or plastic bottles.
Don't hesitate to download more thant the number of needed picture because some won't be interesting. I use about 800 pictures for a first test.

More information in [tools folder](https://github.com/nicolas-szb/Recycling_project/tree/master/Tools/OIDv4_ToolKit).
