from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-m", "--model", required=True, help="path to trained model model")
ap.add_argument(
    "-l", "--labelbin", required=True, help="path to label binarizer")
ap.add_argument("-i", "--input", help="path to input")
args = vars(ap.parse_args())

# load the image
print('[INFO] loading videos')
cap = cv2.VideoCapture(args["input"])

# load the trained convolutional neural network and the label binarizer
print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())

while True:
    ret, frame = cap.read()

    if ret == True:
        cv2.rectangle(frame, (120, 50), (540, 470), (255, 0, 0), 2)
        # x, y, w, h = 60, 80, 430, 580
        crop_img = frame[50:470, 120:540]
        output = frame.copy()

        # pre-process the image for classification
        image = cv2.resize(crop_img, (64, 64))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        # classify the input image
        proba = model.predict(image)[0]
        idx = np.argmax(proba)
        label = lb.classes_[idx]

        # build the label and draw the label on the image
        label = "Predicted {}: {:.2f}%".format(label, proba[idx] * 100)
        cv2.putText(output, label, (180, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                    (0, 0, 0), 2)

        # show the output image
        cv2.imshow("Output", output)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()
