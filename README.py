# naive-bayes
naive bayes application

use the naive bayes can you identify the who is the author of new email or unseen email

Use a Naive Bayes Classifier to identify emails by their authors

"""
 authors and labels:
    kashish has label 0
    honey has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

