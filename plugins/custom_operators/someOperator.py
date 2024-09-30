from airflow.models import Variable
from airflow.models.baseoperator import BaseOperator
from datetime import datetime
import logging


logger = logging.getLogger(__name__)

class someOperator(BaseOperator):
    
    template_fields = ["quote_objects"]
    def __init__(self, quote_objects, **kwargs):
        super().__init__(**kwargs)
        self.quote_objects = quote_objects

    def execute(self, context):
        logger.info(f"context for custom operator: {context}")
        try:
            (company_name,stock_symbol) = self.quote_objects
            logger.info("In Custom Execute")
            quote = self.get_quotes(stock_symbol)
            logger.info(quote)
        except Exception as e:
            logger.info("Exception Occured handle it....")
        finally:
            logger.info("Absolute must things that must occur in case of exception....")

    def get_quotes(self, symbol):
        logger.info(f"Getting quote for {symbol}")
        quote = 10.01
        if symbol== 'aapl':
            quote = 150
        elif symbol=='goog':
            quote= 1000

        return quote
    