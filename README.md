# Hand Number Recognition

This repo contains script for training and testing Hand Number Recognition. We collect dataset manually using usb webcam and split it into images. Training the model is done using Keras with Tensorflow backend.

## Requirements
* Python 3.6
* Keras 2.4
* Tensorflow 1.3
* Scikit-learn
* OpenCV 3
* Imutils
* Argparse

## Download the model
You can download the dataset [here](https://drive.google.com/file/d/1itTa-Pf70cQnPwgY8EDYRPvNv9GUtxU8/view?usp=sharing)

## Testing
For testing model using webcam with parameters -m for models, -l for label and -i for input video.

    $ python src/classify_video.py -m models/lenet_64x64/hnr_lenet_150x150.model -l models/lenet_64x64/lb.pickle -i videos.mp4

## Credits
[1. Pyimagesearch Image Classification with Keras and Deep Learning](https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/)

## Contact
If you have questions please email me at indrango@gmail.com.