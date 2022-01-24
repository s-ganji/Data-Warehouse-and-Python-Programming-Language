# Data-Warehouse-and-Python-Programming-Language
Implementation of series of tasks and queries on a table in MySQL database using Python programming language, Data Mining first course assignment, Fall 2019
## Question 1
Read countries_by_continent.csv and london12.csv files from input, then with their data create london12 table in olapdb database in MySQL with these columns: (id, continent, country, gender, agegroup, sport, gold, silver, bronze) <br/>
For agegroup column use the following table: <br/>
## Question 3
Create all possible single and combinatory indexes for sport, agegroup, gender, country, continent columns. The type of index should be BTree.
## Question 4
Draw the following diagrams:
- Bar chart of the top 10 countries in terms of number of participants
- Circular diagram of medal distribution on different continents
- Bar chart of the top 10 countries in terms of The ratio of medals to the number of participants among all countries with at least 30 participants. For each country, draw the ratio of the number of gold, silver and bronze medals in separate columns.
## Question 5
Generate all the possible queries with dice, slice and drilldown operations and sport, agegroup, continent and gender values. Report the following queries:
- Lead to the classification of the values ​​that have the highest relative standard deviation for the number of medals obtained. In answering this section, consider the followings:
1. Consider only queries that output a sub-cube with at least 100 records and 20 medals
2. The relative standard deviation is calculated as CV = σ /µ.
- Have the highest ratio of total medals to the total number of records. Consider the following limitation in responding to this section:
1. The query result must be a sub-cube that covers at least 10 records.
- The query that results in the most developing sub-cube. The most developing sub-cube is defined as follows:
1. Percentage or more of medals are silver and bronze.
2. Have the most number of medals.
- The query that results in the most developed sub-cube. The most developed sub-cube is defined as follows:
1. More than 50% of medals are gold.
2. Have the most number of medals.
