# Store the GPS coordinates of the warehouse as a tuple
warehouse_location = (12.9715987, 77.594566)  # Example coordinates for Bengaluru

# Function to retrieve the location data
def get_warehouse_location(location):
    return f"Warehouse Location: Latitude {location[0]}, Longitude {location[1]}"

# Example usage
print(get_warehouse_location(warehouse_location))
