import cv2
import numpy as np
import datetime
import time


# create size of screen
date = time.time()

# get timestamp
print(date)
print('Loading image . . .')

# grab an input image
image_path = r"input\city.jpg"

file_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

try:
    # split all channels from the image (this order is correct)
    b, g, r, a = cv2.split(file_image)
except:
    b, g, r = cv2.split(file_image)

# discord's colors
disBlue = 114, 137, 218  # rgb(114, 137, 218)
disWhite = 255, 255, 255  # rgb(255, 255, 255)
disGray1 = 153, 170, 181  # rgb(153, 170, 181)
disGray2 = 44, 47, 51  # rgb(44, 47, 51)
disGray3 = 35, 39, 42  # rgb(35, 39, 42)


def getMaxColorAverage(b, g, r):

    maxB = 0
    maxG = 0
    maxR = 0

    for i in range(len(b)):
        for x in range(len(b[0])):

            if b[i][x] > maxB:
                maxB = int(b[i][x])

            if g[i][x] > maxG:
                maxG = int(g[i][x])

            if r[i][x] > maxR:
                maxR = int(r[i][x])
    print("calculated max colors RGB: ")
    print(maxR, maxG, maxB)
    maxAverage = (maxB + maxG + maxR)/3
    return maxAverage


maxAverage = getMaxColorAverage(b, g, r)

# set quartile ranges
Q1 = (maxAverage/5)*1
Q2 = (maxAverage/5)*2
Q3 = (maxAverage/5)*3
Q4 = (maxAverage/5)*4
Q5 = (maxAverage/5)*5

# for testing purposes set the quartiles manually
'''Q1 = 30  # disBlue
Q2 = 110  # disGray2
Q3 = 157  # disGray3
Q4 = 180  # disGray1
Q5 = 255  # disWhite'''


def type1(img):
    b, g, r = cv2.split(img)

    averageColor = 0
    toDivide = 0

    for i in range(len(img)):
        for z in range(len(img[0])):

            # create color cells
            if (b[i][z] < Q1):
                r[i][z] = disBlue[0]
                g[i][z] = disBlue[1]
                b[i][z] = disBlue[2]
            elif Q1 <= b[i][z] < Q2:
                r[i][z] = disGray2[0]
                g[i][z] = disGray2[1]
                b[i][z] = disGray2[2]
            elif Q2 <= b[i][z] < Q3:
                r[i][z] = disGray3[0]
                g[i][z] = disGray3[1]
                b[i][z] = disGray3[2]
            elif Q3 <= b[i][z] < Q4:
                r[i][z] = disGray1[0]
                g[i][z] = disGray1[1]
                b[i][z] = disGray1[2]
            elif Q4 <= b[i][z] <= Q5:
                r[i][z] = disWhite[0]
                g[i][z] = disWhite[1]
                b[i][z] = disWhite[2]

    # merge the necessary channels back together
    img = cv2.merge([b, g, r])
    return img


def type2noAlpha(b, g, r):

    for i in range(len(b)):
        for z in range(len(b[0])):

            averageColor = ((int(b[i][z])+int(g[i][z])+int(r[i][z]))/3)

            if (averageColor < Q1):
                r[i][z] = disBlue[0]
                g[i][z] = disBlue[1]
                b[i][z] = disBlue[2]
            elif Q1 <= averageColor < Q2:
                r[i][z] = disGray2[0]
                g[i][z] = disGray2[1]
                b[i][z] = disGray2[2]
            elif Q2 <= averageColor < Q3:
                r[i][z] = disGray3[0]
                g[i][z] = disGray3[1]
                b[i][z] = disGray3[2]
            elif Q3 <= averageColor < Q4:
                r[i][z] = disGray1[0]
                g[i][z] = disGray1[1]
                b[i][z] = disGray1[2]

            elif Q4 <= averageColor <= Q5:
                r[i][z] = disWhite[0]
                g[i][z] = disWhite[1]
                b[i][z] = disWhite[2]
            else:
                r[i][z] = disWhite[0]
                g[i][z] = disWhite[1]
                b[i][z] = disWhite[2]

    img = cv2.merge([b, g, r])
    return img


def type2(img):
    try:
        b, g, r, a = cv2.split(img)
    except:
        b, g, r = cv2.split(img)
        return type2noAlpha(b, g, r)

    averageColor = 0
    toDivide = 0

    maxR = 0
    maxG = 0
    maxB = 0

    for i in range(len(b)):
        for z in range(len(b[0])):
            if r[i][z] > maxR:
                maxR = r[i][z]

            if g[i][z] > maxG:
                maxG = g[i][z]

            if b[i][z] > maxB:
                maxB = b[i][z]

    maxAverage = (int(maxR)+int(maxG)+int(maxB))/3
    maxAverage = int(maxAverage)
    print(maxR, maxG, maxB, " with an maxColorAverage of : ", maxAverage)

    for i in range(len(img)):
        for z in range(len(img[0])):
            # if the pixel is completely transparent skip over it
            if not (a[i][z] > 0):
                pass

            else:

                averageColor = ((int(b[i][z])+int(g[i][z])+int(r[i][z]))/3)

            if (averageColor < Q1):
                r[i][z] = disBlue[0]
                g[i][z] = disBlue[1]
                b[i][z] = disBlue[2]
            elif Q1 <= averageColor < Q2:
                r[i][z] = disGray2[0]
                g[i][z] = disGray2[1]
                b[i][z] = disGray2[2]
            elif Q2 <= averageColor < Q3:
                r[i][z] = disGray3[0]
                g[i][z] = disGray3[1]
                b[i][z] = disGray3[2]
            elif Q3 <= averageColor < Q4:
                r[i][z] = disGray1[0]
                g[i][z] = disGray1[1]
                b[i][z] = disGray1[2]

            elif Q4 <= averageColor <= Q5:
                r[i][z] = disWhite[0]
                g[i][z] = disWhite[1]
                b[i][z] = disWhite[2]
            else:
                r[i][z] = disWhite[0]
                g[i][z] = disWhite[1]
                b[i][z] = disWhite[2]

    # merge all channels together as a new image
    img = cv2.merge([b, g, r, a])

    return img


# apply all effects to the initial image
final_image = type2(file_image)

# display on screen
cv2.imshow('drawn', final_image)

# save image
exportName = input("Enter a name for the image: ")
cv2.imwrite("output/"+str(exportName)+".png", final_image)

# exit on keypress
cv2.waitKey(0)
cv2.destroyAllWindows()
