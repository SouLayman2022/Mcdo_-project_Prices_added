import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to site
url = "https://prixdesmenus.com/mcdonalds-menu/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables with the specified class
tables = soup.find_all('table', class_='has-fixed-layout')

# empty list to store data
table_data = []

# Extract data from each table
for table in tables:
    # Find all rows in the table body
    rows = table.find_all('tr')
    
    # Extract data from each row
    for row in rows:
        # Find all cells in the row
        cells = row.find_all(['td', 'th'])
        
        # Extract text from each cell and remove leading/trailing whitespace
        row_data = [cell.get_text(strip=True) for cell in cells]
        
        # Append row data to table data list
        table_data.append(row_data)

# Convert table data to a DataFrame
df = pd.DataFrame(table_data[1:], columns=table_data[0])

# Clean missing vals
df_clean = df.dropna()

# Save to CSV file
df_clean.to_csv('mcdonalds_menu_1.csv', index=False)
