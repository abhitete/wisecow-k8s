import psutil
import datetime

# Define thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

# Create/open log file
log_file = "system_health.log"

def log_message(message):
    with open(log_file, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

def check_system_health():
    # CPU usage
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        log_message(f"⚠️ High CPU usage detected: {cpu}%")

    # Memory usage
    memory = psutil.virtual_memory().percent
    if memory > MEM_THRESHOLD:
        log_message(f"⚠️ High Memory usage detected: {memory}%")

    # Disk usage
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        log_message(f"⚠️ High Disk usage detected: {disk}%")

    # Running processes (top 5 by memory)
    processes = [(p.info['pid'], p.info['name'], p.info['memory_percent'])
                 for p in psutil.process_iter(['pid', 'name', 'memory_percent'])]
    processes = sorted(processes, key=lambda x: x[2], reverse=True)[:5]

    log_message("Top 5 memory-consuming processes:")
    for pid, name, mem in processes:
        log_message(f"PID={pid}, Name={name}, Memory={mem:.2f}%")

if __name__ == "__main__":
    log_message("🔍 Running system health check...")
    check_system_health()
    log_message("✅ Health check completed.\n")
