from Sticher import Sticher
import imutils
import cv2
import numpy as np

def removeBlank(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)

    ret, thresh = cv2.threshold(gray, 1, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    max_area = -1
    best_cnt = None

    for cnt in contours:

        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt

    approx = cv2.approxPolyDP(best_cnt, 0.01 * cv2.arcLength(best_cnt, True), True)
    far = approx[np.product(approx, 2).argmax()][0]
    ymax = approx[approx[:, :, 0] == 1].max()
    xmax = approx[approx[:, :, 1] == 1].max()
    x = min(far[0], xmax)
    y = min(far[1], ymax)

    img2 = img[:y, :x].copy()
    return img2

def read(listImage):
    img=[]
    for l in listImage:
        i=cv2.imread(l)
        i=imutils.resize(i, width=400)
        img.append(i)
    return img

def stich(list):
    imageList=read(list)
    sticher = Sticher()
    print len(imageList)
    x=0
    im=None
    for x in (0, len(imageList)-1):
        if x<1:
            imageA=imageList[x]
            imageB=imageList[x+1]
            (result, vis) = sticher.stitch([imageA, imageB], showMatches=True)
            result=removeBlank(result)
            x+=1
            continue
        else:
            print x
            image=imageList[x]
            #cv2.imshow("Result", image)
            (result, vis) = sticher.stitch([result,image], showMatches=True)
            result = removeBlank(result)
        print x
    cv2.imshow("Result", result)

    cv2.waitKey(0)
