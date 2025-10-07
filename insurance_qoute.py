"""
Insurance Quote Calculation Module

This script calculates an insurance quote based on multiple risk factors
such as accident history, traffic violations, driver age, vehicle stats, 
location-based crime score, and available discounts.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

__LOGGER = logging.getLogger(__name__)


def calc_violation_points(violations):
    """
    Calculate points from traffic violations.

    Args:
        violations (int): Number of traffic violations.

    Returns:
        float: Violation points.
    """
    return violations * 0.01 + 0.005


def calc_theft_score(vehicle_theft_rate_score, location_risk_score, anti_theft_feature_score):
    """
    Calculate theft score for the vehicle.

    Args:
        vehicle_theft_rate_score (int): Theft rate based on model/popularity.
        location_risk_score (float): Risk from location crime level.
        anti_theft_feature_score (int): Effectiveness of anti-theft features.

    Returns:
        float: Theft risk score.
    """
    return vehicle_theft_rate_score + location_risk_score - anti_theft_feature_score


def calc_repair_score(brand_type_score, repair_complex_score, parts_score, vehicle_age):
    """
    Calculate repair cost/complexity score.

    Args:
        brand_type_score (int): Score based on brand's repairability.
        repair_complex_score (int): How complex the repairs are.
        parts_score (int): Score for parts availability/cost.
        vehicle_age (int): Age of the vehicle in years.

    Returns:
        float: Repair score (lower is better).
    """
    return brand_type_score + repair_complex_score + parts_score + (vehicle_age / 2)


def calc_saftey_score(crash_test_ratings, active_saftey_features, passive_saftey_features):
    """
    Calculate safety score of the vehicle.

    Args:
        crash_test_ratings (int): Crash safety rating (e.g. out of 5).
        active_saftey_features (int): Number of active safety features.
        passive_saftey_features (int): Number of passive safety features.

    Returns:
        float: Safety score (higher is better).
    """
    return crash_test_ratings + active_saftey_features * 2 + passive_saftey_features


def calc_accident_points(at_fault_major, at_fault_minor, no_fault, hit_n_runs, duis):
    """
    Calculate accident points based on driving history.

    Args:
        at_fault_major (int): Major at-fault accidents.
        at_fault_minor (int): Minor at-fault accidents.
        no_fault (int): No-fault accidents.
        hit_n_runs (int): Hit-and-run incidents.
        duis (int): Driving Under Influence incidents.

    Returns:
        float: Total accident points.
    """
    return (at_fault_major * 3) + (at_fault_minor * 1.5) + (no_fault * 0.5) + (hit_n_runs * 4) + (duis * 5)


def calc_crime_score(crime_level_factor, anti_theft_adjuestment):
    """
    Calculate the crime score of the location.

    Args:
        crime_level_factor (int): Crime severity in area.
        anti_theft_adjuestment (int): Mitigation score from anti-theft.

    Returns:
        float: Crime score (higher is riskier).
    """
    return crime_level_factor - anti_theft_adjuestment


def calc_base_rate():
    """
    Get the base rate of insurance.

    Returns:
        float: Base insurance rate.
    """
    return 500


def calc_driver_risk(accident_points, violation_points, years_clean, age):
    """
    Calculate the driver's risk multiplier.

    Args:
        accident_points (float): Points from accidents.
        violation_points (float): Points from violations.
        years_clean (int): Years of clean driving.
        age (int): Driver's age.

    Returns:
        float: Driver risk factor.
    """
    if age < 25:
        age_adjustment = 0.15
    elif age < 65:
        age_adjustment = 0.0
    else:
        age_adjustment = 0.10

    years_clean_points = -(years_clean * 0.01)
    return 1 + (0.02 * accident_points) + (0.015 * violation_points) - (0.01 * years_clean_points) + age_adjustment


def calc_vehicle_risk(repair_score, theft_score, saftey_score):
    """
    Calculate vehicle risk multiplier.

    Args:
        repair_score (float): Cost/complexity of repair.
        theft_score (float): Risk of vehicle theft.
        saftey_score (float): Safety rating of the vehicle.

    Returns:
        float: Vehicle risk factor.
    """
    return 1 + (repair_score + theft_score - saftey_score) / 100


def calc_location_risk(accident_points, crime_Score):
    """
    Calculate location-based risk.

    Args:
        accident_points (float): Points from accident history.
        crime_Score (float): Crime score of the location.

    Returns:
        float: Location risk multiplier.
    """
    return 1 + (0.02 * accident_points) + (0.025 * crime_Score)


def calc_discounts():
    """
    Placeholder function for calculating available discounts.

    Returns:
        float: Discount multiplier.
    """
    return 1


# Run quote calculation if this module is the main script
if __name__ == "__main__":
    __LOGGER.info("This is an insurance quote algorithm")

    # Input data (example values)
    accident_points = calc_accident_points(
        at_fault_major=1,
        at_fault_minor=1,
        no_fault=2,
        hit_n_runs=0,
        duis=0
    )

    bp = calc_base_rate()
    dr = calc_driver_risk(
        accident_points=accident_points,
        violation_points=calc_violation_points(violations=1),
        years_clean=5,
        age=23
    )

    lr = calc_location_risk(
        accident_points=accident_points,
        crime_Score=calc_crime_score(
            crime_level_factor=4,
            anti_theft_adjuestment=2
        )
    )

    vr = calc_vehicle_risk(
        repair_score=calc_repair_score(
            brand_type_score=3,
            repair_complex_score=2,
            parts_score=4,
            vehicle_age=15
        ),
        theft_score=calc_theft_score(
            vehicle_theft_rate_score=5,
            location_risk_score=lr,
            anti_theft_feature_score=2
        ),
        saftey_score=calc_saftey_score(
            crash_test_ratings=4,
            active_saftey_features=2,
            passive_saftey_features=3
        )
    )

    dd = calc_discounts()

    __LOGGER.info(f"bp: {bp}, dr: {dr}, vr: {vr}, lr: {lr}, dd: {dd}")

    qoute = bp * dr * vr * lr * dd

    __LOGGER.info(f"Qoute: {qoute}")
