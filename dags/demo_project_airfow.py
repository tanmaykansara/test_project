from airflow.decorators import dag, task
from airflow.models import Variable
import logging
from airflow.utils.dates import days_ago
import importlib
from datetime import datetime
#normally this would be in includes as a generic func to implement 'requests' call
import requests
import json
from plugins.custom_operators.someOperator import someOperator

#from plugins.custom_operators.randomCustom include custom_op
dag_description = 'Sample Demo project to show how Airflow works'

dag_id = 'demo_project_airfow'
dag_display_name = 'Demo Dag for Public View'
dag_schedule_interval = '@daily'
dag_tags = ['poc', 'sample_project']
task1_name = 'Ingest Stock qotes'
owner_links = {'TanmayKansara': 'mailto:tanmay.kansara@gmail.com'}

task_execution_timeout = 3600
test_url = 'http://echo.jsontest.com/apple/aapl/google/goog'

logger = logging.getLogger(__name__)

#get the environment and select appropriate variables based on where the code is running...
try:
    environment_name = Variable.get("ENVIRON", default_var='dev')
    environment_name = environment_name.lower()
    logger.info(f"environment_name:{environment_name}")
    if environment_name == "prod":
       
        #secret_name = secret_prod_name
        #logger.setLevel(logging.ERROR)
        #prod environment parameters
        logger.info("In Prod")
    elif environment_name == "stage":
        logger.info("In Stage")
        #stage enviro  parameters
    elif environment_name == "dev":
        logger.info("In Dev")
        #Dev Environment
       
    else:
        raise ValueError(f"environment_name: {environment_name} not found when running Dag: {dag_id}")
except Exception as ex:
    #the environment variable will not exist on localhost so default to dev.
    #secret_name = secret_dev_name
    #dag_schedule_interval = None
    logger.info(ex)
    #do further error reporting either throug email/slack etc...

@dag(
    dag_id=dag_id,
    description=dag_description,
    dag_display_name=dag_display_name,
    schedule_interval=dag_schedule_interval,
    catchup=False,
    tags=dag_tags,
    owner_links=owner_links,    
    #concurrency=concurrency,
    max_active_runs=1,
    start_date=days_ago(1)
)

def demo_project_tasks():
    @task(task_display_name = task1_name)
    def ingest_data():
        logger.info("In Ingest Task")
        try:
            response = requests.get(test_url, timeout=30)
            response_text = response.text
            logger.info(type(response_text))
            #additional checks if response is not 200 and so on.... using response.status_code
            json_response = json.loads(response_text)
            return json_response
        except Exception as ex:
            logger.error("Error encountered in Ingest call")
            #further processing of error/reporting
    

    stock_symbol = ingest_data()
    get_quote = someOperator.partial(task_id="quote_data").expand(quote_objects=stock_symbol)
demo_project_tasks()