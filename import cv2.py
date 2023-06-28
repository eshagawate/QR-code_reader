import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
import webbrowser
import requests
import cv2

TOKEN = '6028168312:AAGG3fJ7uo_rA99U0t4p1a22YxOHh2oG9Uk'
chat_id = "1314511223"
  

#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
 
url='http://192.168.1.9/'
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
 
prev=""
pres=""
while True:
    img_resp=urllib.request.urlopen(url+'cam-hi.jpg')
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    #_, frame = cap.read()
 
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        pres=obj.data
        if prev == pres:
            pass
        else:
            print("Type:",obj.type)
            print("Data: ",obj.data)
            prev=pres
            u = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={pres}"
            requests.get(u).json # this sends the message
            
            # Open the URL using open() function of module  
            #webbrowser.open_new_tab(pres)
            
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
        
          
        
 #"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
    cv2.imshow("live transmission", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cv2.destroyAllWindows()