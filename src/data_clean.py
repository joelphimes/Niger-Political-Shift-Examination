import numpy as np
import pandas as pd

# Reads in file, describes, shows missing data, 
# shows column feats, formats data. 
class Clean:
    """Example Usage:
        cleaner = clean.Clean()
        cleaner.read_file(file_path)
        ^something like that for most of'em
    """
    
    def __init__(self):
        pass
    
    # Read csv into data frame fucntion.
    def read_file(self, file_path):
        """
        Read a file and return a DataFrame based on the file extension.

        Args:
            file_path (str): Path to the file.

        Returns:
            pandas.DataFrame: DataFrame containing the file data.
        """
        
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        else:
            print("Error: Invalid file extension.")
            return None

    # Different format for describe function.
    def describe_dataframe(self, df):
        """
        Generate descriptive statistics for each numerical column in a Pandas DataFrame.

        Args:
            data (pandas.DataFrame): DataFrame for which to generate descriptive statistics.

        Returns:
            pandas.DataFrame: DataFrame containing descriptive statistics.
        """
        
        # Used the options display from the last project, really handy..
        # https://pandas.pydata.org/docs/user_guide/options.html 
        pd.options.display.float_format = '{:,.0f}'.format
        output = df.describe()
        return output

    # Find missing data and give some common analytics on those values. 
    def find_missing_data(self, df):
        """
        Find missing data in a Pandas DataFrame.

        Args:
            data (pandas.DataFrame): DataFrame to check for missing data.

        Returns:
            pandas.DataFrame: DataFrame summarizing missing data.
        """
        
        missing_data = df.isnull().sum()
        return missing_data

    # Get column and show feat(data type).
    def get_column_features(self, df):
        """provides column dict listing and data type for pandas dataframe

        Args:
            df (DataFrame): DataFrame for which to retrieve the features and data types.

            
        Returns:
            dict: Dictionary containing column names as keys and their data types as values.
        """
        
        # Want to make a dict for all the columns and their data types.
        feats = {}
        for c in df.columns:
            feats[c] = df[c].dtype 
        return feats

    # Drops row with missing data, used in this case when data tht is scattered.
    def drop_rows_with_missing_data(self, df):
        """
        Drop rows with missing data from the given dataframe.
        
        Args:
            df (pandas.DataFrame): The dataframe containing missing data.
        
        Returns:
            pandas.DataFrame: A new dataframe without the rows containing missing data.
        """
        
        df_without_missing = df.dropna()
        return df_without_missing
    
    # Goal is to format the pvalues, espically the ones that are tiny.
    def formatted_pvalues(self, results):
        """
        Prints the formatted p-values from the regression results.
    
        Args:
        - results (Results object): The results object from the regression fit.
    
        Returns:
        - None (prints the p-values).
        """
    
        # Convert the p-value to a pandas Series for easy manipulation.
        pvalues = pd.Series(results.pvalues)

        # Format the p-values using the map method.
        # that :.xf is going to determine on the size, could tweak each time.
        formatted_pvalues = pvalues.map('{:.11f}'.format)

        # Print the formatted p-values.
        print(formatted_pvalues)

# Conditional check used to determine if the class/function is being run as a standalone program 
# or if it has been imported as a module into another script. 
# If it's standalone, the code inside the if block will execute. Otherwise, it won't.
# In this case, nothing happens (indicated by 'pass') when the script is run as standalone.
if __name__ == "__main__":
    pass