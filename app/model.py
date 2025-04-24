
import random

def get_current_status():
    heart_rate = random.randint(55, 110)
    acc_std = round(random.uniform(0.005, 0.08), 4)

    if acc_std < 0.01 and heart_rate < 60:
        status = "rest"
        suggestion = "保持休息状态，良好"
    elif acc_std < 0.05 and heart_rate < 90:
        status = "light"
        suggestion = "轻度活动中，请保持节奏"
    else:
        status = "intense"
        suggestion = "中高强度运动，注意补水"

    return {
        "status": status,
        "heart_rate": heart_rate,
        "suggestion": suggestion
    }
