location=[("New York", 40.7128, -74.0060),
              ("Los Angeles", 34.0522, -118.2437),
              ("Chicago", 41.8781, -87.6298),
              ("Houston", 29.7633, -95.3632),
              ("Philadelphia", 39.9523, -75.1633),]

def get_location(city):
    for for_name, word in location:
        if for_name == city:
            return word
        
        city = "New York"
        coordinates = get_location(city)
        
        if coordinates:
            print(f"The coordinates for {city} are {coordinates}")
        else:
            print(f"{city} not found")