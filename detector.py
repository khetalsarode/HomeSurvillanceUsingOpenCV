import cv2
import numpy as np
import time
from datetime import datetime
import message

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
#rec=cv2.createLBPHFaceRecognizer()
rec.read('recognizers\\trainingData.yml')
id=0
fontscale = 1
fontcolor = (0, 0, 255)
#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
font = cv2.FONT_HERSHEY_SIMPLEX
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(conf<100):
            if(id==1):
                id="khetal"
        else:
            id="unknown"
            #print("invalid")
            if(id=="unknown"):
                #time.sleep(2)
                cv2.putText(img, str(id), (x,y+h), font, fontscale, fontcolor,2)
                cv2.imwrite('capture.jpg', img)
                message.start()
                break
        #cv2.PutText(cv2.fromarray(img).str(id),(x,y+h),font,255)
        cv2.putText(img, str(id), (x,y+h), font, fontscale, fontcolor,2)
    cv2.putText(img,str(datetime.now()),(300,100), font, .5,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow("face",img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
