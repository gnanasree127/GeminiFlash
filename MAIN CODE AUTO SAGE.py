
# Vehicle Information Platform

# Dictionary with vehicle information
vehicles = {
    "Honda Activa": {"type": "two-wheeler", "fuel": "petrol", "emission": "non-eco"},
    "Toyota Innova": {"type": "four-wheeler", "fuel": "diesel", "emission": "non-eco"},
    "Tata Nexon EV": {"type": "four-wheeler", "fuel": "electric", "emission": "eco"},
}

def get_vehicle_info(vehicle_name):
    """Return vehicle information."""
    return vehicles.get(vehicle_name, "Vehicle not found.")

def get_maintenance_schedule(vehicle_type):
    """Return maintenance schedule."""
    if vehicle_type == "two-wheeler":
        return "Oil change every 2,000 km, tire pressure check every month."
    elif vehicle_type == "four-wheeler":
        return "Oil change every 5,000 km, tire pressure check every 2 months."

def get_eco_friendly_vehicles():
    """Return eco-friendly vehicle options."""
    eco_vehicles = [vehicle for vehicle, info in vehicles.items() if info["emission"] == "eco"]
    return eco_vehicles

def main():
    print("Vehicle Information Platform")
    while True:
        print("1. Get vehicle info")
        print("2. Get maintenance schedule")
        print("3. Get eco-friendly vehicles")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            vehicle_name = input("Enter vehicle name: ")
            print(get_vehicle_info(vehicle_name))
        elif choice == "2":
            vehicle_type = input("Enter vehicle type (two-wheeler/four-wheeler): ")
            print(get_maintenance_schedule(vehicle_type))
        elif choice == "3":
            print(get_eco_friendly_vehicles())
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

