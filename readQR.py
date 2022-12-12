import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np
import webbrowser

def decode(image):
    return pyzbar.decode(image)

def display(image, decoded):
    for decode_object in decoded:
        points = decode_object.polygon
        
        if len(points) > 4:
            convex_hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            convex_hull = list(map(tuple, np.squeeze(convex_hull)))
        else:
            convex_hull = points;

        n = len(convex_hull)
        
        for j in range(0, n):
            cv2.line(image, convex_hull[j], convex_hull[(j+1)%n], (255,0,0), 3)
        
        cv2.imshow("result", image)
        cv2.waitKey(0)
        

# main(decoding, display)
if __name__ =='__main__':
    image = cv2.imread('QR.jpg')
    decoded = decode(image)
    qrDecoder = cv2.QRCodeDetector()
    data = qrDecoder.detectAndDecode(image)[0]
    webbrowser.open(data)
    display(image, decoded)
