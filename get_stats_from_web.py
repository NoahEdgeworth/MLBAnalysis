import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape batting stats for a given team abbreviation
def scrape_batting_stats(team_abbreviation):
    url = f"https://www.baseball-reference.com/teams/{team_abbreviation}/2023.shtml"  # Replace with the actual URL structure

    # Send a GET request to the URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table containing batting stats data
        table = soup.find('table')  # Adjust this based on the HTML structure of the page

        # Extract data from the table and write to CSV
        if table:
            rows = table.find_all('tr')
            header = [th.text.strip() for th in rows[0].find_all('th')]

            with open(f'master_batting_stats.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)

                for row in rows[1:]:
                    data = [td.text.strip() for td in row.find_all('td')]
                    writer.writerow(data)
        else:
            print(f"No batting stats table found for {team_abbreviation}")
    else:
        print(f"Failed to retrieve data for {team_abbreviation}. Status code: {response.status_code}")

# List of team abbreviations
team_abbreviations = [
    'ARI', 'ATL', 'BAL', 'BOS', 'CHW', 'CHC', 'CIN', 'CLE', 'COL', 'DET',
    'HOU', 'KC', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYY', 'NYM', 'OAK',
    'PHI', 'PIT', 'SD', 'SF', 'SEA', 'STL', 'TBR', 'TEX', 'TOR', 'WSN'
]


# Loop through each team and scrape batting stats
for abbreviation in team_abbreviations:
    scrape_batting_stats(abbreviation)
    time.sleep(2)
