# Load libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Set seed
np.random.seed(1)

# Import data
housing = pd.read_csv('craigslist.csv')

# Fit model1
model1 =sm.OLS.from_formula('price ~ type +beds +baths + sqfeet', data=housing).fit()

# Fit model2
model2 =sm.OLS.from_formula('price ~ type + beds + baths + sqfeet + comes_furnished + laundry_options + parking_options + smoking_allowed ', data=housing).fit()

# Fit model3
model3 =sm.OLS.from_formula('price ~ type + beds + baths + sqfeet + comes_furnished + laundry_options + parking_options + smoking_allowed + smoking_allowed + cats_allowed + dogs_allowed', data=housing).fit()

# Print R-squared for all models
print(model1.rsquared)
print(model2.rsquared)
print(model3.rsquared)

# Print adjusted R-squared for all models
print(model1.rsquared_adj)
print(model2.rsquared_adj)
print(model3.rsquared_adj)

# Run an F test comparing model2 and model3 = both coefficients on cats_allowed and dogs_allowed are equal to zero
from statsmodels.stats.anova import anova_lm

anova_results =anova_lm(model2, model3)
print(anova_results)

# Print log likelihood for all models = -37528.12294065279 / -22989.87439522474 /-22985.76634388421 = Largest largest log-likelihood

print(model1.llf)
print(model2.llf)
print(model3.llf)

# Print AIC for all models = 75082.24588130559 /46029.74879044948 /46025.53268776842. = Lowest AIC
print(model1.aic)
print(model2.aic)
print(model3.aic)

# Print BIC for all models = 75166.969392794 /46180.63885777244 = LOWEST BIC / 46188.49396047722
print(model1.bic)
print(model2.bic)
print(model3.bic)

# Split housing data
indices = range(len(housing))
s = int(0.8*len(indices))
train_ind = np.random.choice(indices, size = s, replace = False)
test_ind = list(set(indices) - set(train_ind))
housing_train = housing.iloc[train_ind]
housing_test = housing.iloc[test_ind]

# Fit model2 with training data
model2_train =sm.OLS.from_formula('price ~ type + beds + baths + sqfeet + comes_furnished + laundry_options + parking_options + smoking_allowed ', data=housing_train).fit()

# Fit model3 with training data
model3_train =sm.OLS.from_formula('price ~ type + beds + baths + sqfeet + comes_furnished + laundry_options + parking_options + smoking_allowed + smoking_allowed + cats_allowed + dogs_allowed', data=housing_train).fit()

# Calculate predicted price based on model2
fitted_mod2 =model2.predict(housing_test)
# Calculate predicted price based on model3
fitted_mod3 =model3.predict(housing_test)
# Calculate PRMSE for model2 = 404.19409737303937
true =housing_test.price

prmse2 =np.mean((true-fitted_mod2)**2)**.5
print(prmse2)

# Calculate PRMSE for model3 = 403.4430443007299 -> Choose Model 3
prmse3 =np.mean((true-fitted_mod3)**2)**.5
print(prmse3)

