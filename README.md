# Craigslist_Analysis_Project

Craigslist Analysis
In this project, you’ll examine some data about housing rentals on Craigslist — an online classifieds site. The provided housing data contains the following variables:

price: monthly rental price in U.S.D.
type: type of housing (eg., 'apartment', 'house', 'condo', etc.)
sqfeet: housing area, in square feet
beds: number of beds
baths: number of baths
comes_furnished: 1 means yes, 0 means no
laundry_options: laundry availability with values 'laundry on site', 'no laundry on site', ‘w/d hookups‘, or 'w/d in unit'
parking_options: parking availability with values 'carport', 'detached garage', 'no parking', 'off-street parking', 'street parking', or 'valet'
smoking_allowed: 1 means yes, 0 means no
cats_allowed: 1 means yes, 0 means no
dogs_allowed: 1 means yes, 0 means no


# Fit Some Models
1.
Fit a model that predicts price using type, sqfeet, beds, and baths as predictors. Save the fitted model as model1.


2.
Fit a model that predicts price using type, sqfeet, beds, baths, comes_furnished, laundry_options, parking_options, and smoking_allowed as predictors. Save the fitted model as model2.

Note that model1 and model2 are nested models because model2 contains all of the predictors in model1.


3.
Fit a model that predicts price using type, sqfeet, beds, baths, comes_furnished, laundry_options, parking_options, smoking_allowed, cats_allowed, and dogs_allowed as predictors. Save the fitted model as model3.

Note that model3, model2, and model1 are nested models because model2 contains all of the predictors in model1 and model3 contains all of the predictors in model2.


# Find the Best Model to Fit the Data
4.
Print the R-squared for all three models. Approximately what proportion of variation in rental prices can be described using the largest predictor set (model3)?


5.
Print out the adjusted R-squared for all three models. Based on adjusted R-squared, which model fits the data best?

Note that the two extra predictors in model3 (compared to model2) are related to pet policies (cats_allowed and dogs_allowed). Based on your answer to the above: holding all other predictors constant, is there a significant relationship between a housing option’s pet policy and its price?


6.
Use the anova_lm() function from statsmodels (which has already been imported for you in script.py) to run an F-test comparing model2 and model3, then print the results.

Using a significance threshold of 0.05, are the coefficients on cats_allowed and dogs_allowed significantly different from zero? In other words: holding all other predictors constant, is there a significant relationship between a housing option’s pet policy and its price?

Does your answer based on the F-test match your answer based on adjusted R-squared? Note that these two criteria don’t have to agree!


# Find the Best Model for Out-of-Sample Prediction

7.
Print the log-likelihood for all three models. Which model has the largest log-likelihood? Does this make sense?


8.
Print the AIC for all three models. Based on AIC, which model fits the data best?

Would you choose the same model based on AIC as you would based on adjusted R-squared and the F-test?


9.
Print the BIC for all three models. Based on BIC, which model fits the data best?

Note that BIC tends to favor simpler models with fewer predictors. Would you choose the same model based on BIC as you would based on AIC, adjusted R-squared and the F-test?


10.
We’ve provided you with code in script.py to split the housing data into training and test sets. These are saved as housing_train and housing_test, respectively.

Re-fit model2 and model3 using the training dataset and re-save the fitted models as model2_train and model3_train.


11.
Calculate the fitted values for the test dataset based on model2_train and model3_train. Save them as fitted_mod2 and fitted_mod3, respectively.

12.
Calculate and print the predicted root mean squared error (PRMSE) for models 2 and 3.

Based on PRMSE, which model performs best with respect to out-of-sample prediction?

# Bonus Explorations and Next Steps!

13.
In this project, we saw that model2 and model3 performed very similarly. model3 edged out model2 in most comparisons, but only by a small amount.

Note that the process of calculating PRMSE involves randomly splitting the data into training and test datasets. Depending on how we split the data, we’ll calculate slightly different PRMSE values. If two models have very similar PRMSEs, then different models may “win” depending on how we split the data.

Toward the beginning of script.py we’ve set a random seed using np.random.seed(1) to control the way the data is split. Try changing the random seed to a different number besides 1, then re-run the code. Does model 3 still have a smaller PRMSE?

Try a few more times with different numbers. Can you get a sense for whether model 3 wins out more often — or is it a toss-up?
