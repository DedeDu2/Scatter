# Plot scatter plot of two columns in the dataset
def plot_scatter_plot(dataset, x_column, y_column):
    dataset.plot.scatter(x=x_column, y=y_column)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot")
    plt.show()

# Example usage:
plot_scatter_plot(dataset, 'x_column_name', 'y_column_name')
