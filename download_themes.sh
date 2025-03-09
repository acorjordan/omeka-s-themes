#!/bin/bash
mkdir -p themes

echo "Reading themes.yml..."
themes=$(yq e '.themes[] | select(.download == true) | .link' themes.yml)

for url in $themes; do
    filename=$(basename "$url")
    echo "Downloading $filename..."
    wget -q "$url" -O "themes/$filename"
    echo "Extracting $filename..."
    unzip -q "themes/$filename" -d themes/
    rm "themes/$filename"
done

echo "All themes downloaded and extracted."

echo "Removing .git directories..."
find themes -type d -name ".git" -exec rm -rf {} +
echo "Cleanup complete."
