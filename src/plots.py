import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter

# Plot class for line, bar, heatmap, stacked, and folium.heat
class Plot:
    """Example Usage:
        plotter = plots.Plot()
        plotter.plot_residuals(merged_data)
        ^something like that for most of'em
    """
    def __init__(self):
        pass

    def plot_residuals(self, merged_data):
        """
        Plots residuals against predicted values for a regression model on 'Amount_DAC' and 'Amount_GCF'.
    
        Args:
        - merged_data (pd.DataFrame): DataFrame with at least 'Amount_DAC' and 'Amount_GCF' columns.
    
        Returns:
        - None (shows the plot).
        """
        # https://towardsdatascience.com/how-to-use-residual-plots-for-regression-model-validation-c3c70e8ab378 

        # https://stackoverflow.com/questions/13218461/predicting-values-using-an-ols-model-with-statsmodels

        # needed to add that redline, just like we did in our exercises. 
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


    def bar_fa(self, PG4, figsize=(16, 9), custom_colors=None):
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
        # So wanting to get total aid to niger for last 25/26 years from each country
        # Sorting those for country name I just need to add across the DF. 

        # Numbers werent formatting properly, instad of doing pd.display.options I just did a for loop for the numbers.
        # This is so I can use the value in the call out boxes I plan to make. 

        # Alot of fidding with this since i was orginally plotting on the same ax multiple times. 

        # Doing the same thing as I did for the violin plot wanting the colors most
        # closely associated to those countries. 

        # After the feedback from the instructors the bubble chart was kinda lame. 
        # Doing the same thing with a bar chart, looks alot cleaner. 
        # Indicator Name is Country, Total Aid is new last summed column. 

        # Keeping the green lettering theme. 

        # Set the background color to grey.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html 


        # Messed with a lot of things to make the format of the y axis correct
        # Formatteer allows you to deal with the lettering which is nice. 


        # This (after some research) is where I figuered out I was plotting multiple times
        # I would have repeating y ticks and it was really driving me mad. 
        # Long story short even with the formatter and lim adjustments, manually set the ticks using a list comp.
        
        
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
        
        #Text box for Total UK Aid. 
        text_1 = f"Total Aid: {new[0]}"
        plt.text(0.01, 0.047, text_1, transform=plt.gca().transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        #Text box for Total EU Aid.  
        text_2 = f"Total Aid: {new[1]}"
        plt.text(0.125, 0.868, text_2, transform=plt.gca().transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        #Text box for Total SK Aid. 
        text_3 = f"Total Aid: {new[2]}"
        plt.text(0.255, 0.035, text_3, transform=plt.gca().transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        #Text box for Total FR Aid. 
        text_4 = f"Total Aid: {new[3]}"
        plt.text(0.375, 0.525, text_4, transform=plt.gca().transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        #Text box for Total GER Aid. 
        text_5 = f"Total Aid: {new[4]}"
        plt.text(0.5, 0.285, text_5, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        #Text box for Total CAN Aid. 
        text_6 = f"Total Aid: {new[5]}"
        plt.text(0.628, 0.114, text_6, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        #Text box for Total US Aid. 
        text_7 = f"Total Aid: {new[6]}"
        plt.text(0.75, 0.49, text_7, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        #Text box for Total JPN Aid. 
        text_8 = f"Total Aid: {new[7]}"
        plt.text(0.87, 0.15, text_8, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        #Text box for Perspective Metrics (coming from world bank summaries). 
        text_9 = """
        Numbers for Perspective:
        - Niger's Net ODA received, (2021 percentage of GCF): 43.18%
        - Sub-Sahran Region, (2021 percentage of GCF): 13.7%
        - Making Niger 10th Highest in Region for 2021.
        """
        plt.text(0.65, 0.98, text_9, transform=plt.gca().transAxes, fontsize=11,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        # Display the plot
        plt.show()

    def violin_ge(self, data, b_mean, m_mean, i_mean):
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
        # Create the violin plot.
        # I was trying to use niger colors, but it didnt really come out that well ..
        # That organge is really light. 


        # Figsize.


        # Adding the new colors to the palette. 


        # Set the background color to grey.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html 

        # Add a text box with information.


        # Add a text box for Leader 1 (use f string for mean).


        # Add a text box for Leader 2 (use f string for mean).


        # Add a text box for Leader 3 (use f string for mean).

        # Add labels and title.
        # Dont really want that y lable because the names are so long.


        # Sticking with the green theme.    
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
        
    def plot_ei(self, df):
        """
        Plots the economic indicators for Niger as an area chart.

        Args:
        df (DataFrame): The DataFrame containing the economic indicators.

        Returns:
        None.
        """
        # Set the 'Indicator Name' column as the index (optional but might help in chart labeling).
        # This did end up helping btw .. 

        # Transpose the DataFrame to make years as columns and indicators as rows.
        # This was more cautionary than anything with that new set of index / could always flatten if needed.. 
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html

        # Plot the area chart. 

        # Yet another loop since im going through years again.. 
        # Coloumns are the years and wanting to do each indicator by year. 
        # Label was similiar to above but dont have to make it iloc[0] cause its not double nested.
        # plt.fill_between is literally an area chart .. I searched for like two days for the keyword "area chart" .. 
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html

        # Labels w/ green theme.

        # Set the background color to grey.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html 

        # Alot of years so I can do the tilt.

        # Still cant figure out what fancy box does? when I turn it on it looks the same..

        # Needed to show that negative GDP and Inflation.
        # Mainly so I can highlight why that is not good thing during the brief. 

        # Add a text box with information.
        # This was fun to mess with.  
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

    def plot_wgi(self, df, indicator_codes):
        """
        Plots the world governance indicators for Niger as a line chart.

        Args:
            df (DataFrame): The DataFrame containing the world governance indicators.
            indicator_codes (list): The list of indicator codes to plot.

        Returns:
            None.
        """
        # Now to plot the graph. 
        # Use the style that I like.

        # Figsize.

        # For the line chart need each indicator code separate.
        # Not to repeat codes.
        # Using indicator code to cycle through.
        
        # X = Year, Y= Aggregated Indicator Scale.
        # values.flatten for the list of values.
        # https://pandas.pydata.org/pandas-docs/version/0.14.1/generated/pandas.Index.flatten.html 
        # F string for label, used in last project.
        # Will only be plotting 2000 on as it has complete data (which is why I have to slice it).
        # Label needs to start at the first postion each iteration.

        # Label and title. 
        #Label for Coup: Change of Power.
        #Set for empty lables.

        #Label for Attempted Coup.
        #Set for empty lables.

        # Set the background color to grey.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html 

        # Using all the years present for the xticks.
        # Set the tick color to black.

        # Show the legend.
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
        
    def plot_regression(self, merged_data, title, xlabel, ylabel):
        """
        Plots a regression graph using seaborn and decorates it using matplotlib.

        Args:
        - merged_data (pd.DataFrame): DataFrame containing the data to be plotted.
        - title (str): Title for the plot.
        - xlabel (str): X-axis label.
        - ylabel (str): Y-axis label.
        - textbox_content (str): Text content for the textbox in the plot.

        Returns:
        - A formatted regression plot.
        """
        # Now to do the plot. 
        # This really helped, just needed to do the subplots to make it work. 
        # https://stackoverflow.com/questions/40511476/how-to-properly-use-funcformatterfunc 
        # Now to do the plot. 
        # This really helped, just needed to do the subplots to make it work. 
        # https://stackoverflow.com/questions/40511476/how-to-properly-use-funcformatterfunc 
        #  Needed the subplots for the func fomatter.
        # https://www.geeksforgeeks.org/python-seaborn-regplot-method/
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html
        # Set the background color to grey.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html 
        # Title and Lables, keeping it green.
        #Text box for Summary Metrics. 
        def billions(x, pos):
            'The two args are the value and tick position'
            return f'${x*1e-9:.1f}B'

        formatter = FuncFormatter(billions)
        fig, ax = plt.subplots(figsize=(16, 9))
        sns.regplot(x='Amount_DAC', y='Amount_GCF', data=merged_data, ci=95, color='green', scatter_kws={'color':'orange'})
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_formatter(formatter)
        plt.gca().set_facecolor('grey')
        plt.title(title, color='green')
        plt.xlabel(xlabel, color='green')
        plt.ylabel(ylabel, color='green')
        
        #Text box for Summary Metrics. 
        text = """
        In Perspective:

        - R-squared (0.861): 
        86.1% of the variance can be explained by Net Bilateral Aid Flows.

        - F-statistic and Prob (F-statistic) (9.19e-12): 
        The model is statistically significant. 

        - Coef (const -4.749e+08 and Amount_DAC 5.3360): 
        With no aid flow, the Gross Capital Formation is -4.749e+08.

        - P>|t| (const and Amount_DAC) (<0.05):
        Both intercept and slope are significantly different from zero.
        """
        plt.text(0.01, 0.98, text, transform=plt.gca().transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        plt.show()

# Conditional check used to determine if the class/function is being run as a standalone program 
# or if it has been imported as a module into another script. 
# If it's standalone, the code inside the if block will execute. Otherwise, it won't.
# In this case, nothing happens (indicated by 'pass') when the script is run as standalone.
if __name__ == "__main__":
    pass