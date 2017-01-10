# 3D-Gesture-Recognition
3D gesture recognition trained using multiclass SVM's.
Definition of files:
  1. main2All.m: Processes and creates labels for the Microsoft Kinect dataset. A label is generated for each entry which is obtained by converting each frame of every video of every gesture into a string of integers based on a frequency distribution of the pixels.
  2. segment3.m: Called by main2all. Segments the image and returns the frequency count of pixels within each segment in the form of an array.
  3. svmClassification.py: Classifies the labeled dataset (test and train) with the help of multiclass SVM's. Performance metrics- confusion matrices as well as efficiency scores. 
