
# Summary
I tried to explain the flight delays in the USA between 1987 and 2008 by weekdays, location, carriers. The first dashboard is looking at the delays from the flight's departures, showing us the carriers that were delayed and also over view where in the USA is liekly to be deplayed based on the number of records. The same story goes for dashboard two, but this time looking at the arrivals delays.

# Design
### Data Preparation
The original data is by far the biggiest data (10GBs) and had about 120 millions rows with 22 files for each year with 29 variables. For visualization purposes I had to combine all the files together. Since the data was still huge, I, then, ran an cluster instance in google cloud to run VM jupyter notebook, to aggregate it by 'Year' and 'Day', then making several other grouping files for, 'Year' and 'Carrier', 'Year' and 'Origin', 'Year' and 'Destination' to obtain the mean values of 'ArrDelay' and 'DepDelay'. Then used the relation mapping in tableau to combine the files all together. I added a new variable to obtain the total delay per flight by using the flight_agg_year code in Juyter Notebook. 


### Added from Review new
For the Story telling section 1) I choose an horizontal bar to illustrate my top favorite 5 flight carriers, which the graph visually show a ranking of my top 5 favorite carriers that are likely delayed. 2) In this section, I wanted to compare the average baseline of weekdays that flights are on average delayed, against the actual delays of each carrier for the particular weekday. I choose the baseline to be area line, and the actuals to be doted lines. 3) In this section, I choose the mapping graph to illustrate which airports are likekly to be delayed with two clusters, and the two clusters show us which top clustered airplot is always delayed. 4) In this final section, I choose the mapping graph to illustrate which of the airlines is likekly to be delayed based on you destinated airport. This was created with carriers being clustered and mapped thru all the aiports. Give it try and let me know, you next destination and the airline that will totaly be late based on the 2003 to 2008 filtered data. :) 


### Visualization

I choose the line graph, bar graph and also mapping to visualize and present my findings for delays changes. I created four charts in total initially, but added more features as i combined more files that had relationships.
1. A bar graph showing only average total delays in y axis and day on x axis. Days denoted as Weekdays.
2. A Line graph showing only average total delays in y axis and year on x axis.
3. A line graph showing only average total delays in y axis and year on x axis. Day1 denotes as different colored lines.
4. A line graph showing only average total delays in y axis and year on x axis. Carrier denotes as different colored lines.

Added:
5. A bar graph showing only average total delays in y axis and carriers on x axis. 
6. A map graph showing all the origion location with size denoted as averge departed delays, with number of records denoted as color.
7. A map graph showing all the destination location with size denoted as averge arrival delays, with number of records denoted as color.

8. Combined two dashboards, one for origin on average delays, and then arrival on average delays with the airport location mapped.

The initial design can be seen as flight_vizz.(final) (attached)

After I received some feedback, did some chagned on my design. 
* For clearer visualization, I changed the color to display a better story.
* For the Dashboard one, changed around the graph, the viewer felt that the graphs where to clustered at the top. Same went with dashboard one with minor changes.  
* To provide more color scheme, I customized the mapping colors to be the same with stronger color differenciater.


So the final design can be seen flight_vizz.(Final) (attached)

#### After reviewing 1 submittion

File name is flight_vizz_resubmitted (attached)

# Feedback
1. It looks very good on the color choices. 
2. You need to make the color to be more matching differenciated almost like a dark rainbow. 
3. What did it look like from 2004 to 2008 for arrival delays for destination. 


# Resources

* [Data](http://stat-computing.org/dataexpo/2009/the-data.html)
* [stackoverflow](http://stackoverflow.com/)
* [Google](https://console.cloud.google.com)
