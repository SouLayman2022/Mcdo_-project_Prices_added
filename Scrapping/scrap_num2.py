import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
url = "https://hackthemenu.com/mcdonalds/menu-prices/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all list items containing menu items and prices
menu_items = soup.find_all("li")

# Create a CSV file to store the extracted data
with open("mcdonalds_menu.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Item", "Price"])

    # Iterate over each list item
    for item in menu_items:
        # Extract the item name and price
        item_name = item.find("div", class_="kl-break-word")
        item_price = item.find("div", class_="kl-break-word", text=True)
        if item_name and item_price:
            item_name = item_name.text.strip()
            item_price = item_price.text.strip()
            csv_writer.writerow([item_name, item_price])

print("Menu items and prices extracted and saved to 'mcdonalds_menu_2.csv'.")
