from typing import List

from weights.discount_weights import DiscountKeys





class QuoteInputs:
    def __init__(self):
        self.driver_inputs = DriverInputs()
        self.vehicle_inputs = VehicleInputs()
        self.location_inputs = LocationInputs()
        self.policy_inputs = PolicyInputs()
        self.discount_inputs = DiscountsInputs()

from typing import List

class DriverInputs:
    def __init__(self, at_fault_major: int = -1, at_fault_minor: int = -1, no_fault: int = -1,
                 hit_n_runs: int = -1, duis: int = -1, age: int = -1, years_clean: int = 1, violations: int = -1):
        self.at_fault_major = at_fault_major
        self.at_fault_minor = at_fault_minor
        self.no_fault = no_fault
        self.hit_n_runs = hit_n_runs
        self.duis = duis
        self.age = age
        self.years_clean = years_clean
        self.violations = violations


class VehicleInputs:
    def __init__(self, brand_type_score: int = -1, repair_complexity_score: int = -1, parts_score: int = -1, 
                 vehicle_age: int = -1, theft_score: int = -1, anti_theft_feature_score: int = -1, 
                 crash_test_rating: int = -1, active_safety_features: int = -1, passive_safety_features: int = -1):
        self.brand_type_score = brand_type_score
        self.repair_complexity_score = repair_complexity_score
        self.parts_score = parts_score
        self.vehicle_age = vehicle_age
        self.theft_score = theft_score
        self.anti_theft_feature_score = anti_theft_feature_score
        self.crash_test_rating = crash_test_rating
        self.active_safety_features = active_safety_features
        self.passive_safety_features = passive_safety_features


class LocationInputs:
    def __init__(self, crime_level_factor: int = -1, anti_theft_adjustment: int = -1):
        self.crime_level_factor = crime_level_factor
        self.anti_theft_adjustment = anti_theft_adjustment


class PolicyInputs:
    def __init__(self, coverage_type: str = None, add_ons: List[str] = None):
        self.coverage_type = coverage_type
        self.add_ons = add_ons

class DiscountsInputs:

    @staticmethod
    def get_discounts(multi_policy: bool = False,
                 safe_driver: bool = False,
                 low_mileage: bool = False,
                 anti_theft: bool = False):
        """
        Returns a list of discount keys based on boolean input flags.

        Args:
            multi_policy (bool): Eligible for multi-policy discount.
            safe_driver (bool): Eligible for safe driver discount.
            low_mileage (bool): Eligible for low mileage discount.
            anti_theft (bool): Eligible for anti-theft discount.

        Returns:
            list: A list of applicable discount keys.
        """
        discounts = []

        if multi_policy:
            discounts.append(DiscountKeys.MULTI_POLICY)
        if safe_driver:
            discounts.append(DiscountKeys.SAFE_DRIVER)
        if low_mileage:
            discounts.append(DiscountKeys.LOW_MILEAGE)
        if anti_theft:
            discounts.append(DiscountKeys.ANTI_THEFT)

        return discounts
    
    def __init__(self, discounts: List[str] = None):
        self.discounts = discounts





