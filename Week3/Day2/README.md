### Day 2 – Linear Regression

In Day 2, we were introduced to the basics of Linear Regression, which is one of the most common supervised learning models used for making predictions of continuous numerical values. We were introduced to training a linear regression model with scikit learn and predicting and interpreting the meaning of the coefficients and intercept of the linear model. We also got to know about the evaluation of regression models through the measures like MAE, RMSE, and R².

## Learning Objectives
Today we learned about training a Linear Regression model and making predictions from it. We have learned about how to interpret the coefficients and the intercept of the model and what each feature contributes to the prediction made by the model. We have also learned how to assess the model based on MAE, RMSE, and R² score and compare it with a base model.
## Key Concepts
- Linear Regression: A supervised machine learning algorithm that is used to predict a numerical value using a linear function that fits into the data with minimum errors. It uses weights and biases to learn the data and make predictions.

- Training and Predictions: The Linear Regression algorithm is trained using the fit() function. Once the algorithm is trained, it is ready to make predictions for the testing dataset.the predict() method is used to generate predictions for the test data.
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
- Coefficients and Intercept: There is a coefficient for each predictor variable that shows the change in the predicted output when the predictor variable changes by one unit. The value of the intercept is an indication of the bias in the model.
print(model.coef_) # one coefficient for each feature print(model.intercept_) # intercept or bias
- Metrics for Regression: The performance of regression models can be determined by analyzing the gap between the actual and predicted values. The key metrics that we have learned were:

-- MAE (Mean Absolute Error): Calculates the average gap between the predicted and actual values. This is easier to interpret because it is measured in the units of the target variable.
-- RMSE (Root Mean Squared Error): Determines the prediction error with more weight on large errors.
-- R² (Coefficient of Determination): Determines the variance in the target variable that is accounted for by the model. The value of 1 denotes a perfect model.
- Comparison Baseline: A comparison baseline is a straightforward approach to forecasting that is taken as a point of reference to assess the efficacy of the machine learning algorithm. In case of regression analysis, one common practice is to predict the average value for each instance. The model should outperform the baseline.
## Tools Used
- Python
- Scikit-learn
- Pandas
- NumPy
- Jupyter Notebook
- matplotlib
## Hands-On Lab (Tasks)
- Step 1: Train a LinearRegression model on a provided regression dataset (e.g. house prices).
- Step 2: Report the model's coefficients and identify which feature has the strongest effect.
- Step 3: Evaluate the model with MAE, RMSE, and R² on the test set.
- Step 4: Compare the RMSE against a baseline that predicts the mean for every row, and state whether the
model adds value.
- Step 5: Document the interpretation of results in Markdown.
## Learning Outcomes
A primary learning outcome for the day was learning about Linear Regression and how it can be applied to make continuous numerical predictions. I got hands-on knowledge of training a regression model, making predictions, and understanding the interpretation of the coefficients and intercepts. Additionally, I learned about the evaluation of regression models through the use of MAE, RMSE, and R². In addition to this, I learned about the importance of testing a machine learning model against a simple benchmark to see if the model has learned useful patterns from the dataset.
