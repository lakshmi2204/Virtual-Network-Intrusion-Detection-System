import logging
from log_insert import insert_log

# Configure logging
logging.basicConfig(
    filename="attack.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create logger object
logger = logging.getLogger()


# Function to log attack events
def log_attack(ip, attack_type, severity):

    message = f"IP: {ip} | Attack: {attack_type} | Severity: {severity}"

    # Save to attack.log
    logger.info(message)

    # Save to database
    insert_log(ip, attack_type, severity)

    print("✔ Log recorded:", message)
    