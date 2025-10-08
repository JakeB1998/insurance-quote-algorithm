
from weights.policy_weights import CoverageType


class DiscountKeys:
    MULTI_POLICY = "multi_policy"
    SAFE_DRIVER = "safe_driver"
    LOW_MILEAGE = "low_mileage"
    ANTI_THEFT = "anti_theft"


class DiscountWeights:
    MULTI_POLICY = 0.1        # 10% discount
    SAFE_DRIVER = 0.12        # 15% discount
    LOW_MILEAGE = 0.05        # 5% discount
    ANTI_THEFT = 0.03         # 7% discount


class PolicyDiscountMap:
    POLICY_DISCOUNT_MAP = {
        CoverageType.LIABILITY: {
            DiscountKeys.MULTI_POLICY: DiscountWeights.MULTI_POLICY,
            DiscountKeys.LOW_MILEAGE: DiscountWeights.LOW_MILEAGE,
        },
        CoverageType.FULL_COVERAGE: {
            DiscountKeys.MULTI_POLICY: DiscountWeights.MULTI_POLICY,
            DiscountKeys.SAFE_DRIVER: DiscountWeights.SAFE_DRIVER,
            DiscountKeys.ANTI_THEFT: DiscountWeights.ANTI_THEFT,
        },
        CoverageType.COLLISION_ONLY: {
            DiscountKeys.SAFE_DRIVER: DiscountWeights.SAFE_DRIVER,
            DiscountKeys.LOW_MILEAGE: DiscountWeights.LOW_MILEAGE,
        }
    }
