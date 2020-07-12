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













