"""import cv2
import os
from PIL import Image


def detectFaces(image_name):
    img = cv2.imread(image_name)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    print(face_cascade)
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img #if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)#1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    result = []
    for (x,y,width,height) in faces:
        result.append((x,y,x+width,y+height))
    return result

def saveFaces(image_name):
    faces = detectFaces(image_name)
    print (faces)
    if faces:
        #将人脸保存在save_dir目录下。
        #Image模块：Image.open获取图像句柄，crop剪切图像(剪切的区域就是detectFaces返回的坐标)，save保存。
        save_dir = image_name.split('.')[0]+"_faces"
        os.mkdir(save_dir)
        count = 0
        for (x1,y1,x2,y2) in faces:
            file_name = os.path.join(save_dir,str(count)+".jpg")
            Image.open(image_name).crop((x1,y1,x2,y2)).save(file_name)
            count+=1

saveFaces("img531.jpg")"""
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