import cv2

# 1 ...Loads The Orignal Picture ......

test=cv2.imread("g4.png",)
cv2.imshow("display",test)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2....Converts Orignal Picture into Gray Color For More Effiency ....

grayImg= cv2.cvtColor(test,cv2.COLOR_RGB2GRAY)
cv2.imshow("display",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Loads Haar scale classifier For Eyes ........
'''hfc = cv2.CascadeClassifier('C:\\Users\\Ali\\PycharmProjects\\FaceDetection\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')
faces = hfc.detectMultiScale(test, scaleFactor=1.05, minNeighbors=5)

for (x,y,w,h) in faces:
    cv2.circle(test,(x,y),(x+w,y+h),(0,255,0),2)'''

# Loads Haar scale classifier For Face Detection ........

hfc = cv2.CascadeClassifier('C:\\Users\\Ali\\PycharmProjects\\FaceDetection\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml')
faces = hfc.detectMultiScale(test, scaleFactor=1.05, minNeighbors=5)

for (x,y,w,h) in faces:
    cv2.rectangle(test,(x,y),(x+w,y+h),(0,255,0),8)


cv2.imshow("display", test)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Faces Found" ,len(faces))