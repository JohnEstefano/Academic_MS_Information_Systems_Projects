
# Summary

For this project, I will be using the "Baseball Data" dataset provided by Udacity. This data set contain 1,157 baseball players including their handedness (right or left handed), height (in inches), weight (in pounds), batting average, and home runs. The purpose of this project is to create a visualization that shows differences among the performance of the baseball players based on their height, weight and handedness.

# Design

#### Data Story
First, we must define our measure of performance. There are only 2 metrics within the dataset that measures the output of a player; their "batting average" and "home run" metrics. For each of these measures, the higher the number, the better a player's performance. 

I have "featured engineered" 2 new metrics. BMI and Performance. 
Formulas:
Performance = ([Avg]/.300)+([HR]/294)
BMI = 703*([Weight]/([Height]*[Height]))

This was done to help consolidate most metrics into two that can be easily plotted against each other to use as a "summary chart".

#### Tableau Story
I decided to go with scatter plots and barcharts for my charts. Mainly because it can highlight correlations (or lack of) between the chosen variables in quantitative data and display the distribution of the data respectfully. I added color to highlight the majortiy amount of records/rows and the correlation it presents.

The barchart on the first page of the story was chosen to show how the data was distributed. It has helped me see that the batting average for each handedness is bimodal and negatively skewed. It also helps display that the data for home runs is unimodal and positively skewed for each handedness.

The 4 chart layout on the second page was chosen because the same 2 variables where plotted against the other 2 (batting average and homeruns for both weight and height). I chose scatter plots to help highlight whether there was a correlation between weight vs both batting average and home runs. As you can see from the scatter plot, there does not seem to be any correlation between height vs both batting average and home runs or between weight vs both batting average and home runs. Most baseball players are clustered between Height(70-76) and weight (170-220) batting average (0-0.3)/ homeruns (0-200). Height nor weight correlates to higher performance in both of those metrics. When filtering for Left, right or both handedness, the fact still remains true! 


The 2 chart layout on the third page was chosen because the BMI vs Performance is more evidence for the point made in the first page (no correlation exists) and coupling it with the homeruns vs batting average would conclude and drive point home by mentioning that batting averages do not correlate with home runs because one is a derivative of the other. I chose scatter plots to help highlight whether there was a correlation between Performance vs both BMI and Batting Average. Taking a look at the a scatter plot, there does not seem to be any correlation between BMI vs Performance. Most baseball players are clustered between a BMI (22-28) and Performance (0.5-1.5). BMI does not correlate with higher performance. Home runs and batting average do display some type of relationship, which makes sense, since home runs count towards hits, which rises batting average. Again when filtering for Left, right or both handedness, the fact still remains true! 

The legends where left for chart readablity, and handedness filter was applyed to visualize highlight the same findings within each particular handedness group.


# Feedback #1

##### What do you notice in the visualization?

Person#1: The colors and the clustering presented a majorty

##### What questions do you have about the data?

Person#1: Why is there so few data on baseball players, and why aren't there more entries.

##### What relationships do you notice?

Person#1: Aside from batting average and homeruns, that there weren't any relationships.

##### What do you think is the main takeaway from this visualization?

Person#1: That a player's height and weight will not predict or add on to a player's success as a performer in baseball (for home runs and batting average anyway)

##### Is there something you don’t understand in the graphic?

Person#1: not really, all looks pretty good and straight forward to understand.


# Feedback For Version 2

##### Please describe your project with a title by changing the name of "Story" into a more meaningful name.
Story Named has been changed.

##### Explore more findings and state them in your summary, as it's the 1st part that readers will notice. Readers must have a clear view of your project.
An extra insight was described in the story.

##### Try to use another chart type other than the Scatter plot chart, as you've only used one type of chart.
A barchart was added to the story.

##### Provide the reasons behind choosing each chart in the design section. For example: "I chose the scatter plot chart to show... and it has helped me in..."
Reasons and how the charts helped my analysis was documented within the story.

##### Feedback collected and documented, but please provide your responses to each feedback point and whether you've fixed it or not.
Done.

##### You must provide two links, one for the 1st version and another one for the last/final version of your project as an evidence that your visualization has been improved.
Please look below.

# Resources

#### Link to Data set
https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud507/baseball_data.csv&sa=D&ust=1544199829269000

#### Link to TABLEAU STORYS

##### Version 1
https://public.tableau.com/views/Udacity_Project_8/Story?:embed=y&:display_count=yes&publish=yes

##### Version 2
https://public.tableau.com/views/Udacity_Project_v2_0/Story?:embed=y&:display_count=yes&publish=yes

