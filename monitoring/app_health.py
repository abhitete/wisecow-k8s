import requests
import datetime

# URL of the application (change if needed)
URL = "http://localhost:4499"

# Log file
log_file = "app_health.log"

def log_message(message):
    with open(log_file, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

def check_app_health():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            log_message(f"App is UP  - Status Code: {response.status_code}")
        else:
            log_message(f"App is DOWN  - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        log_message(f"App is DOWN  - Error: {e}")

if __name__ == "__main__":
    log_message("Running application health check...")
    check_app_health()
    log_message("Health check completed.\n")
