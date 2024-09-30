#Sample Demo Project
This sample Demo shows how we can accomploish the task of ETL task of getting a list of symbols for which we would need to get the quotes. 

The project uses Pytest as a basic testing framework. A lot of testing in this environment is done at the CI/CD level. To test the test case included in the folder, one can execute 

##Executing the test case
> pytest symbol_quote.py

##Create the Docker Container
We need Docker to run the code. Once Docker is installed, and running the following command can be executed to create the Docker containers:
> docker build -t demo-project .

#Run the Docker Container
> docker compose up

Once the image is build and running, we can access the UI using the URL 
> http://127.0.0.1:8080/
![sample_demo drawio](https://github.com/user-attachments/assets/8d0173fb-66b9-45f5-aae9-15fadbb9ef76)

