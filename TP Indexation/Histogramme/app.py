import numpy
from PIL import Image


def histogram(img):
    image_gray = img.convert('L')
    killy = numpy.array(image_gray)
    maximum = numpy.max(killy)
    minimum = numpy.min(killy)
    dim = maximum - minimum + 1
    hist, bins = numpy.histogram(killy, bins=dim)
    return hist


image1 = Image.open("image1.jpg")
hist1 = histogram(image1)

image2 = Image.open("image2.jpg")
hist2 = histogram(image2)

image3 = Image.open("image3.jpg")
hist3 = histogram(image3)

image4 = Image.open("image4.jpg")
hist4 = histogram(image4)

image5 = Image.open("image5.jpg")
hist5 = histogram(image5)

image6 = Image.open("image6.jpg")
hist6 = histogram(image6)

image7 = Image.open("image7.jpg")
hist7 = histogram(image7)

image8 = Image.open("image8.jpg")
hist8 = histogram(image8)

image9 = Image.open("image9.jpg")
hist9 = histogram(image9)

image10 = Image.open("image10.jpg")
hist10 = histogram(image10)


def calcul_distance(h1, h2):
    size1 = len(h1)
    size2 = len(h2)
    somme = 0
    somme2 = 0
    if size2 > size1:
        for i in range(size2):
            if i < size1:
                somme = somme + (min(h1[i], h2[i]))
            else:
                somme = somme + h2[i]
    else:
        for i in range(size1):
            if i < size2:
                somme = somme + (min(h1[i], h2[i]))
            else:
                somme = somme + h1[i]

    for i in range(size1):
        somme2 = somme2 + h1[i]
    distance = 1 - somme / somme2
    return distance


distance1 = calcul_distance(hist1, hist2)
distance2 = calcul_distance(hist1, hist3)
distance3 = calcul_distance(hist1, hist4)
distance4 = calcul_distance(hist1, hist5)
distance5 = calcul_distance(hist1, hist6)
distance6 = calcul_distance(hist1, hist7)
distance7 = calcul_distance(hist1, hist8)
distance8 = calcul_distance(hist1, hist9)
distance9 = calcul_distance(hist1, hist10)


dictionary = {"image2": distance1, "image3": distance2, "image4": distance3, "image5": distance4,
              "image6": distance5, "image7": distance6, "image8": distance7, "image9": distance8,
              "image10": distance9}

print("Order of similarity used the request image <<image1>> : ")
for w in sorted(dictionary, key=lambda x: dictionary[x] if x in dictionary else None, reverse=False):
    print(w, dictionary[w])
