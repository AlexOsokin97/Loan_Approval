# Project Overview:
***Are you intrested in taking a loan but don't want to wait the whole process just to get rejected?***

**As it is well known, the gap between real estate prices and the average salary is extreme, which makes the chances for an individual to purchase property almost impossible. Married couple and people with salaries above average even struggle when it comes to real estate. Those situations are where loans come in handy. You go to the bank and borrow N amount of money which you then return in a fixed payment for K certain number of months. The amount of money you are allowed to borrow depends on your monthly income, your partner's income (if you decide to take it with someone), the amount of money you need, type of real estate property you are interested in, credit history and number of dependencies of the borrower.**

## Data Cleaning & Outlier Removal:

* **Used statistical methods such as Mean Median and Mode to replace missing values** 
* **for Loan_Amount_Term I created a dictionary which contained all the avaliable term and for each term I calculated the mean loan amount borrowed. I then replaced the missing values of the Loan_Amount_Term with respect to the dictionary in order to make the replacements as accurate as possible**
* **Transformed column data type to the correct type**<br/>

**I used the interquartile range (IQR) statistical formula which describes the middle 50% of values when ordered from lowest to highest to set the lowest and highest bounds for outlier removal in relevant numerical columns:**

***Applicant Income:***

IQR = 2,918$<br/>
Upper Bound = 10,172$<br/>
Lower Bound = -63.5 (Because an income cannot be negative I set the lower bound to the minimum value in that column)

***Co-Applicant Income:***

IQR = 2,297$<br/>
Upper Bound = 5,742$<br/>
Lower Bound = -3445.5 (Because an income cannot be negative I set the lower bound to the minimum value in that column)

***Loan Amount:***

IQR = 64,500$<br/>
Upper Bond = 261,500$<br/>
Lower Bond = 3,500$

## Exploritory Data Analysis:
***created various simple plots and graphs to get information about the type of borrowers and how each of their features affects their loan verdict***

* *According to the data you have 33% chance to get your loan rejected and 67% chance to get your loan approved*

* *If you are a graduate you have 69% chance getting your loan approved*

* *Most of the term time taken by borrowers is between 300 - 400 months with the average of 337 months*

* *64% of the borrowers are married*

* *86% of the borrowers are not self employed which means they live of a paycheck*

* *Graduated Women have a higher probability of borrowing a loan between 100-150 thousand dollars than Men. This might be because male graduates tend to get a higher paying job than female graduates. On the other hand, males that did not graduate yet/have no education have higher probability to take a loan. The reason for this is not clear enough but it might be because jobs that do not require education pay higher wages to females*

* *The Urban property type has the biggest probability spread when it comes to loan amount requested by the borrower. This might mean that urban property is most prefered real estate for most people or urban property have a high price variation*

* *A loan for urban property has 65% chance of approval with 35% chance of rejection. 32% of all loan applications were for urban property.*

* *A loan for rural property has 64% chance of approval with 36% chance of rejection. 30% of all loan applications were for rural property.*

* *A loan for semi-urban property has 76.5% chance of approval with 23.5% chance of rejection. 38% of all loan applications were for semi-urban property*

## Machine Learning:
***I did the following steps before beginning to implement machine learning techniques in order to make the process easier and maybe to gain more insights***

* *I created 2 figure canvases. Each canvas can contain 4 plots. The first canvas I plotted 4 distribution plots for: Applicant Income, Co applicant income, Loan Amount and Loan Amount Term columns with values corresponding with Loan Status of type "Y" (Approved Loan). The same thing I did with Loan Status of type "N". The reason I did those plots was in order to see how the distribution of the data changes for each Loan Status type which helped me to gain more information.*

* *I created 2 Heatmaps using the same technique of class splitting in order to see if maybe there are different column correlation for each Loan Status. Both of the Heatmaps were the same*

***After studying and gaining information from those plots It was time to train and test my machine learning algorithms***

***I used the following scikit-learn packages for feature engineering, data scaling and data manipulation:***
* **cross_val_score function:** I used this method because I wanted to check if my model's performance on the training data was not accidental. I checked it by splitting my training data to 7 folds of datasets where 1 of 7 folds was used as validation data and fitting the model to each split variation. In the end I took the mean accuracy score of all the accuracies. This method lowered the probability that the model's performance was accidental and also gave me a general idea of the quality of my dataset.

* **GridSearchCV:** I used this method for model's hyper parameter tuning. With this method I was able to get better classification results.

* **train_test_split:** I used this technique in order to split my dataset into 2 fractions. The first largest fraction is the 'training set' which would include 80% of the whole dataset and the second smallest fraction is the 'testing set' which would include 20% from the whole dataset. I used this technique because I wanted to check how successful my models were by applying them on data they had never seen before.

* **PCA (principal component analysis):** The PCA is a dimension reduction technique which transforms an M number of features into N number of components. This method makes the data less complex and as a result an algorithm may train faster and use less computation power. I chose 2 components because I did not have too much numerical features in my dataset and because it is the standard choice.

* **OneHotEncoder, LabelEncoder & ColumnTransformer:** These packages transform categorical columns into numerical values. each value is then put in a binary column with 1 and 0 values that indicate whether a specific category is present in the observation or not.

* **Normilizer:** A scaling function for normal distributed data which scales values between 0 and 1. I used this method because I used IQR in order to remove outliers.

***After the data was feature engineered, split and ready to use, I used the following machine learning algorithms:***

* **Random Forests Classifier:** A Decision Tree based algorithm which uses different non correlated random decision trees. Each tree uses different randomly selected features to make a prediction. For each observation in the data a selected amount of trees are grown and the most frequent prediction gets chosen. I chose this algorithm because I had a good amount of features, a case that is a good fit for this algorithm. In addition, It is very fast and most of the times has good performance. *It is also my personal favorite*. [https://www.youtube.com/watch?v=J4Wdy0Wc_xQ]

* **XGBoost Classifier:** XGBoost is a decision-tree-based ensemble Machine Learning algorithm that uses a gradient boosting framework. I chose this algorithm because it is fast, uses less computation resources and has many hyper-parameters that you can change which may lead to good results. [https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d]

* **Support Vector Machine with RBF kernel:** The algorithm uses the help of hyperplanes to classify groups of data. I chose this algorithm because I removed outliers and scaled the data both of which have a negative effect on the outcome of the algorithm. In addition, it is very comfortable with high data dimensionality.

* **Logistic Regression:** A linear regression based algorithm which uses a sigmoid function to make a prediction. y with a value bigger than 0.5 will be classified as 1 and value less than 0.5 will be classified as 0. I chose this algorithm because it is very simple, it is easy to implement and it is a great choice for a binary classification problem. [https://www.youtube.com/watch?v=yIYKR4sgzI8]

***Lastly, I trained the algorithms on the training set and evaluated their performance on the testing set:***

#### Random Forest Classifier
* Accuracy: 84%
* Precision: 80%

#### XGBoost Classifier
* Accuracy: 83%
* Precision: 82%

#### SVM rbf
* Accuracy: 84%
* Precision: 81%

#### Logistic Regression
* Accuracy: 84%
* Precision: 81%

## Conclusion
***All 4 algorithms had an outstanding performance. Each one of them scored above 80% accuracy and 80% precision. Firstly, the reason the algorithms weren't able to achieve a higher accuracy and precision might be because: 1. There was not enough data to train the algorithm on. 2. Not enough features which could have helped the algorithm to make a better predicition.<br/> 
Secondly, I also chose the precision scoring metic because as a loan giver it is important for me that the model would have a high rate of correct predictions from all the predictions that it had made.<br/>
As a result, if I were to choose 1 algorithm to put on production I would choose XGBoost classifier.***










