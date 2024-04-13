import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
url = "https://marketingfoodonline.com/blogs/news/mcdonalds-full-updated-2023-menu-with-pricing-and-all-food-menu-items"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all tables containing menu items and prices
tables = soup.find_all("table", class_="__reading_mode_data_table_class")

# Create a CSV file to store the data
csv_file = open("mcdonalds_menu.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Foods", "Size", "Prices"])

# Extract data from each table and write it to the CSV file
for table in tables:
    for row in table.find_all("tr")[1:]:
        columns = row.find_all("td")
        food = columns[0].get_text(strip=True)
        size = columns[1].get_text(strip=True) if len(columns) > 1 else ""
        price = columns[-1].get_text(strip=True)
        csv_writer.writerow([food, size, price])

# Close the CSV file
csv_file.close()

print("Menu items and prices extracted and saved to 'mcdonalds_menu_3.csv'.")
