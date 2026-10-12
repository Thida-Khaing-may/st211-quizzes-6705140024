from rental import Vehicle, Renter, ElectricCar, Motorbike


def main():
    print("=== Vehicle Rental Demonstration ===")

    # Create vehicles and a renter
    vehicle = Vehicle("Toyota", "Yaris", "1AB234")
    electric_car = ElectricCar("Tesla", "Model 3", "EV123", 75)
    motorbike = Motorbike("Honda", "CBR500R", "MB500", 500)

    renter = Renter("Thida", 12345)

    print("\n--- Renter ---")
    print("Name:", renter.name)
    print("License:", renter.license_no)
    print("Rented vehicles:", renter.rented)

    # Rent and return a vehicle
    print("\n--- Rent and Return ---")
    print(vehicle)

    vehicle.rent()
    print("After renting:")
    print(vehicle)

    vehicle.return_vehicle()
    print("After returning:")
    print(vehicle)

    # Show ValueError for a bad name
    print("\n--- Invalid Renter Tests ---")
    try:
        Renter("", 12345)
    except ValueError as e:
        print("Caught ValueError:", e)

    # Show ValueError for a bad license
    try:
        Renter("Test User", -10)
    except ValueError as e:
        print("Caught ValueError:", e)

    # Show that validation also happens when values are changed
    try:
        renter.name = ""
    except ValueError as e:
        print("Caught ValueError when changing name:", e)

    try:
        renter.license_no = 0
    except ValueError as e:
        print("Caught ValueError when changing license:", e)

    # Polymorphism: different Vehicle types in one list
    print("\n--- Polymorphism ---")
    vehicles = [vehicle, electric_car, motorbike]

    for v in vehicles:
        print(v)


if __name__ == "__main__":
    main()
