def genrate_report(data):
    if data['average'] > 90:
        return "Excellent"
    elif data['average'] > 70:
        return "Very Good"
    else:
        return "Good"