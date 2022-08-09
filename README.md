Decision Tree assignment

Implementation steps:

    1- Import Important Libraries and load the dataset.
    
    2- Load the training dataset.
    
    3- Get some information about the training dataset.
    
    4- Count the numbers occurrence in the label column.
    
    5- Split data into x_train and y_train.
    
    6- Load the test dataset.
    
    7- Count the numbers occurrence in label column.
    
    8- Split the test data into x_test and y_test.
    
    9- Train the Decision Tree classification Model.
    
    10- Train SVM model.
    
    11- Apply Hard and soft Voting Classifiers.
    
    12- Apply Bagging Classifier in range[10:200].
    
    13- Train bagging classifier with the best number of estimators.
    
    14- Apply Random Forest classifier: (additional model code).
    
    15- Train Boosting Classifier in range[10:200].
    
    16- Train the boosting classifier at n estimator = 100 and with range [0.1:0.9].
    
    17- Train Boosting classifier with n_estimators=100, learning_rate=0.3.
    
    18- Apply XGBOOST classification model with n_estimators=100, learning_rate=0.3
    
    
Which metric is the best to compare performance, accuracy or the confusion 
matrix?
    - Accuracy performance metrics can be critical when dealing with imbalanced data and 
      overfitting.
    
    - The confusion matrix, recall, precision, and F1 score gives good obviousness of prediction
       results comparing with the accuracy.
    
    - The F1-score can tell us if there is overfitting or not.
    
    - After seeing the F1-score, we notice that there is no overfitting in the data, so the accuracy is 
      good here than the confusion matrix.
      
   
 Conclusion:
      - During this assignment we learned how to apply different classification techniques, such as 
         decision tree classifier, and apply bagging and boosting with the best estimator and learning 
         rate.
      
      - After comparing the models with each other, we noticed that the decision tree model is the 
        lowest accuracy, which is 0.92, and the SVM model is the highest accuracy, which is 0.98
      
      - After applying soft voting and hard voting, the hard voting is the best, which have accuracy =
        0.94, and the soft voting is the worst, which have accuracy = 0.92.
      
      - After comparing bagging and boosting, the best accuracy is boosting classifier, which have 
         accuracy = 0.965,
      
      - When comparing the XGBOOST model(with the best number of estimator and 
        hyperparameter like the boosting classifier) with Gradient Boosting classifier, the accuracy of 
        XGBOOST is the higher which ism = 0.9668
