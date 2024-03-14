# BrainStroke-Analysis-using-Python-and-Power-BI
Brain Stroke Analysis Using Python and Power Bi.

Problem Statement :
The problem statement for the analysis on the data was whether the person will have brain stroke or not.
For this we need to have potential solution to predict it
So the process for the analysis was done and breakup of it is given below.

Process Steps:

1.Python

It is used to do the data cleaning, extraction, Eda, nullity/Na checking as well as to visualize the data where can we better understand how many are affected due to brain stroke

a.	Libraries import

We have taken libraries like pandas, numpy, matplotlib, seaborn, scikitlearn.
Model for the analysis was Logistic Regression imported from scikitlearn.

b.	Data check

As there were null and na values in the data we have to clean the data to get the accurate and precise result

c.	Data extraction

We need to extract, delete, manipulate some columns, rows which were important (primary) for the analysis and to discard the unnecessary columns and rows

d.	Data Check

Need to verify the columns and rows, outliners as well as dtypes we are performing on the data as they play a main role in analysis

e.	All set to visualize

Using mathplotlib library we have visualize the data in box plot for the age as need to check the what is the least and most age of people in the data and figure out the mean of it and after that done histogram plot on the population having brain stroke or not w.r.t male and female. Also, visualize the stroke status of particular gender with histogram and plot a line plot for the average bmi of the age w.r.t genders

f.	Train 

We have trained 80% of the dataset to perform logistic regression

g.	Test 

We have tested 20% of the dataset

h.	Split

It was splited into random form.

i.	Accuracy and Precision

After performing logistic regression on the dataset we got 87% accuracy and 22 % of precision.

2.	Power Bi

Power Bi was used to generate interactive report were we can easily interact with the data as we have done the visualization of the data in scatterplot, barplot, donut chart, pie chart and card chart to show the actual reading of the selected data from the dataset.

Conclusion : 

Using the Python ( Jupyter notebook) and Power Bi the analysis was done on the dataset and it was conclude that the men population are having more brain stroke compared to female population. 

