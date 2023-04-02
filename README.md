# geojson-combine
A simple script to combine multiple GeoJSON files into one

## Functionality
This script will look through all subdirectories of the directory it is launched from. For each subdirectory, it will find all `.geojson` files, and extract their `features`.

The script then combines these `features` for each subdirectory and generates one `.geojson` file for each subdirectory. It only deals with `features`, and no other GeoJSON metadata.

## Instructions

1. Ensure you have Python 3 installed
2. Place the `.geojson` files you wish to combine into a subdirectory of the directory where the script is (the directory name will be the combined file's name)
3. Run the script
