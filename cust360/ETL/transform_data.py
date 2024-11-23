import pandas as pd
from logging_config.logging_config import logger


def transform_data(crm_data, sales_data, customer_service_data):
        logger.info("Transforming data...")
        try:
            # Check for required columns
            required_sales_cols = ['customer_id', 'amount', 'transaction_id']
            required_service_cols = ['customer_id', 'interaction_id']

            if not all(col in sales_data.columns for col in required_sales_cols):
              raise ValueError(f"Sales data is missing one of the required columns: {required_sales_cols}")

            if not all(col in customer_service_data.columns for col in required_service_cols):
                raise ValueError(f"Customer service data is missing one of the required columns: {required_service_cols}")

            # 1. Calculate Customer Lifetime Value (CLV)
            clv_data = sales_data.groupby('customer_id').agg(
            total_spent=('amount', 'sum'),
            total_transactions=('transaction_id', 'count')
            ).reset_index()

            # Assuming a simple CLV formula: CLV = Average Order Value * Purchase Frequency
            clv_data['average_order_value'] = clv_data['total_spent'] / clv_data['total_transactions'].replace(0, 1)  # Avoid division by zero
            clv_data['clv'] = clv_data['average_order_value'] * clv_data['total_transactions']  # This is a simplification

            # 2. Count the number of interactions per customer from Customer Service data
            interaction_count = customer_service_data.groupby('customer_id').agg(
            interaction_count=('interaction_id', 'count')
            ).reset_index()

            # 3. Merge CLV data with CRM data and interaction counts
            transformed_data = pd.merge(crm_data, clv_data, on='customer_id', how='left')
            transformed_data = pd.merge(transformed_data, interaction_count, on='customer_id', how='left')

            # Fill NaN values if needed
            transformed_data['clv'] = transformed_data['clv'].fillna(0)
            transformed_data['interaction_count'] = transformed_data['interaction_count'].fillna(0)

            # 4. Format date fields (assuming 'join_date' is in a valid date format)
            transformed_data['join_date'] = pd.to_datetime(transformed_data['join_date'], errors='coerce').dt.strftime('%Y-%m-%d')

            # 5. Select relevant columns for loading into the database
            final_data = transformed_data[['customer_id', 'first_name', 'last_name', 'email',
                                   'phone_number', 'city', 'state', 'country',
                                   'join_date', 'total_spent', 'clv', 'interaction_count']]

            return final_data
            logger.info("Data transformation completed.")
        except Exception as e:
            logger.error(f"Data transformation failed: {e}")

