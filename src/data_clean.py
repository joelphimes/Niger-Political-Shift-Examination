import numpy as np
import pandas as pd

# Reads in file, describes, and cleans df.
class Clean:
    """Example Usage:
        cleaner = clean.Clean()
        cleaner.read_file(file_path)
        ^something like that for most of'em
    """
    def __init__(self):
        pass
    
    # Read csv into data frame fucntion
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

    # Different format for describe function
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

    # Find missing data and give some common analytics on those values 
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

    # Get column and show feat(data type)
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

    # Drops row with missing data, used in this case when data tht is na = scattered 
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

if __name__ == "__main__":
    pass