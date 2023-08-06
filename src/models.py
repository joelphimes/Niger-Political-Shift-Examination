import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from statsmodels.stats.outliers_influence import variance_inflation_factor

class Model():
    
    def __init__(self) -> None:
        pass
    
    def perform_regression(merged_data):
        """
        Performs a linear regression on the merged_data dataframe using Amount_DAC as the independent variable
        and Amount_GCF as the dependent variable. 

        Args:
        - merged_data (pd.DataFrame): DataFrame with at least 'Amount_DAC' and 'Amount_GCF' columns.

        Returns:
        - Regression results summary.
        """
    
        # Defining X and y variables
        X = sm.add_constant(merged_data['Amount_DAC'])
        y = merged_data['Amount_GCF']

        # Fitting the model
        model = sm.OLS(y, X)
        results = model.fit()

        # Return summary statistics of the regression model
        return results.summary()
    
    def calculate_vif(X):
        """
        Calculates the Variance Inflation Factor (VIF) for each column in the given DataFrame.
    
        Args:
        - X (pd.DataFrame): DataFrame for which VIF should be calculated.
    
        Returns:
        - v (pd.DataFrame): DataFrame containing variables and their respective VIF values.
        """
    
        X = sm.add_constant(X)
    
        v = pd.DataFrame()
        v['Variables'] = X.columns
        v['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    
        return v
    
    def train_test_evaluate(merged_data):
        """
        Splits the data into training and test sets, fits a linear regression model using the training set,
        predicts on the test set, and prints the Mean Squared Error and Root MSE.
    
        Args:
        - merged_data (pd.DataFrame): DataFrame with at least 'Amount_DAC' and 'Amount_GCF' columns.
    
        Returns:
        - None (prints MSE and Root MSE).
        """
    
        # Splitting data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(merged_data[['Amount_DAC']], merged_data['Amount_GCF'], test_size=0.2, random_state=42)

        # Fitting the regression model
        lm_train = sm.OLS(y_train, sm.add_constant(X_train)).fit()
    
        # Predicting on the test set
        y_pred = lm_train.predict(sm.add_constant(X_test))
    
        # Calculating and printing the MSE and Root MSE
        mse = mean_squared_error(y_test, y_pred)
        print('Mean Squared Error:', mse)
        print('Root MSE', np.sqrt(mse))

# Conditional check used to determine if the class/function is being run as a standalone program 
# or if it has been imported as a module into another script. 
# If it's standalone, the code inside the if block will execute. Otherwise, it won't.
# In this case, nothing happens (indicated by 'pass') when the script is run as standalone.
if __name__ == "__main__":
    pass