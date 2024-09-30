from airflow.models import Variable
from airflow.models.baseoperator import BaseOperator
from datetime import datetime
import logging


logger = logging.getLogger(__name__)

class someOperator(BaseOperator):
    

    def __init__(self, aws_region: str, media_objects: list, **kwargs):
        super().__init__(**kwargs)
        

    def execute(self, context):
        logger.info(f"context for custom operator: {context}")
        try:
            
            logger.info("In Custom Execute")
            
        except Exception as e:
            logger.info("Exception Occured handle it....")
        finally:
            logger.info("Absolute must things that must occur in case of exception....")

    def get_quotes(self, symbol):
        logger.info(f"Getting quote for {symbol}")
        quote = 10.01


        return quote
    