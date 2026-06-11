def check_alert(status):

    if status == "Poor":
        return "Warning: Air Quality Poor"

    elif status == "Hazardous":
        return "ALERT: Hazardous Pollution Level"

    else:
        return "No Alert"