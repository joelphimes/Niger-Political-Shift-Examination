import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

class Hypothesis():
    
    def __init__(self) -> None:
        pass
    
    def perform_anova(df):
        """
        Renames 'Indicator Value' column to 'Indicator_Value' (if present),
        performs ANOVA using OLS on 'Indicator_Value' by the 'Regime' and
        prints the ANOVA table.
    
        Args:
        - df (pd.DataFrame): DataFrame with at least 'Indicator Value' and 'Regime' columns.
    
        Returns:
        - None (prints ANOVA table).
        """
    
        # Rename the 'Indicator Value' column
        df.rename(columns={'Indicator Value': 'Indicator_Value'}, inplace=True)

        # Fit the OLS model
        model = ols('Indicator_Value ~ C(Regime)', data=df).fit()

        # Obtain the ANOVA table
        anova_table = sm.stats.anova_lm(model)

        # Print the ANOVA table
        print(anova_table)

    def perform_tukey_hsd(df):
        """
        Performs the Tukey HSD test on 'Indicator_Value' by the 'Regime' column and
        prints the pairwise comparison results.
    
        Args:
        - df (pd.DataFrame): DataFrame with at least 'Indicator_Value' and 'Regime' columns.
    
        Returns:
        - None (prints pairwise comparison results).
        """
    
        # Perform multiple pairwise comparison (Tukey HSD)
        m_comp = pairwise_tukeyhsd(endog=df['Indicator_Value'], groups=df['Regime'], alpha=0.05)
    
        # Print the pairwise comparison results
        print(m_comp)
        
# Conditional check used to determine if the class/function is being run as a standalone program 
# or if it has been imported as a module into another script. 
# If it's standalone, the code inside the if block will execute. Otherwise, it won't.
# In this case, nothing happens (indicated by 'pass') when the script is run as standalone.
if __name__ == "__main__":
    pass