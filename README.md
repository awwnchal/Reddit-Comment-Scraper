# Reddit Comment Scraper
This project focuses on scraping comments from a chosen post on Reddit and storing them in a MongoDB collection. The script retrieves the first 5 comment threads with a maximum depth of 3 and organizes the comments in a nested structure. Additionally, a MongoDB query is provided to retrieve all the replies and nested replies for a given comment in a specific format.

 Prerequisites
 
To run this project, you will need:

Python 3.x

PRAW (Python Reddit API Wrapper)

MongoDB


# Project Overview

1. Scraping Reddit Comments

The first part of the project involves scraping comments from a chosen post on Reddit. The script utilizes the PRAW library to interact with the Reddit API and retrieve the comments. It specifically retrieves the first 5 comment threads with a maximum depth of 3. The comments are then stored in a MongoDB collection.

2. Querying Comment Replies

The second part focuses on querying the stored comments in MongoDB to obtain all the replies and nested replies for a given comment. The query utilizes the $graphLookup aggregation pipeline operator, which allows traversing a graph-like structure to retrieve nested documents. The results are formatted in a specific structure that includes the comment ID and an array of replies, each containing its comment ID and text. Replies can be nested, and the structure follows the same format recursively.
Getting Started

Follow the steps below to set up and run the project:

Clone the repository to your local machine.

Install the required dependencies by running pip install -r requirements.txt.

Create a Reddit Developer application to obtain the necessary credentials (client ID, client secret, and user agent). Refer to the PRAW documentation for detailed instructions.

Configure the MongoDB connection in the code by updating the appropriate variables in the config.py file.

Update the Reddit credentials in the config.py file.

Run the main script using python main.py.

Acknowledgments

This project is inspired by the need to extract and analyze comments from Reddit posts. 
