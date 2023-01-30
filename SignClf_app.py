import cv2
import numpy as np
import streamlit as st
import sklearn 
from tensorflow import keras
from keras import models

model2 = keras.models.load_model('C:/Users/SUNDARESAN C G\Documents/ML/signing_classifier/signingmodel1.h5')


def preprocess(img):

  image_1_resize = cv2.resize(img,(256,256))
  image_1_b_w = cv2.cvtColor(image_1_resize, cv2.COLOR_BGR2GRAY)
  return image_1_b_w


def abs_diff(img1, img2):

  absdiff = cv2.absdiff(img1,img2)
  return absdiff


run = st.checkbox('Run')

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)


while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.waitKey(0)
    _, frame1 = camera.read()
    img1 = preprocess(frame)
    img2 = preprocess(frame1)
    res = abs_diff(img1,img2)

    #FRAME_WINDOW.image(res)
    res1 = np.dstack([res,res,res])
    res1 = np.expand_dims(res1,axis=0)
    pred = model2.predict(res1)

    if pred==0:
        text = "Signing"
    else:
        text = "Not Signing"
    
    def jls_extract_def():
        
        return 

    font = cv2.FONT_HERSHEY_SIMPLEX = jls_extract_def()
    display = cv2.putText(frame,text,(50,50),font,2,(0,0,0),2,cv2.LINE_4)

    FRAME_WINDOW.image(display)


else:

    st.write('Stopped')




