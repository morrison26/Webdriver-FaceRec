import cv2
import json

from os import walk

filenames = []

for (_, _, files) in walk('photos'):
    filenames.extend(files)
    break

out = {}

for file in filenames:
    img = cv2.imread('photos/' + file)

    img_gs = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    haar = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')

    rect = haar.detectMultiScale(img_gs, scaleFactor = 1.2, minNeighbors = 5, minSize = (30, 30))

    out[file] = len(rect)

    for (x, y, w, h) in rect:
        cv2.rectangle(img, (x,y), (x+w, y+h), 2)

print(out)

with open('out2.json', 'w') as fp:
    json.dump(out, fp)

# for (x,y,w,h) in rect:
#     cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
#
# while True:
#     cv2.imshow('first',img)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
#
# cv2.destroyAllWindows()
