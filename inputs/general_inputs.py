# Currently Not USed

class Inputs:
    def __init__(self):
        self.driver_inputs = DriverInputs()
        self.vehicle_inputs = VehicleInputs()
        self.location_inputs = LocationInputs()
        self.polict_inputs = PolicyInputs()

class DriverInputs:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.license_number = ""
        self.driving_history = []  # List of incidents or violations


class VehicleInputs:
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = 0
        self.vin = ""
        self.usage_type = ""  # e.g., personal, commercial


class LocationInputs:
    def __init__(self):
        self.zip_code = ""
        self.state = ""
        self.city = ""
        self.address = ""


class PolicyInputs:
    def __init__(self):
        self.coverage_type = ""  # e.g., liability, full coverage
        self.deductible = 0
        self.policy_start_date = ""
        self.policy_end_date = ""


