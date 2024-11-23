from logging_config.logging_config import logger,log_audit

import sqlalchemy
DATABASE_URI = 'your URI here'

def load_data(transformed_data):
    logger.info("Loading transformed data...")
    # Load the transformed data into PostgreSQL
    engine = sqlalchemy.create_engine(DATABASE_URI)

    transformed_data.to_sql('transformed_customer_data', con=engine, if_exists='replace', index=False)
    logger.info("Data loading completed.")