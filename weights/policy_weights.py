class CoverageType:
    LIABILITY = "liability"
    FULL_COVERAGE = "full_coverage"
    COLLISION_ONLY = "collision_only"

class AddOnKeys:
    ROADSIDE_ASSISTANCE = "roadside_assistance"
    RENTAL_REIMBURSEMENT = "rental_reimbursement"
    GLASS_COVERAGE = "glass_coverage"
    GAP_COVERAGE = "gap_coverage"

class AddOnWeights:
    ROADSIDE_ASSISTANCE = 0.15
    RENTAL_REIMBURSEMENT = 0.1
    GLASS_COVERAGE = 0.05
    GAP_COVERAGE = 0.05

    


class PolicyAddOnMap:
    POLICY_ADD_ON_MAP = {
            CoverageType.LIABILITY: {
                "weight": 1.0,
                "add_ons": {
                    AddOnKeys.ROADSIDE_ASSISTANCE: AddOnWeights.ROADSIDE_ASSISTANCE,
                    AddOnKeys.RENTAL_REIMBURSEMENT: AddOnWeights.RENTAL_REIMBURSEMENT,
                    AddOnKeys.GLASS_COVERAGE: AddOnWeights.GLASS_COVERAGE
                }
            },
            CoverageType.FULL_COVERAGE: {
                "weight": 1.5,
                "add_ons": {
                    AddOnKeys.ROADSIDE_ASSISTANCE: AddOnWeights.ROADSIDE_ASSISTANCE,
                    AddOnKeys.RENTAL_REIMBURSEMENT: AddOnWeights.RENTAL_REIMBURSEMENT,
                    AddOnKeys.GAP_COVERAGE: AddOnWeights.GAP_COVERAGE,
                    AddOnKeys.GLASS_COVERAGE: AddOnWeights.GLASS_COVERAGE
                }
            },
            CoverageType.COLLISION_ONLY: {
                "weight": 1.2,
                "add_ons": {
                    AddOnKeys.RENTAL_REIMBURSEMENT: AddOnWeights.RENTAL_REIMBURSEMENT,
                    AddOnKeys.GLASS_COVERAGE: AddOnWeights.GLASS_COVERAGE
                }
            }
        }
