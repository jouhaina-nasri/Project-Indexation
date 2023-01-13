import numpy
from PIL import Image
import cv2


# Convert image RVB to gray #
def convert_gris(image):
    image_gray = image.convert('L')
    image_reduce = image_gray.resize((4, 4))
    killy = numpy.array(image_reduce)
    return killy
########################################################################

# Extract the elements of the matrix(3,3) except the element to calculate#
def number_occurrence(matrix, i, j):
    result = []
    for a in range(i - 1, i + 2, 1):
        for b in range(j - 1, j + 2, 1):
            if i != a or j != b:
                result.append(matrix[a][b])
    return result
#######################################################

# Fill new matrix by frequencies #
def matrix_correlogram(matrix_corr, x, y, freq):
    z = matrix_corr[x][y]
    t = len(matrix_corr)
    for i in range(t):
        for j in range(t):
            matrix_corr[x][y] = z + freq
    return matrix_corr
####################################

# Apply the correlogram #
def calcul(matrix, matrix_corr, result, k, h):
    list_number = list(set(result))
    size = len(list_number)
    for i in range(size):
        frequency = result.count(list_number[i])
        matrix_corr = matrix_correlogram(matrix_corr, matrix[k][h], list_number[i], frequency)
    return matrix_corr
##############################

# Apply the correlogram for each element #
def correlogram(matrix, matrix_corr, n, m):
    for i in range(n - 2):
        for j in range(m - 2):
            result = number_occurrence(matrix, i + 1, j + 1)
            matrix_corr = calcul(matrix, matrix_corr, result, i + 1, j + 1)
    return matrix_corr
#############################################

# Apply the correlogram to image #
def images(matrix):
    maximum = numpy.max(matrix)
    matrix_corr = numpy.zeros((maximum + 1, maximum + 1))
    n = len(matrix)
    m = len(matrix[1])
    return correlogram(matrix, matrix_corr, n, m)
###########################################


# Matrix descriptors : principal diagonal #
def signature(image):
    matrix = convert_gris(image)
    matrix_corr = images(matrix)
    descriptor = numpy.diag(matrix_corr)
    return descriptor
########################################


# distance intersection of histograms #
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
############################################################


image1 = Image.open("image1.jpg")
signature1 = signature(image1)

image2 = Image.open("image2.jpg")
signature2 = signature(image2)

image3 = Image.open("image3.jpg")
signature3 = signature(image3)

image4 = Image.open("image4.jpg")
signature4 = signature(image4)

image5 = Image.open("image5.jpg")
signature5 = signature(image5)

image6 = Image.open("image6.jpg")
signature6 = signature(image6)

image7 = Image.open("image7.jpg")
signature7 = signature(image7)

image8 = Image.open("image8.jpg")
signature8 = signature(image8)

image9 = Image.open("image9.jpg")
signature9 = signature(image9)

image10 = Image.open("image10.jpg")
signature10 = signature(image10)


distance1 = calcul_distance(signature1, signature2)
distance2 = calcul_distance(signature1, signature3)
distance3 = calcul_distance(signature1, signature4)
distance4 = calcul_distance(signature1, signature5)
distance5 = calcul_distance(signature1, signature6)
distance6 = calcul_distance(signature1, signature7)
distance7 = calcul_distance(signature1, signature8)
distance8 = calcul_distance(signature1, signature9)
distance9 = calcul_distance(signature1, signature10)

dictionary = {"image2": distance1, "image3": distance2, "image4": distance3, "image5": distance4,
              "image6": distance5, "image7": distance6, "image8": distance7, "image9": distance8,
              "image10": distance9}

print("Order of similarity used the request image <<image1>> : ")
for w in sorted(dictionary, key=lambda x: dictionary[x] if x in dictionary else None, reverse=False):
    print(w, dictionary[w])
