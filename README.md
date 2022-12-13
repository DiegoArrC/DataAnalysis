# Overview

I am using Python Pandas to analyze a fitness exercise dataset. The dataset includes information about different exercise names, target muscle groups and target muscles, and the equipment necessary for that specific exercise. The idea behind creating this data analyzer for this fitness exercise dataset was to develop a more honed understanding of creating visualized data through filtering and aggregation through the use of one of the well known data analysis tools, python pandas.

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

There were two primary questions that I was trying to answer using the information form this data set. The first question was of which body parts each piece of equipment covered and how many exercises fit those parameters. The second question was for how many different pieces of equipment could be used for specific muscles within generalized muscle groups.

From doing the analysis, I have found that abs are the muscles that were most exercisable, given the dataset, which used tires as the primary exercise equipment for development. As for the first question, body weight is the primary source for doing any exercise, being near equivalent in count to the 3th and 4th most used exercise equipment, cables and barbells.
# Development Environment

* Visual Studio Code 1.74.0
* Python 3.10.1
* Python Matplotlib
* Python Pandas
* Python Numpy

# Useful Websites

* [Fitness Exercise Dataset From Kaggle]( https://www.kaggle.com/datasets/edoardoba/fitness-exercises-with-animations)
* [Pandas Bar Plotting]( https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)

# Future Work

* Make the bar generation functions more abstract to allow multi-parameter input as opposed to hard-coded values
* Create custom graphing of data beyond a bar chart. Example would be area highlights on a human body template.
