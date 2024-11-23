import logging
import os

# Create a directory for logs if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG for verbose output, can be INFO or WARNING for less
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/data_pipeline.log'),  # Log to a file
        logging.StreamHandler()  # Also log to console
    ]
)

# Create a logger object
logger = logging.getLogger()

def log_audit(action, details):
    """Log an audit trail for data operations."""
    logger.info(f"Audit Log - Action: {action}, Details: {details}")

def log_data_quality_issue(issue):
    """Log data quality issues."""
    logger.warning(f"Data Quality Issue: {issue}")

def log_error(error_message):
    """Log error messages."""
    logger.error(f"Error occurred: {error_message}")

def log_info(info_message):
    """Log general information messages."""
    logger.info(info_message)
