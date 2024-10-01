# Sample Demo Project
This sample Demo shows how we can accomploish the task of ETL task of getting a list of symbols for which we would need to get the quotes. 

The project uses Pytest as a basic testing framework. A lot of testing in this environment is done at the CI/CD level. To test the test case included in the folder, one can execute 

## Executing the test case
> pytest symbol_quote.py

## Create the Docker Container
We need Docker to run the code. Once Docker is installed, and running the following command can be executed to create the Docker containers:
> docker build -t demo-project .

# Run the Docker Container
> docker compose up

Once the image is build and running, we can access the UI using the URL 
> http://127.0.0.1:8080/

We are using Yaml config files and Jinja template to dynamically create tasks at runtime. The current config file has a hardcoded URL for 2 stock quotes, if we need to have an additional Dag to pull 2 other stock quotes, we can create the config file and execute the following render command to create the Python Dag file:
> python scripts\render_dags.py

Once the dag is created, the UI will pick up the new code. Upon executing the job we will see that the dag creates 2 dynamic tasks for each of the stock quote for Hardcoded URL in the config file.

![image](https://github.com/user-attachments/assets/b5d39373-f85c-4cd2-852b-87b9b187d988)

The above snippet shows that 1 Ingest task is created and 2 Get data tasks are dynamically created based on the ingest URL. If the ingest URL returned more records, the number of tasks would increase proportionately. 

Below is a sample high level schema on how the data could be stored. 
![sample_demo drawio](https://github.com/user-attachments/assets/8d0173fb-66b9-45f5-aae9-15fadbb9ef76)

