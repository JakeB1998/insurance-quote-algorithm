from default_checker import check_defaults
from inputs.quote_inputs import DiscountsInputs, DriverInputs, LocationInputs, PolicyInputs, QuoteInputs, VehicleInputs
from insurance_quote import calc_base_rate, calc_accident_points, calc_crime_score, calc_discounts, calc_driver_risk, calc_location_risk, calc_policy_adjustment, calc_repair_score, calc_saftey_score, calc_theft_score, calc_vehicle_risk, calc_violation_points, calculate_quote
from logger import LOGGER
from weights.policy_weights import AddOnKeys, CoverageType


__LOGGER = LOGGER


def run_test_quote():
    # Create inputs
    driver_inputs = DriverInputs(
        at_fault_major=1,
        at_fault_minor=1,
        no_fault=2,
        hit_n_runs=0,
        duis=0,
        age=23,
        years_clean=5,
        violations=1
    )

    location_inputs = LocationInputs(
        crime_level_factor=4,
        anti_theft_adjustment=2
    )

    vehicle_inputs = VehicleInputs(
        brand_type_score=3,
        repair_complexity_score=2,
        parts_score=4,
        vehicle_age=15,
        theft_score=5,
        anti_theft_feature_score=2,
        crash_test_rating=4,
        active_safety_features=2,
        passive_safety_features=3
    )

    policy_inputs = PolicyInputs(
        coverage_type=CoverageType.FULL_COVERAGE,
        add_ons=[AddOnKeys.ROADSIDE_ASSISTANCE, AddOnKeys.RENTAL_REIMBURSEMENT]
    )

    discounts_inputs = DiscountsInputs(discounts=DiscountsInputs.get_discounts(multi_policy=True,
        safe_driver=True,
        low_mileage=False,
        anti_theft=True)

    )


    # Load into QuoteInputs
    quote_inputs = QuoteInputs()
    quote_inputs.driver_inputs = driver_inputs
    quote_inputs.vehicle_inputs = vehicle_inputs
    quote_inputs.location_inputs = location_inputs
    quote_inputs.policy_inputs = policy_inputs
    quote_inputs.discount_inputs = discounts_inputs

    __LOGGER.info(calculate_quote(quote_inputs))




if __name__ == "__main__":
    __LOGGER.info("This is an insurance quote algorithm")
    run_test_quote()