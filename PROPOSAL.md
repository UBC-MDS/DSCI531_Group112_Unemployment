# Proposal: Unemployment rates 

## Section 1: Motivation and Purpose
  
  Unemployment rates can inform us on the rise and fall of a country’s economic condition. The purpose of this dataset is to show which industries have been decreasing or increasing in the number of jobs available. We would expect the industries that are implementing more automation to have higher rates of unemployment. Understanding unemployment trends could help us address economic challenges and determine which industries are facing job losses or gains. This dashboard will be used to compare various industries unemployment rates as well as see their trends change over time for the specific country. 
	

## Section 2: Description of the data

We will be visualizing the Unemployment Across Industries dataset gathered from the [vega datasets](https://github.com/vega/vega-datasets) with 6 variables and 1708 observations. The `series` column gives us the 14 industry types in the dataset. The industries in the dataset are:

* Government, Mining and Extraction, 
* Construction, Manufacturing, 
* Wholesale and Retail Trade, 
* Transportation and Utilities, 
* Information, 
* Finance, 
* Business services, 
* Education and Health, 
* Leisure and hospitality, 
* Other, 
* Agriculture, 
* Self-employed

 There is also a `year` column with the years 2000 and 2010 and a `month` column. The monthly unemployment information across various industries from 2000 to 2010 of an unknown area. It is unclear whether this area is a town, city, or country and for the purpose of the assignment, we will call it "Country X". The dataset contains the unemployment in two forms: the number of people who are unemployed (`count`) and the rate of unemployment (`rate`). We presume that the rate of unemployment is the proportion of people who are unemployed in a specific industry for that given year. 

## Section 3: Research questions and usage scenarios

This dashboard works to answer questions on industries unemployment trends with visualizations. Our dashboard could serve as a framework for officials to gain insight into their countries industry employment trends and implement changes pertaining to the results. For instance, the officials can change policies such as cutting taxes for certain industries that have higher unemployment rates. Our research questions are as follows: 

1) Which industry has grown/shrunk the most?
2) How does overall unemployment change in country X over the years?
3) Is the unemployment rate across industries seasonal?

