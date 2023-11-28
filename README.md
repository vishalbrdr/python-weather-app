

# 🌞 Weather App

A simple weather application built using Python and customtkinter GUI to display weather information based on the user's location or input query.

## Features

- Fetches the user's location by their IP address upon initial load.
- Retrieves weather data for the user's location.
- Displays current weather conditions, temperature, feels-like temperature, wind speed, pressure, precipitation, humidity, UV index, visibility, and more.
- Allows searching by city name or airport code.
- Graphical user interface (GUI) built with Python's customtkinter library.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/vishalbrdr/python-weather-app.git
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Upon initial load, it automatically fetches the user's location using their IP address and retrieves weather data for that location. Alternatively, enter the city name or airport code in the search field.
3. Click the "Search" button to fetch and display specific weather data.

## Screenshots
### Initial Load
![screenshot-1](/images/screenshots/initial_load.jpg)

### Search By City Name
![screenshot-1](/images/screenshots/city_name.jpg)

### Search By Airport Code
![screenshot-1](/images/screenshots/airport_code.jpg)

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.

## Credits

- **Author:** Vishal Biradar
- **API:** [Weather API](https://www.weatherapi.com/) and [IP Geolocation API](https://geo.ipify.org/)


## License

This project is licensed under the [MIT License](LICENSE).
