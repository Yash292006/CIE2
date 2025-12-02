# employee.py
def vehicle_details(no, name, type, year):
    result = (
        f"Vehical Number: {no}\n"
        f"Owner Name: {name}\n"
        f"Vehicle Type: {type}\n"
        f"Year of Manufacture: {year}"
    )
    return result


if __name__ == "__main__":
    # Sample input
    no = "KA251498"
    name = "Yash"
    type = "bike"
    year = "2013"

    print(vehicle_details(no, name, type, year))
