# Shortest Path Finder

## Overview
Shortest Path Finder is a web application developed to find the shortest path between two locations within a city in Algeria. It utilizes data from OpenStreetMap to create a road network graph, and then uses the A* algorithm to find the shortest path between the selected source and target locations.

## Features
- Select a city from a dropdown menu.
- Choose source and destination locations within the selected city.
- Click a button to find the shortest path between the selected locations.
- View the shortest path on an interactive map.

## Tools Used
- **Streamlit**: Used to create the web application interface for user interaction.
- **OSMnx**: Python library used to retrieve OpenStreetMap data and construct road network graphs.
- **NetworkX**: Python library used to perform graph-based operations, such as finding the shortest path.
- **Folium**: Python library used to visualize the road network graph and shortest path on an interactive map.

## Usage
1. Install the necessary dependencies by running:
    ```
    pip install -r requirements.txt
    ```
2. Run the Streamlit application by executing the following command in the terminal:
    ```
    streamlit run app.py
    ```
3. Select a city from the dropdown menu, choose source and destination locations, and click the "Find Shortest Path" button to view the shortest path on the map.

## Screenshots
![Screenshot 1](images/1.png)
![Screenshot 2](images/2.png)


## Contributing
Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.
