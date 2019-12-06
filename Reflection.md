### Reflection

Our dashboard does well in answering our research questions of understanding unemployment rates across industries over a range of years. It also allows the user to interact with the plots in various ways with a radio button, year slider and multi-option select tabs using the many features that dash has to offer. Our dashboard is simple, yet effective, especially when we divided the graphs into 3 tabs. This allows the user to focus on one plot at a time and to gain insight from every graph. Despite the limited amount of data given, we were able to display two different variations of statistics for unemployment rates. 

Due to time constraints and the extent of our knowledge, there were a couple of known limitations:

- In plot 1, our year range slider for our plots cannot be restricted so that the same year is chosen for the range. This creates single points on the graph that holds no significance for the user to see.
- The changes to the slider is quite static and we hope for the future to include a smooth transition slider when selecting different ranges. 
- Add more space between Rate and Count Bubbles, we are having difficulties solving this issue.

We also would have liked to add more features on our app that allow deeper interactions of the plots for users to understand the trends more clearly. For example, a detailed tooltip that could tell us more information about the country’s industry, but due to a limitation of our dataset we were not given what country this data was collected from.
- We used the Github issues to create a to-do list that let us communicate with each other the tasks at hand and made sure we were following our timeline and team contract.

Here are the main issues we will be working on and the bugs we have fixed from the peer review feedback:  https://github.com/UBC-MDS/DSCI532_Group112_Unemployment/issues/41 

* Subtitle specifies "rate" when both rate and count options are available 
      - This is more of an informational change to provide users more context and gives more clarity on what to expect for the plots. 
      
* Remove 2010 from the seasonal unemployment plot since there is only data for first 2 months (we should fix it)
      - 2010 only had two months worth of data so it wasn't very useful for user to see this year in the third plot. 
      
* Zooming functionality in the plots is probably not necessary (we should remove this function)
      - Users may mess around with the zooming function too much and it doesn't provide any insight so we decided to remove it. 
      
* Change the slider bar in the 3rd tab to something else (we'll do that if we have time)
      - One of the users in the feedback session found the slider bar to be confusing as we are picking only one year but the slider bar has a shading that may lead users to believe they are choosing a range. 

* Save filter criteria when switching between tabs (we'll try to do that if we have time and if it is possible)

* Have a dashed line for the total industry average that the individual industries can be compared to. (Try to add this feature in our R app)


<b> Feedback Lab Reflection </b> 

Overall, the users had a relatively easy time manuvering around our app. They found it useful and well displayed. We were surprised to find some great feedback and suggestions that were overlooked during our time of creating the app. One example we found useful that we will try to do in our R app is to have an average of all industries compared to the industries individually. Due to time restraints we are unable to complete all the issues that were raised, these are displayed in our known limitations. 

