import os
import json

GEOJSON_EXTENSION = ".geojson"
EXTENSION_LENGTH = len(GEOJSON_EXTENSION)

BASE_FILE = "base" + GEOJSON_EXTENSION

def combine_all_airports():
    airport_directories = find_airports()
    for airport_directory in airport_directories:
        print("Combining airport directory " + airport_directory)
        airport_files = get_component_files(airport_directory)
        combine_files(get_airport_code(airport_directory), airport_files)

def find_airports():
    return [ f.path for f in os.scandir(os.getcwd()) if f.is_dir()]

def get_component_files(directory):
    result_files = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path) and is_geojson(full_path):
            result_files.append(full_path)
    return result_files

def combine_files(airport, file_paths):
    all_features = []
    for file_path in file_paths:
        with open(file_path, "r") as f:
            features = json.loads(f.read())["features"]
            all_features.extend(features)
    write_combined_file(airport, all_features)

def write_combined_file(airport, all_features):
    with open(BASE_FILE, "r") as base:
        airport_data = json.loads(base.read())
        airport_data["features"] = all_features
        airport_data_json = json.dumps(airport_data)
        with open(airport + GEOJSON_EXTENSION, "w") as airport_file:
            airport_file.write(airport_data_json)
        
def is_geojson(filename):
    return filename[-EXTENSION_LENGTH:] == GEOJSON_EXTENSION

def get_airport_code(filepath):
    return os.path.basename(filepath)

if __name__ == "__main__":
    combine_all_airports()
