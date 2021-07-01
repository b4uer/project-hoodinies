#All the imports go here
import numpy as np
import cv2
import os
import shutil
from PIL import Image, ImageDraw

#Initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Variable store execution state
images_taken = False

#Starting the video capture
cam = cv2.VideoCapture(0)
ret,img = cam.read()

img_counter = 0

while(ret):
    ret,img = cam.read()
    #Coverting the recorded image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Applying filter to remove impurities
    gray = cv2.bilateralFilter(gray,5,1,1)

    #Detecting the face for region of image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(200,200))
    if((len(faces)>0)):
        for (x,y,w,h) in faces:
            #img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            img_crop = img[y:y+h, x:x+w]

            #cv2.putText(img,"Face detected",(100,100),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),2)
        img_name = "tmp/face_image_{}.png".format(img_counter)
        cv2.imwrite(img_name, img_crop)
        print("{} written!".format(img_name))
        img_counter += 1
 
    else:
        cv2.putText(img,"No face detected",(100,100),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),2)

    if(img_counter == 20):
        break

cam.release()
cv2.destroyAllWindows()

img_tmp = "tmp/face_image_9.png"

img_face = Image.open(img_tmp)
h,w = img_face.size      
 #Creating luminous image
lum_img = Image.new('L',[h,w] ,0) 
draw = ImageDraw.Draw(lum_img)
draw.pieslice([(50,0),(h-50,w)],0,360,fill=255)
        
face = Image.open(img_tmp)
frame = Image.open('shot12.JPG')
back_im = frame.copy()
back_im.paste(face,(285,180),lum_img)
back_im.save(img_tmp, quality=95)

original = r'C:\Users\potow\Documents\Python\Project\tmp\face_image_9.png'
target = r'C:\Users\potow\Documents\Python\Project\Image-Server\Photo.png'

shutil.copyfile(original, target)




  

