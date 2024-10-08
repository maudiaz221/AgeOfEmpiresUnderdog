# Code/Software

This project comprises six Jupyter notebooks and one Python script designed to analyze and process data from Age of Empires (AoE) tournaments.

## Notebooks and Scripts

### 1. 3types.ipynb

This notebook divides all tournaments into three types: hidden, s-tier, and normal. It ensures that these classifications collectively match the original comprehensive dataframe containing all registered match data.

### 2. cleaning.ipynb

Performs an SQL query to extract data from a local AoE database. It tests if a given match involves an underdog player, serving as the main notebook for data extraction and initial cleaning.

### 3. connect.ipynb

Joins AoE Elo data with Liquipedia data. Liquipedia is used to obtain additional player information, enriching the dataset.

### 4. PlayerData.ipynb

Extracts and formats player information from the Liquipedia website, ensuring name consistency across databases.

### 5. Regression.ipynb

Utilizes sklearn to run simple logistic and linear regressions on the data to determine whether a player is an underdog or not.

### 6. stats.ipynb

Generates generalized statistics about players, tournaments, and matches using the dataframes created by the other notebooks.

### 7. scrape.py

Scrapes data from Liquipedia to determine which tournaments are s-tier, hidden, or normal.

## Folders

- **players**: Contains data scraped from Liquipedia using its API.
- **TempData**: Contains all necessary data for processing and storing information, including tournament, match, and player data.
- **TempData**: Contains all the main data for the analysis and statistics.
- **sql**: Contains the .sql database from aoe-elo.com.

## Process Overview

The process is divided into two main parts: Extraction and Cleaning.

### 1. Extraction

Involves primarily extracting data from the aoe-elo.com database stored in an SQL file. Additional information is obtained from the Liquipedia player data acquired through the Liquipedia API.

### 2. Cleaning

Involves using regex and pandas to organize the data as effectively as possible, as the scraping process provides unordered data.

## Main Packages Used

- **Pandas**: For data cleaning.
- **re**: For data cleaning.
- **BeautifulSoup**: For web scraping.
- **requests**: For web scraping.
- **mysqlconnector**: To handle the database from Python.
- **sklearn**: For the regressions.
