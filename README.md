# University Data Summarizer

This Python-based command-line tool fetches and summarizes open-source online university metadata from http://universities.hipolabs.com/search. It provides various ways to query and display university information globally, by country, by province, and through a search function.

## Features

1. Global University Statistics
2. Country-specific University Statistics
3. Province-specific University Listings
4. University Name Search

## Requirements

- Python 3.12 or higher
- Required packages: requests, tabulate

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/avivilloz/university-data-summarizer.git
   cd university-data-summarizer
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

The tool is used via command-line arguments. Here are the available options:

- `--global`: Show global university statistics
- `--country=COUNTRY`: Show statistics for a specific country
- `--country=COUNTRY --province=PROVINCE`: Show universities in a specific province of a country
- `--search=QUERY`: Search for universities by name

### Examples

1. Global University Statistics:
   ```
   python uni.py --global
   ```
   This command displays a table showing the number and percentage of universities in each country.

2. Country-specific Statistics:
   ```
   python uni.py --country=CA
   ```
   This command shows statistics for universities in Canada, broken down by province.

3. Province-specific University Listings:
   ```
   python uni.py --country=CA --province=ontario
   ```
   This command lists all universities in Ontario, Canada.

4. University Name Search:
   ```
   python uni.py --search=toronto
   ```
   This command searches for universities with "toronto" in their name and displays the results.

## Output Format

The tool uses tabulate to present data in a grid format. The exact columns depend on the query type, but generally include:

- For global and country statistics: Rank, Country/Province, Number of Universities, Percentage
- For province listings: Rank, University Name, URL
- For search results: Rank, University Name, Country Code, Province, URL

## Notes

- The tool fetches data in real-time from the API, ensuring up-to-date information.
- Country codes and full country names can be used interchangeably in queries.
- The search function is case-insensitive and matches partial names.