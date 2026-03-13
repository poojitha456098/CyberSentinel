import random
import datetime

roles = ["Developer","HR","Admin","Finance","Analyst"]
regions = ["Hyderabad","Bangalore","Mumbai","Delhi"]

def generate_log():

    abnormal = random.random() < 0.2

    user_id = f"EMP{random.randint(100,999)}"
    role = random.choice(roles)
    now = datetime.datetime.now()

    if not abnormal:

        log = {
            "user_id": user_id,
            "role": role,
            "login_time": now.strftime("%H:%M:%S"),
            "ip_region": random.choice(regions),
            "failed_attempts": random.randint(0,2),
            "files_accessed": random.randint(5,15),
            "session_duration": random.randint(180,300)
        }

    else:

        log = {
            "user_id": user_id,
            "role": role,
            "login_time": now.strftime("%H:%M:%S"),
            "ip_region": "Unknown Region",
            "failed_attempts": random.randint(5,10),
            "files_accessed": random.randint(200,400),
            "session_duration": random.randint(5,20)
        }

    return log