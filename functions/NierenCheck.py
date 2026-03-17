def calculate_gfr(krea, age, sex):
    """Calculate GFR using CKD-EPI formula.

    Args:
        krea (float): serum creatinine in mg/dL
        age (int): age in years
        sex (str): "Männlich" or "Weiblich"

    Returns:
        float: estimated GFR in ml/min/1.73m²
    """
    if sex == "Weiblich":
        kappa = 0.7
        alpha = -0.329
        gender_fix = 1.018
    else:
        kappa = 0.9
        alpha = -0.411
        gender_fix = 1.0

    gfr = 141 * min(krea / kappa, 1) ** alpha * max(krea / kappa, 1) ** -1.209 * 0.993 ** age * gender_fix
    return gfr