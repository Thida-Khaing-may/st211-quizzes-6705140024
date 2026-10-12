import pytest
from rental import Vehicle, Renter, ElectricCar, Motorbike


# =====================================================================
# Vehicle & Renter
# =====================================================================

def test_vehicle_start_available_rent_and_return():
    """A new vehicle starts available; rent() makes it rented; return_vehicle() makes it available again."""
    v = Vehicle("Toyota", "Yaris", "1AB234")

    assert v.is_rented is False

    v.rent()
    assert v.is_rented is True

    v.return_vehicle()
    assert v.is_rented is False


def test_vehicle_str_status_changes():
    """__str__ shows the status, and the line changes after the vehicle is rented."""
    v = Vehicle("Toyota", "Yaris", "1AB234")

    initial_str = str(v)
    assert "available" in initial_str.lower()

    v.rent()

    rented_str = str(v)
    assert "rented" in rented_str.lower()
    assert initial_str != rented_str


def test_renter_rented_list_starts_empty():
    """A new renter's rented list starts empty."""
    r = Renter("Alice", 10452)

    assert isinstance(r.rented, list)
    assert len(r.rented) == 0


# =====================================================================
# Encapsulation
# =====================================================================

def test_renter_empty_name_raises_value_error():
    """Creating a renter with an empty name raises ValueError."""
    with pytest.raises(ValueError):
        Renter("", 10452)

    with pytest.raises(ValueError):
        Renter("   ", 10452)


def test_renter_zero_or_negative_license_raises_value_error():
    """Creating a renter with a zero or negative licence raises ValueError."""
    with pytest.raises(ValueError):
        Renter("Bob", 0)

    with pytest.raises(ValueError):
        Renter("Charlie", -15)


def test_renter_validation_fires_on_attribute_change():
    """The same check also fires if the value is changed later."""
    r = Renter("David", 5555)

    with pytest.raises(ValueError):
        r.name = ""

    with pytest.raises(ValueError):
        r.name = "   "

    with pytest.raises(ValueError):
        r.license_no = 0

    with pytest.raises(ValueError):
        r.license_no = -99


# =====================================================================
# Inheritance & Polymorphism
# =====================================================================

def test_subclasses_are_instance_of_vehicle():
    """ElectricCar and Motorbike are treated as a Vehicle."""
    ev = ElectricCar("Tesla", "Model 3", "EV789", 75)
    mb = Motorbike("Honda", "Click", "BK123", 125)

    assert isinstance(ev, Vehicle)
    assert isinstance(mb, Vehicle)


def test_subclasses_have_parent_data_and_can_rent_return():
    """They still have the parent's data and can rent() / return_vehicle()."""
    ev = ElectricCar("Tesla", "Model 3", "EV789", 75)
    mb = Motorbike("Honda", "Click", "BK123", 125)

    # Parent data preserved
    assert ev.make == "Tesla"
    assert ev.model == "Model 3"
    assert ev.plate == "EV789"
    assert ev.is_rented is False

    assert mb.make == "Honda"
    assert mb.model == "Click"
    assert mb.plate == "BK123"
    assert mb.is_rented is False

    # Subclass-specific data
    output_ev = str(ev)
    assert "75" in output_ev
    assert "kWh" in output_ev

    output_mb = str(mb)
    assert "125" in output_mb
    assert "cc" in output_mb

    # rent() and return_vehicle() inherited functionality
    ev.rent()
    mb.rent()

    assert ev.is_rented is True
    assert mb.is_rented is True

    ev.return_vehicle()
    mb.return_vehicle()

    assert ev.is_rented is False
    assert mb.is_rented is False


def test_polymorphic_str_three_different_lines():
    """Each type's __str__ is different."""
    fleet = [
        Vehicle("Toyota", "Yaris", "1AB234"),
        ElectricCar("Tesla", "Model 3", "EV789", 75),
        Motorbike("Honda", "Click", "BK123", 125),
    ]

    outputs = [str(item) for item in fleet]

    # Ensure all three output strings are distinct
    assert len(set(outputs)) == 3