import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Performs Hypothesis specfied tests (ANOVA, TUKEY HSD).
class Hypothesis:
    """Example Usage:
        h_tester = hypo_test.Hypothesis()
        h_tester.perfrom_anova(df)
        ^something like that for most of'em
    """
    def __init__(self) -> None:
        pass
    
    # Perfroms ANOVA on specfied data.
    def perform_anova(self, df):
        """
        Renames 'Indicator Value' column to 'Indicator_Value' (if present),
        performs ANOVA using OLS on 'Indicator_Value' by the 'Regime' and
        prints the ANOVA table.
    
        Args:
        - df (pd.DataFrame): DataFrame with at least 'Indicator Value' and 'Regime' columns.
    
        Returns:
        - None (prints ANOVA table).
        """
        # Took me like 2 hours, ANOVA OLS is not a fan on the spaces.. yikes.
        # Rename the 'Indicator Value' column
        df.rename(columns={'Indicator Value': 'Indicator_Value'}, inplace=True)

        # Fit the OLS model
        # Use OLS on Indicator Value (in this case GOV Effect).
        model = ols('Indicator_Value ~ C(Regime)', data=df).fit()

        # Obtain the ANOVA table
        # https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.anova_lm.html
        anova_table = sm.stats.anova_lm(model)

        # Print the ANOVA table
        # Tried using pretty print on this and tabulate, no go. 
        # I'll just throw it in excel. 
        print(anova_table)

    # Performs HSD on specfied data to back up ANOVA.
    def perform_tukey_hsd(self, df):
        """
        Performs the Tukey HSD test on 'Indicator_Value' by the 'Regime' column and
        prints the pairwise comparison results.
    
        Args:
        - df (pd.DataFrame): DataFrame with at least 'Indicator_Value' and 'Regime' columns.
    
        Returns:
        - None (prints pairwise comparison results).
        """


        # Perform multiple pairwise comparison (Tukey HSD)
        # https://towardsdatascience.com/anova-tukey-test-in-python-b3082b6e6bda
        m_comp = pairwise_tukeyhsd(endog=df['Indicator_Value'], groups=df['Regime'], alpha=0.05)
    
        # Print the pairwise comparison results
        # This already prints really lovely so no need to change it.  
        print(m_comp)
        
# Conditional check used to determine if the class/function is being run as a standalone program 
# or if it has been imported as a module into another script. 
# If it's standalone, the code inside the if block will execute. Otherwise, it won't.
# In this case, nothing happens (indicated by 'pass') when the script is run as standalone.
if __name__ == "__main__":
    pass