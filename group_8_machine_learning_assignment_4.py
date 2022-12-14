# -*- coding: utf-8 -*-
"""Group_8_Machine_Learning_Assignment_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CgJFBf0r9Hc9js783LEYCEZ8dj0iTfpW

# **Group 8 Assignment 4**

## **Import Important Libraries and load the dataset**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd #for working with dataframes
import numpy as np #to deal with arrays
import matplotlib.pyplot as plt #for plotting
import seaborn as sns
# %matplotlib inline

columns = ['pixel ' + str(i) for i in range(17)]
columns[-1] = 'label'
#load the train dataset
train = pd.read_csv('/content/pendigits-tra.csv',names=columns)
train.head()

#get some information about the train dataset
train.info()

#count the numbers occurrence in label column
sns.countplot(train['label'])

#split the data into x_train and y_train
x_train = train.drop('label',axis= 1)
y_train = train['label']

columns = ['pixel ' + str(i) for i in range(17)]
columns[-1] = 'label'
#load the test dataset
test = pd.read_csv('/content/pendigits-tes.csv',names=columns)
test.head()

#count the numbers occurrence in label column
sns.countplot(test['label'])

#split the test dataset into x_test and y_test
x_test = test.drop('label',axis= 1)
y_test = test['label']

"""## **Train the Decision Tree classification Model**

Decision Tree is a Supervised learning technique that can be used for both classification and Regression problems, but mostly it is preferred for solving Classification problems. It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.
"""

from sklearn.tree import DecisionTreeClassifier #for DT model
from sklearn.metrics import classification_report,accuracy_score,plot_confusion_matrix

dt = DecisionTreeClassifier(random_state=0)
dt.fit(x_train,y_train)
y_pred = dt.predict(x_test)

#print accuracy of DT model 
print('Accuracy ', accuracy_score(y_test,y_pred))

#print classification report of DT model 
print(classification_report(y_test,y_pred))

#print confusion matrix of DT model 
plot_confusion_matrix(dt,x_test,y_test)

"""## **Train SVM model**

SVM offers very high accuracy compared to other classifiers such as logistic regression, and decision trees. It is known for its kernel trick to handle nonlinear input spaces. It is used in a variety of applications such as face detection, intrusion detection, classification of emails, news articles and web pages, classification of genes, and handwriting recognition.
"""

from sklearn.svm import SVC
#train SVM model
svm = SVC(random_state=0)
svm.fit(x_train,y_train)
y_pred = svm.predict(x_test)

#print accuracy score for SVM model
print('Accuracy ', accuracy_score(y_test,y_pred))

#print classification model for SVM model
print(classification_report(y_test,y_pred))

#print confusion matrix for SVM model
plot_confusion_matrix(svm,x_test,y_test)

"""## **Apply Hard and soft Voting Classifiers**

Hard voting entails picking the prediction with the highest number of votes.

soft voting entails combining the probabilities of each prediction in each model and picking the prediction with the highest total probability.
"""

from sklearn.ensemble import VotingClassifier
#train the hard voting classifier
hard_votting = VotingClassifier(estimators=[('dt', dt), ('svm', svm)], voting='hard')
hard_votting.fit(x_train, y_train)
y_pred = hard_votting.predict(x_test)

#print accuracy score of hard voting classifier
print('Accuracy ', accuracy_score(y_test,y_pred))

#print classification report of hard voting classifier
print(classification_report(y_test,y_pred))

#print aconfusion matrix of hard voting classifier
plot_confusion_matrix(hard_votting,x_test,y_test)

"""### **Apply Soft Voting Classifier**"""

#train the soft voting classifier
svm = SVC(probability=True)
soft_votting = VotingClassifier(estimators=[('dt', dt), ('svm', svm)], voting='soft')
soft_votting.fit(x_train, y_train)
y_pred = soft_votting.predict(x_test)

#print accuracy score of soft voting classifier
print('Accuracy ', accuracy_score(y_test,y_pred))

#print classification report of soft voting classifier
print(classification_report(y_test,y_pred))

#print aconfusion matrix of soft voting classifier
plot_confusion_matrix(soft_votting,x_test,y_test)

"""## **Apply Bagging Classifier**

A Bagging classifier is an ensemble meta-estimator that fits base classifiers each on random subsets of the original dataset and then aggregate their individual predictions (either by voting or by averaging) to form a final prediction.
"""

from sklearn.ensemble import BaggingClassifier
scores =[]
for i in [30,70,100,150,200]:
  ba = BaggingClassifier(n_estimators=i,random_state=0)
  ba.fit(x_train,y_train)
  y_pred = ba.predict(x_test)
  print('Accuracy ', accuracy_score(y_test,y_pred))
  print(classification_report(y_test,y_pred))
  plot_confusion_matrix(ba,x_test,y_test)
  scores.append(accuracy_score(y_test,y_pred))

scores.append(accuracy_score(y_test,y_pred))

#plot n_estimator Vs accuracy 
plt.plot([30,70,100,150,200],scores)
plt.title('n_estimator Vs accuracy')
plt.xlabel('n_estimator')
plt.ylabel('accuracy')

"""**So, the highest accuracy is at n estimator = 150**

### **Train bagging classifier with the best number of estimator**
"""

ba = BaggingClassifier(n_estimators=150,random_state=0)
ba.fit(x_train,y_train)
y_pred = ba.predict(x_test)
print('Accuracy ', accuracy_score(y_test,y_pred))

print(classification_report(y_test,y_pred))

plot_confusion_matrix(ba,x_test,y_test)

"""## **Apply Random Forest classifier (additional model)**

A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.
"""

from sklearn.ensemble import RandomForestClassifier
scores =[]
for i in [30,70,100,150,200]:
  rf = RandomForestClassifier(n_estimators=i,random_state=0)
  rf.fit(x_train,y_train)
  y_pred = rf.predict(x_test)
  #accuracy score for random forest
  print('Accuracy ', accuracy_score(y_test,y_pred))
   #classification report for random forest
  print(classification_report(y_test,y_pred))
   #confusion matrix for random forest
  plot_confusion_matrix(rf,x_test,y_test)
  scores.append(accuracy_score(y_test,y_pred))

#plot numbers of estimators Vs. accuracy scores
plt.plot([30,70,100,150,200],scores)
plt.title('n_estimator Vs accuracy')
plt.xlabel('n_estimator')
plt.ylabel('accuracy')

"""**So, the highest accuracy is at n = 200**

### **Train random forest with estimator = 200**
"""

rf = RandomForestClassifier(n_estimators=200,random_state=0)
rf.fit(x_train,y_train)
y_pred = rf.predict(x_test)
print('Accuracy ', accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
plot_confusion_matrix(rf,x_test,y_test)

"""## **Train Boosting Classifier**

Boosting is an ensemble technique that attempts to create a strong classifier from a number of weak classifiers.
"""

from sklearn.ensemble import GradientBoostingClassifier
scores_1 =[]
for i in [70,100,150,200]:
  gb = GradientBoostingClassifier(n_estimators=i,random_state=0)
  gb.fit(x_train,y_train)
  y_pred = gb.predict(x_test)
  print('Accuracy ', accuracy_score(y_test,y_pred))
  print(classification_report(y_test,y_pred))
  plot_confusion_matrix(gb,x_test,y_test)
  scores_1.append(accuracy_score(y_test,y_pred))

#plot numbers of estimators Vs. accuracy scores
plt.plot([70,100,150,200],scores_1)
plt.title('n_estimator Vs accuracy')
plt.xlabel('n_estimator')
plt.ylabel('accuracy')

"""**So, the highest accuracy score is at n estimator = 100**

### **Train the boosting classifier at n estimator = 100 and with range [0.1:0.9]**
"""

scores_2 =[]
for i in [0.1,0.3,0.5,0.7]:
  gb = GradientBoostingClassifier(n_estimators=100,learning_rate=i,random_state=0)
  gb.fit(x_train,y_train)
  y_pred = gb.predict(x_test)
  print('Accuracy ', accuracy_score(y_test,y_pred))
  print(classification_report(y_test,y_pred))
  plot_confusion_matrix(gb,x_test,y_test)
  scores_2.append(accuracy_score(y_test,y_pred))

#Plot the learning rate Vs. accuracy scores
plt.plot([0.1,0.3,0.5,0.7],scores_2)
plt.title('learning rate Vs accuracy')
plt.xlabel('learning rate')
plt.ylabel('accuracy')

"""**So, the best accuracy is when number of estimator = 100 and with learning rate = 0.3**

#### **Train Boosting classifier with n_estimators=100,learning_rate=0.3**
"""

gb = GradientBoostingClassifier(n_estimators=100,learning_rate=0.3,random_state=0)
gb.fit(x_train,y_train)
y_pred = gb.predict(x_test)
print('Accuracy ', accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
plot_confusion_matrix(gb,x_test,y_test)

"""##**Apply XGBOOST classification model with n_estimators=100,learning_rate=0.3**

XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable.
"""

import xgboost as xg
xgb = xg.XGBClassifier(n_estimators=100,learning_rate=0.3,random_state=0)
xgb.fit(x_train,y_train)
y_pred = xgb.predict(x_test)
print('Accuracy ', accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
plot_confusion_matrix(xgb,x_test,y_test)

"""## **comparing between the models**

After comparing the models with each other, we noticed that the decision tree model is the lowest accuracy, which is 0.92, and the SVM model is the highest accuracy, which is 0.98

After applying soft voting and hard voting, the hard voting is the best, which have accuracy = 0.94, and the soft voting is the worst, which have accuracy = 0.92.

After comparing bagging and boosting, the best accuracy is boosting classifier, which have accuracy = 0.965

When comparing the XGBOOST model(with the best number of estimator and hyperparameter like the boosting classifier) with Gradient Boosting classifier, the accuracy of XGBOOST is the higher which ism =  0.9668
"""