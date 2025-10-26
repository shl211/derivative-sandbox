import numpy as np
import math

def annual_to_continuous_compounding(annual_rate: float, payout_frequency: int) -> float:
    """Converts an annual interest rate (R_m) paid out m times over the year 
    to a continuous interest rate (R_c) i.e.

    R_c = m ln(1 + R_m / m)

    Args:
        annual_rate (float): Annual interest rate
        payout_frequency (int): Interest rate payout frequency per year

    Returns:
        float: Continuous interest rate
    """
    return payout_frequency * math.log(1 + annual_rate / payout_frequency)

def continuous_to_annual_compounding(continuous_rate: float, payout_frequency: int) -> float:
    """Converts a continuous interest rate (R_c) to an annual interest rate (R_m)
    paid out m times over the year i.e.

    R_m = m(exp(R_c/m) - 1)

    Args:
        continuous_rate (float): Continuous interest rate
        payout_frequency (int): Interest rate payout frequency per year

    Returns:
        float: Annual compounding interest rate
    """
    return payout_frequency * (math.e ** (continuous_rate / payout_frequency) - 1)

if __name__ == "__main__":
    interest_rate = 0.1
    freq = 2
    continuous_rate = annual_to_continuous_compounding(interest_rate,freq)
    print("Testing annual to continuous interest rate conversion")
    print(f"Get {continuous_rate * 100:.3f}%, should be 9.758%")

    annual_rate = continuous_to_annual_compounding(continuous_rate,freq)
    print("Testing continuous to annual interest rate conversion")
    print(f"Get {annual_rate * 100:.0f}%, should be 10%")
