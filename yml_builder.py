import requests
from bs4 import BeautifulSoup
import yaml

# URL of the Omeka S themes page
URL = "https://omeka.org/s/themes/"

# Fetch the page content
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

themes = []

# Extract theme data
div_entries = soup.find_all("div", class_="addon-entry")
for entry in div_entries:
    title_tag = entry.find("h4")
    download_tag = entry.find("a", class_="button")
    version_tag = entry.find("span", class_="version")
    updated_tag = entry.find("span", class_="date")

    if title_tag and download_tag:
        title = title_tag.text.strip()
        link = download_tag["href"]
        version = version_tag.text.replace("Latest Version: ", "").strip() if version_tag else "Unknown"
        updated = updated_tag.text.replace("Updated: ", "").strip() if updated_tag else "Unknown"

        # Determine if the theme should be downloaded
        download = "archived" not in title.lower()

        themes.append({
            "name": title,
            "link": link,
            "version": version,
            "updated": updated,
            "download": download
        })

# Save to YAML
with open("themes.yml", "w") as file:
    yaml.dump({"themes": themes}, file, default_flow_style=False, sort_keys=False)

print("YAML file 'themes.yml' generated successfully!")
