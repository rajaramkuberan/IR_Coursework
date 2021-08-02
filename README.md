# IR_Coursework

## Search Engine Process followed in Task 1 of the CourseWork:

![alt text](https://github.com/rajaramkuberan/IR_Coursework/blob/main/Search_Engine.jpg)


### 1. Web Crawler: 
   The [Pureportal website of Coventry Scholars](https://pureportal.coventry.ac.uk/en/organisations/coventry-university/persons/) is crawled to obtain the data to create a search engine similar to Google Scholar. The python codes for profile and research output crawling is as below:

[Web Crawler for Profiles](https://github.com/rajaramkuberan/IR_Coursework/tree/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Crawler_bs4/Crawler_Profile)
[Web Crawler for Research Output](https://github.com/rajaramkuberan/IR_Coursework/tree/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Crawler_bs4/Crawler_Paper)
[Scheduler](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Scheduler.py)

### 2. JSON Output Data File of the Research Paper:
   The crawled or scrapped data is stored in the form of key value pairs, and the best format is JSON file which can be further imported into the NOSQL database like MongoDB for production level deployment of search engines.
   
   [Research Output JSON file](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Crawler_bs4/Crawler_Paper/Final_Cov_Research_Paper.json)
   
### 3. Data Preprocessing of JSON files and Index Creation:

The index is created to implement the search engine. The inverted index file is created in three columns such as word/vocabulary in the document, and its total count in the document, and finally the column where corresponding index positions are calculated. The below link contains Indexing python file with data preprocessing. 

[Indexing Code](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Indexer/indexer.py): The code outputs the index in key value pairs or dictionaries
[Inverted Index CSV file](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/inverted.csv):The corresponding CSV file is created for better understanding and simplicity.

### 4. Search Engine Query Processor:

The keywords are queried with boolean expressions augmented in the search query. Eg., AND,OR,NOT

Query Processor Code:[Last part of Indexing.py file](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Indexer/indexer.py)

### 5. Flask UI/Search Portal:

Flask framework is used to create the UI of the search engine portal.
Executing the [app.py](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/app/app.py) file to run the local host server where the created coventry university research papers are retrieved and the data is listed in the query results.

Website Design Codes:

[HTML Layout - layout.html](https://github.com/rajaramkuberan/IR_Coursework/tree/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/app/templates)
[Home Page of Research Paper Search Portal-search.html](https://github.com/rajaramkuberan/IR_Coursework/tree/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/app/templates)
[Query result page - search_result.html](https://github.com/rajaramkuberan/IR_Coursework/tree/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/app/templates)

## Task 2: Subject Classification of each research Papers:

### 1. Data Collection/Creation:

The dataset is created by processing and amalgamating the BBC Dataset and research paper scholar json file.

[Dataset](https://github.com/rajaramkuberan/IR_Coursework/tree/main/IRCW_Codes/Search_Engine_Coventry/Training_data)

### 2. Data preprocessing:

The dataset is preprocessed using the same process that is followed before the index creation.

[Dataset Preprocessing - 1](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/Data_preprocessing.ipynb)
[Dataset Preprocessing - 2](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Classification/Classification.py)

### 3. Model Creation:

The two Classification models used: MultinomialNB and SVC with Grid Search CV for better accuracy.

[Classification.py](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/Classification/Classification.py)

###  4. Classification result in the Search Portal:

[app.py](https://github.com/rajaramkuberan/IR_Coursework/blob/main/IRCW_Codes/Search_Engine_Coventry/pureportal_search_engine/app/app.py)

Flask Web framework by default loads in Port-5000 - [localhost:5000](http://localhost:5000/)
