
# path to the folder containing the images
folder1 = Path to Synthetic Data
folder2 = Path to real Data

import csv
import numpy as np
from scipy import signal
from scipy.stats import pearsonr
from imageio import imread
import os

# function to find the correlation between two images
def find_correlation(image1, image2):
  # read the images and convert them to grayscale
  img1 = imread(image1, as_gray=True)
  img2 = imread(image2, as_gray=True)

  # compute the correlation using scipy's built-in function
  correlation, pvalue = pearsonr(img1.flatten(), img2.flatten())

  return correlation

# path to the target image
target_image = "path/to/target_image.png"

images1 = os.listdir(folder1)

for image in images1:

  target_image = os.path.join(folder1, image)
  
  # list the images in the folder
  images = os.listdir(folder2)

  # compute the correlations with the target image
  correlations = []
  for img in images:
    correlations.append(find_correlation(os.path.join(folder2, img), target_image))

  # find the index of the image with the maximum correlation
  max_index = np.argmax(correlations)

  # print the maximum correlation and the corresponding image
  print("***********************************************")
  print("Source Image : ", image)
  print("Maximum correlation:", correlations[max_index])
  print("Image:", images[max_index])
  coo= correlations[max_index]
  ioo = images[max_index]
  row = [image, ioo, coo]
  with open("output.csv", "a", newline="") as f:
  # create a CSV writer
    writer = csv.writer(f)
    # write each row to the CSV file
    writer.writerow(row)



