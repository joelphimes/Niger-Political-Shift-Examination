import seaborn as sns
import folium
import matplotlib.pyplot as plt
from matplotlib import style
from folium.plugins import HeatMap

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

if __name__ == "__main__":
    pass