import cv2

import tensorflow as tf

from keras.preprocessing import image


import tensorflow.keras as k
import cv2
import numpy as np
import time

model = tf.keras.models.load_model('static\\gesture.h5')
face_cascade=cv2.CascadeClassifier("static\\haarcascade_frontalface_alt2.xml")
ds_factor=0.6

class VideoCamera(object):
    mask=0

    def __init__(self):

        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    def mask_status(self):
        return(self.mask)

    def get_frame(self):
        success, pic = self.video.read()
        pic=cv2.resize(pic,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
        #print(pic.shape)

        
        cv2.imshow('frame',gray)
        k=cv2.waitKey(5)&0xFF
        cv2.imwrite('static\\img.png',gray)






        path="static\\img.png"

        img = image.load_img(path, target_size=(150, 150))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)
        print(classes)
        


       

obj=VideoCamera()
while(1):
    obj.get_frame()