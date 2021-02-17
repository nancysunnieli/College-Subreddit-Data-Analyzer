Name of Group: JSEN<br /><br />

Group Members: Sarah Zhang, Evan Xiang, Jingwen Zhang, Nancy Li<br /><br />

WEEK 6-7:<br /><br />
Sarah, Evan, and Jingwen work on their tasks and finish them<br /><br />
WEEK 8:<br /><br />
Nancy integrates their tasks with the website. After this, we will submit the project<br /><br />


To run the program:<br /><br />
1.) Enter the directory called "collegesubredditwebsite". To do this, run the following command in your terminal: "cd collegesubredditwebsite". <br /><br />
2.) Enter the follwing command in the terminal: "python3 manage.py runserver".<br /><br />
2.) This will output a link. Copy and paste the link in the desired internet browser.<br /><br />
3.) Explore the pages on the website, which are as follows:<br />
  - Home: This is a welcome message<br />
  - About: This gives an explanation of the project and the pages<br />
  - Top Keywords: This outputs the top keywords given parameters from the user<br />
  - Word Prevalence: This outputs a graph of the percentage usage of a given word over time given parameters from the user<br />
  - Similarity: The compares the similarity of two colleges given parameters from the user<br />
  - Upvotes Analysis: This provides an analysis of the upvotes on the posts given parameters from the user<br />
  
 
Description of files in this repository: <br />
1.) csv files:  <br />
  a.) word_raw_data.csv maps words to the post they are from. <br />
  b.) all_raw_data.csv contains all the raw data that was scraped from reddit APIs. It has the following columns: downs (number of down votes), epoch_time (time of post in epoch time), score (computed by reddit), subreddit (name of college the post is from), text (the raw text of the post), title (the title of the post), unique_post_id (unique post id), ups (amount of up votes), upvote_ratio (ratio between up and down votes). <br />
  c.) Yale_raw_data.csv, Stanford_raw_data.csv, UPenn_raw_data.csv, UChicago_raw_data.csv, Princeton_raw_data.csv, MIT_raw_data.csv, JHU_raw_data.csv, Harvard_raw_data.csv, and Caltech_raw_data.csv contain the same data as all_raw_data.csv. The difference is that it splits the data up by college.  <br /><br />
  
2.) reddit_scraping.py: this was the program used to scrape reddit APIs. <br /><br />
3.) Set_Up_Database.py and create_tables_in_sql: these were used to set up the db.sqlite3 database using the csv files. <br /><br />


4.) nancy_word_prevalence.py: This was the program used to create the word prevalence graphs  <br /><br />
5.) evan_top_terms.py: This was the program used to create top keywords/ngrams, as well as the wordclouds <br /><br />
6.) evan_word_saliency.py: This was evan's code from one of the PA's from CMSC 12100. She modified it and added some other helpful helper functions within the document. It is essentially a util file for evan_top_terms.py <br /><br />
7.) jingwen_scores_trend.py: This was the code created to generate a heatmap of popular posting times and topics <br /><br />
8.) sarah_word_similarity.py: This was the code created to compute similarity across schools.

9.) collegesubredditwebsite directory: This contains all the necessary files for the website.  <br /><br />

10.) Project_Proposal.pdf and edited_plan.pdf contain the overview and schedule of the project.
