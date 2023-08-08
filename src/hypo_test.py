import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

class Hypothesis:
    
    def __init__(self) -> None:
        pass
    
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
        # Use OLS on Indicator Value (in this case GOV Effect).
        # Fit the Model. 
        # Use stats.annova_lm. 
        # https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.anova_lm.html
        # Print the ANOVA table. 
        # Tried using pretty print on this and tabulate, no go. 
        # I'll just throw it in excel. 
        # Rename the 'Indicator Value' column
        df.rename(columns={'Indicator Value': 'Indicator_Value'}, inplace=True)

        # Fit the OLS model
        model = ols('Indicator_Value ~ C(Regime)', data=df).fit()

        # Obtain the ANOVA table
        anova_table = sm.stats.anova_lm(model)

        # Print the ANOVA table
        print(anova_table)

    def perform_tukey_hsd(self, df):
        """
        Performs the Tukey HSD test on 'Indicator_Value' by the 'Regime' column and
        prints the pairwise comparison results.
    
        Args:
        - df (pd.DataFrame): DataFrame with at least 'Indicator_Value' and 'Regime' columns.
    
        Returns:
        - None (prints pairwise comparison results).
        """
        # So from some light research the next logical step would be to see about the Tukey HSD.
        # Null Hypothesis (H0): The means of the two groups being compared are equal.
        # Alternative Hypothesis (H1): The means of the two groups being compared are not equal. 
        # (import part right here) ANOVA does not tell us which groups are different. 
        # The Tukey HSD test helps us identify which specific group means are different from each other.

        # Good summary -->
        # The Tukey HSD ("honestly significant difference" or "honest significant difference") test is a statistical tool used to determine 
        # if the relationship between two sets of data is statistically significant – that is, whether there's a strong chance that an observed 
        # numerical change in one value is causally related to an observed change in another value. 
        # In other words, the Tukey test is a way to test an experimental hypothesis.

        # Perform multiple pairwise comparison (Tukey HSD)
        # This already prints really lovely so no need to change it.  
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