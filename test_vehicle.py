from employee import vehicle_details

def test_vehical_details():
    expected_output = (
        "Vehical Number: KA25EP1498"
        "Owner Name: Yash"
        "Vehicle Type: bike"
        "Year of Manufacture: 2013"
    )

    assert vehicle_details("KA25EP1498", "Yash", "bike", 2013) == expected_output
