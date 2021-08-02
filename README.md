# IR_Coursework

## Search Engine Process followed in Task 1 of the CourseWork:

![alt text](https://github.com/rajaramkuberan/IR_Coursework/blob/main/Search_Engine.jpg)


### 1. Web Crawler: 
   The [Pureportal website of Coventry Scholars](https://pureportal.coventry.ac.uk/en/organisations/coventry-university/persons/) is crawled to obtain the data to create a search engine similar to Google Scholar. The python codes for profile and research output crawling is as below:

[Web Crawler for Profiles](https://github.com/rajaramkuberan/IR_Coursework/tree/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Crawler_bs4/Crawler_Profile)
[Web Crawler for Research Output](https://github.com/rajaramkuberan/IR_Coursework/tree/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Crawler_bs4/Crawler_Paper)

### 2. JSON Output data file of the Research Paper:
   The crawled or scrapped data is stored in the form of key value pairs, and the best format is JSON file which can be further imported into the NOSQL database like MongoDB for production level deployment of search engines.
   
   [Research Output JSON file](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Crawler_bs4/Crawler_Paper/Final_Cov_Research_Paper.json)
