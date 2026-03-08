def grade_severity(percent):

    if percent <=10:
        severity="Healthy"
        disease="No disease detected"

    elif percent <=30:
        severity="Mild"
        disease="Possible nutrient deficiency"

    elif percent <=60:
        severity="Moderate"
        disease="Possible leaf spot disease"

    elif percent <=80:
        severity="Severe"
        disease="Possible fungal infection"

    else:
        severity="Dying"
        disease="Severe plant damage"

    return severity, disease