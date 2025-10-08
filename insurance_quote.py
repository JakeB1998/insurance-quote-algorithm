"""
Insurance Quote Calculation Module

This script calculates an insurance quote based on multiple risk factors
such as accident history, traffic violations, driver age, vehicle stats, 
location-based crime score, and available discounts.
"""

from typing import List
from default_checker import check_defaults
from logger import LOGGER
from inputs.quote_inputs import QuoteInputs
from weights.discount_weights import PolicyDiscountMap
from weights.policy_weights import PolicyAddOnMap

__LOGGER = LOGGER


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
    return 320


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


def calc_policy_adjustment(policy_type: str, add_ons: List[str]):
    adjustments = 0
    policy_obj = PolicyAddOnMap.POLICY_ADD_ON_MAP.get(policy_type, None)
    policy_weight = policy_obj["weight"]

    if policy_weight == -1:
        LOGGER.warning("Could not extract policy weight due to invalid key")
        return -1
    
    try:
        for add_on in add_ons:
            adjustments += policy_obj["add_ons"][add_on]

    except Exception as e:
        __LOGGER.error(f"Failed to calculate policy adjustment", e)

    return policy_weight + adjustments

def calc_discounts(policy_type: str, discounts: List[str]):
    """
    Calculates the total discount multiplier based on policy type and applicable discounts.

    Args:
        policy_type (str): The coverage type (e.g., liability, full_coverage).
        discounts (List[str]): List of discount keys.

    Returns:
        float: Total discount value (e.g., 0.2 for 20% discount).
    """
    discount_total = 0.0
    discount_obj = PolicyDiscountMap.POLICY_DISCOUNT_MAP.get(policy_type, None)

    if discount_obj is None:
        LOGGER.warning(f"Invalid policy type '{policy_type}' for discount calculation.")
        return 0.0

    try:
        for discount in discounts:
            discount_value = discount_obj.get(discount)
            if discount_value is not None:
                discount_total += discount_value
            else:
                LOGGER.warning(f"Discount key '{discount}' not found for policy type '{policy_type}'")

    except Exception as e:
        LOGGER.error(f"Failed to calculate discounts: {e}")

    return discount_total


def calculate_quote(quote_inputs_ctx: QuoteInputs):

    driver_inputs = quote_inputs_ctx.driver_inputs
    vehicle_inputs = quote_inputs_ctx.vehicle_inputs
    location_inputs = quote_inputs_ctx.location_inputs 
    policy_inputs = quote_inputs_ctx.policy_inputs
    discounts_inputs = quote_inputs_ctx.discount_inputs 

    check_defaults(driver_inputs, "driver_inputs", logger=__LOGGER)
    check_defaults(vehicle_inputs, "vehicle_inputs", logger=__LOGGER)
    check_defaults(location_inputs, "location_inputs", logger=__LOGGER)
    check_defaults(policy_inputs, "policy_inputs", logger=__LOGGER)


    
    bp = calc_base_rate()

    accident_points = calc_accident_points(
        at_fault_major=quote_inputs_ctx.driver_inputs.at_fault_major,
        at_fault_minor=quote_inputs_ctx.driver_inputs.at_fault_minor,
        no_fault=quote_inputs_ctx.driver_inputs.no_fault,
        hit_n_runs=quote_inputs_ctx.driver_inputs.hit_n_runs,
        duis=quote_inputs_ctx.driver_inputs.duis
    )

    violation_points = calc_violation_points(
        violations=quote_inputs_ctx.driver_inputs.violations
    )

    dr = calc_driver_risk(
        accident_points=accident_points,
        violation_points=violation_points,
        years_clean=quote_inputs_ctx.driver_inputs.years_clean,
        age=quote_inputs_ctx.driver_inputs.age
    )

    crime_score = calc_crime_score(
        crime_level_factor=quote_inputs_ctx.location_inputs.crime_level_factor,
        anti_theft_adjuestment=quote_inputs_ctx.location_inputs.anti_theft_adjustment
    )

    lr = calc_location_risk(
        accident_points=accident_points,
        crime_Score=crime_score
    )

    repair_score = calc_repair_score(
        brand_type_score=quote_inputs_ctx.vehicle_inputs.brand_type_score,
        repair_complex_score=quote_inputs_ctx.vehicle_inputs.repair_complexity_score,
        parts_score=quote_inputs_ctx.vehicle_inputs.parts_score,
        vehicle_age=quote_inputs_ctx.vehicle_inputs.vehicle_age
    )

    theft_score = calc_theft_score(
        vehicle_theft_rate_score=quote_inputs_ctx.vehicle_inputs.theft_score,
        location_risk_score=lr,
        anti_theft_feature_score=quote_inputs_ctx.vehicle_inputs.anti_theft_feature_score
    )

    safety_score = calc_saftey_score(
        crash_test_ratings=quote_inputs_ctx.vehicle_inputs.crash_test_rating,
        active_saftey_features=quote_inputs_ctx.vehicle_inputs.active_safety_features,
        passive_saftey_features=quote_inputs_ctx.vehicle_inputs.passive_safety_features
    )

    vr = calc_vehicle_risk(
        repair_score=repair_score,
        theft_score=theft_score,
        saftey_score=safety_score
    )

    policy_adjustment = calc_policy_adjustment(policy_type = policy_inputs.coverage_type, add_ons = policy_inputs.add_ons)

    dd = calc_discounts(policy_type = policy_inputs.coverage_type, discounts=discounts_inputs.discounts)

    __LOGGER.info(f"bp: {bp}, dr: {dr}, vr: {vr}, lr: {lr}, pa: {policy_adjustment}, dd: {dd}")

    quote = bp * dr * vr * lr * policy_adjustment
    discounted_total = quote * dd
    adjusted_quote = quote - discounted_total

    __LOGGER.info(f"Quote: {adjusted_quote}, Discounted: {discounted_total}")


    return {
        "base_rate": bp,
        "original_quote": quote,
        "total_discount": discounted_total,
        "quote": adjusted_quote,
        "weights": {
            "driver_risk": dr,
            "vehicle_risk": vr,
            "location_risk": lr,
            "policy_adjustment": policy_adjustment,
            "discount": dd
        },
        "scores": {
            "repair_score": repair_score,
            "theft_score": theft_score,
            "safety_score": safety_score,
            }
    }