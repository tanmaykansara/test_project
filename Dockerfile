FROM apache/airflow:2.9.3-python3.11
COPY requirements.txt /
COPY dags/ ${AIRFLOW_HOME}/dags
COPY logs/ ${AIRFLOW_HOME}/logs
COPY includes/ ${AIRFLOW_HOME}/includes
COPY scripts/ ${AIRFLOW_HOME}/scripts
COPY dag_configs/ ${AIRFLOW_HOME}/dag_configs
COPY templates/ ${AIRFLOW_HOME}/templates
COPY plugins/ ${AIRFLOW_HOME}/plugins
COPY tests/ ${AIRFLOW_HOME}/tests
ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}/logs"
ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}/includes"
ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}/scripts"
ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}/dag_configs"
ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}/templates"
ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}/plugins"
ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}/tests"
RUN pip install  --force-reinstall --no-cache-dir -r /requirements.txt --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.3/constraints-3.11.txt"
# install dbt into a virtual environment
#RUN cd /opt/airflow/
#ENV PIP_USER=false
#RUN python -m venv dbt_environment
#RUN /opt/airflow/dbt_environment/bin/pip install dbt-snowflake==1.8.3
