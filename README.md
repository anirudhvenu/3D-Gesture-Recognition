# 3D-Gesture-Recognition
Gesture recognition provides a more natural way of communicating with computing machines. Even more so for people who are deaf, mute or those with speech defects where features such as speech recognition is out of the picture. This project aims at training an SVM to learn sign language gestures captured using a RGB-D camera.

The camera views the subject in the front plane and generates a depth image of the subject in the plane towards the Kinect&copy;. This depth image is then used for background removal, followed by generation of the depth profile of the subject. In addition to this, the difference between subsequent frames gives the motion profile of the subject and is used for recognition of gestures. [[1]](http://ieeexplore.ieee.org/abstract/document/6144864/) 

The Microsoft Research Cambridge-12 Kinect gesture data set has been used for this project. There are 12 dynamic American Sign Language (ASL) gestures, performed by 10 subjects.

#Program Listing:
  1. main2All.m: Processes and creates labels for the Microsoft Kinect dataset. A label is generated for each entry which is obtained by converting each frame of every video of every gesture into a string of integers based on a frequency distribution of the pixels.
  2. segment3.m: Called by main2all. Segments the image and returns the frequency count of pixels within each segment in the form of an array.
  3. svmClassification.py: Classifies the labeled dataset (test and train) with the help of multiclass SVM's. Performance metrics- confusion matrices as well as efficiency scores. 
