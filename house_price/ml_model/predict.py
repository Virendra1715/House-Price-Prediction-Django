import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df=pd.read_csv('kc_house_data.csv')
print(df.head())
print("missing values:",df.isnull().sum())
print("duplicate:",df.duplicated().sum())

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

print(df.drop('date',axis=1,inplace=True))
print(df.head())


print(df.drop(['id','waterfront','view','zipcode','lat','long'],axis=1,inplace=True))
print(df.head())
"""
plt.figure(figsize=(12,6))

sns.scatterplot(
    x='sqft_lot',
    y='price',
    data=df
)
plt.show()
sns.histplot(df[['price']],kde=True,bins=50)
plt.show()
sns.boxplot(x=df['price'])
plt.show()

plt.title("House Price vs Total Square Feet")
plt.xlabel("Total Square Feet")
plt.ylabel("Price (Lakhs)")
plt.show()
sns.pairplot(df[['price','bedrooms']])
plt.show()
"""
print(df.describe())
print(df.info())
print(df.dtypes)

from sklearn.model_selection import train_test_split
X=df.drop('price',axis=1)
y=df['price']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
from sklearn.linear_model import LinearRegression
lm=LinearRegression()

lm.fit(X_train,y_train)
prediction_lm=lm.predict(X_test)

from sklearn.tree import DecisionTreeRegressor
dtree=DecisionTreeRegressor()

dtree.fit(X_train,y_train)
prediction_dtree=dtree.predict(X_test)

from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor()
rfr.fit(X_train,y_train)
prediction_rfr=rfr.predict(X_test)


from sklearn.metrics import mean_absolute_error, mean_squared_error,root_mean_squared_error,r2_score

print("MAE:",mean_absolute_error(y_test,prediction_rfr))
print("MSE:",mean_squared_error(y_test,prediction_rfr))
print("RMSE:",np.sqrt(mean_squared_error(y_test,prediction_rfr)))
print("R2 Score:",r2_score(y_test,prediction_rfr))


from sklearn.model_selection import GridSearchCV
param_grid={
    'n_estimators': [100, 200, 300],
        'max_depth': [10, 20, None],
        'min_samples_split': [2],
        'min_samples_leaf': [1],
        'max_features': ['sqrt'],
        'bootstrap': [True, False]
}

grid=GridSearchCV(rfr,param_grid,cv=2,n_jobs=4)
grid.fit(X_train,y_train)
prediction_grid=grid.predict(X_test)
print("MAE :", mean_absolute_error(y_test, prediction_grid))
print("MSE :", mean_squared_error(y_test, prediction_grid))
print("RMSE:", np.sqrt(mean_squared_error(y_test, prediction_grid)))
print("R2 Score:",r2_score(y_test,prediction_grid))

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)
print("Best Model:", grid.best_estimator_)


import joblib

joblib.dump(grid.best_estimator_, "house_price_model.pkl")
joblib.dump(X.columns.tolist(), "model_columns.pkl")