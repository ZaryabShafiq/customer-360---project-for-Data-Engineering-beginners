import pandas as pd
from logging_config.logging_config import logger

def extract_data():
    logger.info("Extracting data...")
    try:
        # Extract data from CSV files (replace with your actual file paths)
        crm_data = pd.read_csv(r'your path here')
        sales_data = pd.read_csv(r'your path here')
        customer_service_data = pd.read_csv(r'your path here')

        # Clean column names by stripping whitespace
        crm_data.columns = crm_data.columns.str.strip()
        sales_data.columns = sales_data.columns.str.strip()
        customer_service_data.columns = customer_service_data.columns.str.strip()

        return crm_data, sales_data, customer_service_data
    except Exception as e:
        logger.error(f"Failed to extract CRM data: {e}")
