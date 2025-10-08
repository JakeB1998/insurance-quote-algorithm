# Insurance Quote Calculator

This Python module provides a structured way to calculate insurance quotes based on multiple input factors including driver history, vehicle details, location risk, policy types, add-ons, and applicable discounts.

---

## Features

- **Input Classes:** Encapsulates driver, vehicle, location, policy, and discount inputs with clear data structures.
- **Policy Add-Ons:** Supports different insurance coverage types with weighted add-ons.
- **Discounts:** Calculates discounts from multiple discount types (e.g., safe driver, multi-policy).
- **Quote Calculation:** Combines policy weights, add-ons, and discounts to generate a final insurance quote adjustment factor.
- **Extensible:** Easy to add new discount types, policy types, and weighting logic.

---

## Classes and Key Components

- `DriverInputs` — Driver-related input factors (accident points, age, violations, etc.).
- `VehicleInputs` — Vehicle-related input factors (brand, repair complexity, safety features).
- `LocationInputs` — Location risk inputs (crime levels, anti-theft adjustments).
- `PolicyInputs` — Defines coverage type and selected add-ons.
- `DiscountsInputs` — Holds discount eligibility flags and provides active discount keys.
- `PolicyAddOnMap` — Maps policy types and add-ons to weight values.
- `DiscountKeys` & `AddOnKeys` — Enumerations for consistent key management.
- `calculate_quote_api(quote_input_ctx)` — Core function to calculate the quote based on all inputs.

---

## How to Use

1. **Create input instances:**

```python
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
```


2. **Calculate the Quote:**

```python
quote = calculate_quote_api(quote_inputs)
print(quote)
```

3. **JSON Return:**
```python
{
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
```