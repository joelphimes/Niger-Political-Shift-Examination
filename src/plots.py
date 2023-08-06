import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mticker

# Plot class for line, bar, heatmap, stacked, and folium.heat
class Plot:
    """Example Usage:
        plotter = functions.Plot()
        plotter.line_chart(x_values, y_values, 'X', 'Y', 'Line Chart')
        ^something like that for most of'em
    """
    def __init__(self):
        pass
    
    def line_chart(self, series, x_label, y_label, title):
        """
        Plot a line chart.

        Args:
        series(pandas.series): Pandas series.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plt.show()
        """
        # Need to import style first (as shown above).
        style.use('fivethirtyeight')

        # Figsize.
        # Using series.plot show in Week 4 of learn material. 
        plt.figure(figsize=(10, 6))
        series.plot(kind='line', marker='o', color='orange')
        
        # Label and title.
        # Needed to make them black on the white margin.
        plt.xlabel(x_label, color='black')
        plt.ylabel(y_label, color='black')
        plt.title(title, color='black')

        # Set the background color to black.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html helped a ton.. 
        plt.gca().set_facecolor('black')

        # Using all the years present for the xticks.
        # Set the tick color to black.
        # Needed to make them black on the white margin.
        plt.xticks(series.index)
        plt.tick_params(axis='x', colors='black')
        plt.tick_params(axis='y', colors='black')
        
        # plt.show.
        plt.show()  

    def heatmap(self, data, x_label, y_label, title):
        """
        Plot a heatmap.

        Args:
        data (DataFrame, poss corr matrix): Data to be plotted as a heatmap.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plt.show()
        """
        # Self explaintory - easy one
        # Getting the data formated the right way is the hard one for the right corr matrix
        plt.figure(figsize=(10, 6))
        sns.heatmap(data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()
        
    def heatmap(self, data, x_label, y_label, title):
        """
        Plot a boxplot.

        Args:
        data (DataFrame or Series): Data to be plotted as boxplot.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plt.show()
        """
        # Self explaintory - easy one
        plt.figure(figsize=(10, 6))
        sns.boxplot(data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()
    
    def stacked(self, series, x_label, y_label, title):
        """
        Plot a stacked bar chart.

        Args:
        series: Data to be plotted.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plot
        """
        
        # Figsize.
        # Using series.plot show in Week 4 of learn material.  
        plt.figure(figsize=(16, 12))
        series.plot(kind='bar', stacked=True)

        # Add lables and title.
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        # Roatate xticks.
        plt.xticks(rotation= 45)

        # Set the background color to black.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html helped a ton.. 
        plt.gca().set_facecolor('black')

        # Wanted to get the legend in the bottom left corner.. 
        # https://stackoverflow.com/questions/25068384/bbox-to-anchor-and-loc-in-matplotlib
        plt.legend(title='Method', bbox_to_anchor=(1.05, 0), loc='lower left')

        # plt.show.
        plt.show()
        
    def plot_residuals(merged_data):
        """
        Plots residuals against predicted values for a regression model on 'Amount_DAC' and 'Amount_GCF'.
    
        Args:
        - merged_data (pd.DataFrame): DataFrame with at least 'Amount_DAC' and 'Amount_GCF' columns.
    
        Returns:
        - None (shows the plot).
        """
    
        # Fit the regression model
        X = sm.add_constant(merged_data['Amount_DAC'])
        Y = merged_data['Amount_GCF']
        lm = sm.OLS(Y, X).fit()

        # Calculate predicted values and residuals
        merged_data['predicted_GCF'] = lm.predict(X)
        merged_data['residuals'] = merged_data['Amount_GCF'] - merged_data['predicted_GCF']

        # Plotting residuals against predicted values
        sns.scatterplot(x='predicted_GCF', y='residuals', data=merged_data)
        plt.xlabel('Predicted GCF')
        plt.ylabel('Residuals')
        plt.axhline(y=0, color='r', linestyle='--')
        plt.show()


    def bar_aid_to_niger(PG4, figsize=(16, 9), custom_colors=None):
        """
        Plot the total aid given to Niger by various countries over a specified period.

        Parameters:
        - PG4 (pd.DataFrame): A DataFrame where each row represents a country and columns represent years of aid 
                          (with the first column being country names labeled "Indicator Name").
        - figsize (tuple, optional): Size of the plot. Default is (16, 9).
        - custom_colors (list, optional): A list of colors to use for each country's bar in the plot. 
                                      Default colors are specified within the function.

        Returns:
        - None: The function displays a bar chart using matplotlib.

        Example:
        PG4 = <your dataframe>
        plot_aid_to_niger(PG4)
        """

        # Calculate total aid for Niger
        PG4["Total_Aid_Niger"] = PG4.iloc[:, 1:-1].sum(axis=1)

        # Format the numbers
        number = [PG4.iloc[i, -1] for i in range(8)]
        new = ["${:,.2f}".format(n) for n in number]

        # Setup the plot
        fig, ax = plt.subplots(figsize=figsize)

        # Set default colors if not provided
        if not custom_colors:
            custom_colors = ['blue', 'yellow', 'white', 'blue', 'black', 'maroon', 'navy', 'red']

        # Bar chart
        ax.bar(PG4["Indicator Name"], PG4["Total_Aid_Niger"], color=custom_colors, alpha=0.6)

        # Setting labels and title
        ax.set_xlabel("Country", color='green')
        ax.set_ylabel("Total DAC Flows to Niger (USD Billions)", color='green')
        ax.set_title("Total DAC Flows by Country to Niger (1996-2021)", color='green')

        # Background color and formatting
        plt.gca().set_facecolor('grey')
        formatter = mticker.FuncFormatter(lambda x, _: f"${x / 1e9:.0f}B")
        ax.yaxis.set_major_formatter(formatter)

        # Set the y-axis limits and ticks
        max_total_aid = PG4["Total_Aid_Niger"].max()
        y_ticks = [tick * 1e9 for tick in range(int(max_total_aid / 1e9) + 1)]
        ax.set_yticks(y_ticks)
        ax.set_ylim(0e7, 4e9)
        ax.set_xlim(-0.5, len(PG4) - 0.5)
        plt.xticks(rotation=45)

        # Display the plot
        plt.show()

    def violin_gov_effectiveness(data, b_mean, m_mean, i_mean):
        """
        Plot the Government Effectiveness Scores for various leaders using a violin plot.

        Parameters:
        - data (pd.DataFrame): DataFrame containing the 'Leader' and 'Government Effectiveness Score' columns.
        - b_mean (float): Mean score for Mainassara.
        - m_mean (float): Mean score for Tandja.
        - i_mean (float): Mean score for Issoufou.

        Returns:
        - None: The function displays a violin plot with information boxes using matplotlib and seaborn.
        """
    
        # Define colors for the plot
        new_colors = ['white', 'green', 'orange']

        # Set figure size
        plt.figure(figsize=(10, 6))

        # Create violin plot
        sns.violinplot(y='Leader', x='Government Effectiveness Score', data=data, palette=new_colors)

        # Set background color
        plt.gca().set_facecolor('grey')

        # Add text box with general considerations
        text_1 = '''
        Considerations

        Regime: 
        1996 - 1999: Ibrahim Bare Mainassara
        1999 - 2010: Mamadou Tandja
        2011- 2021:  Mahamadou Issoufou

        GE Scale:
        -2.5 <-> +2.5
        '''
        plt.text(0.02, 0.97, text_1, transform=plt.gca().transAxes, fontsize=8,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        # Add text boxes for each leader's mean score
        text_2 = f"Mainassara's Mean: {b_mean:.2f}"
        plt.text(0.61, 0.85, text_2, transform=plt.gca().transAxes, fontsize=8,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
        text_3 = f"Tandja's Mean: {m_mean:.2f}"
        plt.text(0.82, 0.51, text_3, transform=plt.gca().transAxes, fontsize=8,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        text_4 = f"Issoufou's Mean: {i_mean:.2f}"
        plt.text(0.8, 0.18, text_4, transform=plt.gca().transAxes, fontsize=8,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        # Add labels and title
        plt.ylabel('')
        plt.xlabel("Government Effectiveness Indicator", color='green')
        plt.title("Distribution of Government Effectiveness During Regime", color='green')
        plt.xlim(-2.5, 0)

        # Display the plot
        plt.show()
        
    def plot_niger_economic_indicators(df):
        """
        Plots the economic indicators for Niger as an area chart.

        Args:
        df (DataFrame): The DataFrame containing the economic indicators.

        Returns:
        None.
        """

        df.set_index('Indicator Name', inplace=True)

        df_transposed = df.T

        # Plot the area chart.
        plt.figure(figsize=(16, 9))

        for indicator in df_transposed.columns:
            plt.fill_between(df_transposed.index, df_transposed[indicator], alpha=0.7, label=indicator)

        # Labels w/ green theme.
        plt.xlabel('Years', color='green')
        plt.ylabel('Percentage', color='green')
        plt.title('Niger Economic Indicators', color='green')

        plt.gca().set_facecolor('grey')

        # Alot of years so I can do the tilt.
        plt.xticks(rotation=45)

        plt.legend(loc='center', bbox_to_anchor=(0.7, 0.92), fancybox=False, shadow=True, ncol=1)
        plt.tick_params(axis='x', colors='black')
        plt.tick_params(axis='y', colors='black')

        # Needed to show that negative GDP and Inflation.
        # Mainly so I can highlight why that is not good thing during the brief.
        plt.ylim(-2, 15)

        # Add a text box with information.
        # This was fun to mess with.
        text_box = '''
        Over 26 Years

        World GDP growth: 3.00% vs Niger GPD growth: 5.10%

        World Inflation: 3.62% vs Niger Inflation: 2.19%

        World Unemployment: 5.78% vs Niger Unemployment: 1.83%
        '''
        plt.text(0.02, 0.98, text_box, transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        plt.show()

    def plot_world_governance_indicators(df, indicator_codes):
        """
        Plots the world governance indicators for Niger as a line chart.

        Args:
            df (DataFrame): The DataFrame containing the world governance indicators.
            indicator_codes (list): The list of indicator codes to plot.

        Returns:
            None.
        """

        style.use('fivethirtyeight')
        plt.figure(figsize=(16, 9))

        for indicator in indicator_codes:
            indicator_data = df[df['Indicator Code'] == indicator]
            plt.plot(indicator_data.columns[4:], indicator_data.iloc[:, 4:].values.flatten(), marker='o', label=f'{indicator_data["Indicator Name"].iloc[0]}')

        plt.xlabel('Year', color='green')
        plt.ylabel('Aggregate Indicator', color='green')
        plt.title('World Governance Indicators For Niger', color='green')

        plt.plot([], [], ' ', label="Coup: Change of Power")
        plt.plot([], [], ' ', label="Attempted Coup")

        plt.gca().set_facecolor('grey')
        plt.xticks(rotation=45)
        plt.tick_params(axis='x', colors='black')
        plt.tick_params(axis='y', colors='black')

        plt.legend()
        plt.show()

# Conditional check used to determine if the class/function is being run as a standalone program 
# or if it has been imported as a module into another script. 
# If it's standalone, the code inside the if block will execute. Otherwise, it won't.
# In this case, nothing happens (indicated by 'pass') when the script is run as standalone.
if __name__ == "__main__":
    pass