from datetime import datetime, timedelta

# Function to get sunrise/sunset times from the Sunrise-Sunset API
def get_sunrise_sunset(lat, lng, date):
    url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={date}&formatted=0"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        sunrise = data['results']['sunrise']
        sunset = data['results']['sunset']
        return sunrise, sunset
    else:
        print("Error fetching sunrise/sunset data")
        return None

# Get sunrise and sunset for each day of the year
def get_sunrise_sunset_for_year(lat, lng):
    start_date = datetime(datetime.now().year, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(365)]  # All days of the year
    
    for date in dates:
        date_str = date.strftime('%Y-%m-%d')
        sunrise, sunset = get_sunrise_sunset(lat, lng, date_str)
        print(f"Date: {date_str}, Sunrise: {sunrise}, Sunset: {sunset}")

# Example usage
if coordinates:
    get_sunrise_sunset_for_year(lat, lng)

