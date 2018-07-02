import os
import cv2

cap = cv2.VideoCapture(1)
img_number = 0

path = '/media/indra/DATA/Dataset/college/hand-number-recognition/data/data3/nothing/'

while True:
    ret, frame = cap.read()

    if ret == True:
        # cv2.rectangle(frame, (120, 50), (540, 470), (255, 0, 0), 2)
        # x, y, w, h = 60, 80, 430, 580
        crop_img = frame[50:470, 120:540]
        cv2.imshow('Frame', crop_img)

        # create folder
        if not os.path.exists(target + '/' + file_split[0]):
            os.makedirs(target + '/' + file_split[0])

        else:
            if img_number % 5 == 0:
                print(path + 'img_' + str(img_number) + '.png')
                cv2.imwrite(path + 'img_' + str(img_number) + '.png', crop_img)

        img_number += 1

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()
