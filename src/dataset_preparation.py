import os
import cv2

path = "/media/indra/DATA/Dataset/college/hand-number-recognition/videos"
target = "/media/indra/DATA/Dataset/college/hand-number-recognition/data/data2/nothing"

for root, dirs, files in os.walk(path):
    for file in files:
        print(file)
        vids = str(path + '/' + file)
        cap = cv2.VideoCapture(vids)
        img_number = 0

        while True:
            ret, frame = cap.read()

            if ret == True:
                # cv2.rectangle(frame, (10, 10), (200, 200), (255, 0, 0), 2)
                # x, y, w, h = 60, 80, 430, 580
                crop_img = frame[10:200, 10:200]
                # cv2.imshow('Frame', crop_img)
                crop_img = cv2.resize(crop_img, (420, 420))
                # cv2.imshow("Image", frame)
                file_split = file.split('.')

                # create folder
                if not os.path.exists(target + '/' + file_split[0]):
                    os.makedirs(target + '/' + file_split[0])

                # else:
                if img_number % 10 == 0:
                    print(str(target) + '/' + 'img_nothing_' +
                          str(file_split[0]) + str(img_number) + '.png')
                    cv2.imwrite(
                        str(target) + '/' + 'img_nothing_' +
                        str(file_split[0]) + str(img_number) + '.png',
                        crop_img)

                img_number += 1

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            else:
                break

        cap.release()

        cv2.destroyAllWindows()
