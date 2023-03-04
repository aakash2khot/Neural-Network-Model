STUDENT_ROLLNO = yourRollNumberHere #yourRollNumberHere
STUDENT_NAME = yourNameHere #yourNameHere
#@PROTECTED_1
##DO NOT MODIFY THE BELOW CODE. NO OTHER IMPORTS ALLOWED. NO OTHER FILE LOADING OR SAVING ALLOWED.
import torch.nn as nn 
import torch.optim as optim 
import torchmetrics
import sklearn.preprocessing as preprocessing
import sklearn.model_selection as model_selection 
import torch.utils.data as data 
import numpy as np 
X_train = np.load("X_train.npy")
y_train = np.load("y_train.npy")
X_test = np.load("X_test.npy")
submission = np.load("sample_submission.npy")
#@PROTECTED_1

#@PROTECTED_2
np.save("{}__{}".format(STUDENT_ROLLNO,STUDENT_NAME))
#@PROTECTED_2