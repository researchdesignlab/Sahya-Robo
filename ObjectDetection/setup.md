## Step1 - Requirements

  1.Python
  
  2.Tensorflow 
  
  ```
  pip install tensorflow 
  ``` 
  3.openCV
  ```
  pip install opencv
  ```
  
## Step2 - 
  Download the Darkflow repo

  https://github.com/thtrieu/darkflow

  extract the files somewhere locally

## Step3 - Build the library

  open an cmd window within darkflow-master folder and type
  ```
  python setup.py build_ext --inplace
  ```
  OR
  ```
  pip install -e .
  ```
## Step 4 - Download weights

  Download the YOLOv2 608x608 weights file here (https://pjreddie.com/darknet/yolov2/)

  create a bin folder within the darkflow-master folder

  put the weights file in the bin folder

## Commands to execute - 

  Navigate to darkflow-master

  put the provided code within this folder

  open a cmd within darkflow-master and type 
  ```
  python objdect.py
  ```
  
 ## Credits -
  Mark Jay
  
  https://github.com/markjay4k
