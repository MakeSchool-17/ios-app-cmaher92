# Slingshot
Comparing twitter trends to market trends for more accurate investing

# Technologies
Python
Flask
MangoDB
Swift

# Description
Slingshot will be an iOS app in which a user can enter a hashtag and a stock exchange symbol to compare trends between the market and the buzz around the market. Will twitter trends play a direct roll in the market or is it strictly reactive?

# Financial Algorithm
The financial data will be focused strictly on price and volume during the MVP using either google finances or bloomberg.

The twitter data is where it gets difficult, there are two options, query the standard API each time the user searches a hashtag or set up a stream for every ticker symbol on the stock exchange. This issue with the querying each time the user wants to check a hashtag is that the data is limited to what the API provides, which isn't a time-reflective as a stream. On the other hand if we set up streams and parse the data as it comes in-real time then the potential is much bigger. That's what will allow future analytics that aren't possible as an MVP, including A.I. based on the comparisons of information over-time.

# MVP
- Decide how to query data from twitter's api constantly  
- Decide how to display data on the client (which graphing library if at all) (https://github.com/danielgindi/ios-charts)  
- Build algorithm for parsing stream and saving to database  
(Goal by 12/11/2015)  
- Build flask backend  
(Goal by 12/16/2015)  
- Build iOS client  
(Goal by 12/25/2015)  
- Handle syncing between realm & back-end  
(Goal by 1/1/2016)  
- Design app for demo-day  
(Goal by 1/8/2016)  

# Future Goals
- Integrating with robinhood  
- Integrating with coinbase  
- Improved algorithm  
- Machine learning?!
