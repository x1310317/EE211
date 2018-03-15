import cv2
import sys
import os.path
from glob import glob

if __name__ == '__main__':
    if os.path.exists('faces_extract') is False:
        os.makedirs('faces_extract')
    file_list = glob('original_image/*.jpg')
    for filename in file_list:
        cascade = cv2.CascadeClassifier("lbpcascade_animeface.xml")
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(48, 48))
        for i, (x, y, w, h) in enumerate(faces):
            face = image[y: y + h, x:x + w, :]
            face = cv2.resize(face, (256, 256))
            save_filename = '%s.jpg' % (os.path.basename(filename).split('.')[0])
            cv2.imwrite("faces_extract/" + save_filename, face)