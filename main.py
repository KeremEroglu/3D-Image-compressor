from PIL import Image
import numpy as np
import json
from DistCalc import DistanceFromFocus, MaxDistance

with open("settings.json", "r") as file:
    setting = json.load(file)
    normalPhoto = setting["general"]["Normal photo"]
    depthPhoto = setting["general"]["Depth photo"]
    focalPoint = setting["general"]["Focal point"]
    distancex = setting["distance"]["dist x"]
    distancez = setting["distance"]["dist z"]

colorImage = Image.open(normalPhoto)
depthImage = Image.open(depthPhoto)

width = colorImage.size[0]
length = colorImage.size[1]

BWImage = colorImage.convert('L')

BWImage.save("../photos/output/OriginalBWImage.png")

colorImageArray = np.array(BWImage)
depthImageArray = np.array(depthImage)

max_dist = MaxDistance(width,length,distancex,distancez)

for i in range(0,length-1):
    newArray = []
    for j in range(0,width-1):
        newArray.append([i,j,depthImageArray[i][j], colorImageArray[i][j]])
        colorImageArray[i][j] = DistanceFromFocus(newArray[j],max_dist,focalPoint,distancex,distancez)

resultImage = Image.fromarray(colorImageArray)
resultImage.save("../photos/output/OutputImage4.png")