# Import necessary libraries:
# - Jinja2 for template management
# - os for file and directory operations
# - yaml for reading yaml files
# - json for JSON operations (not used in the current version of your code)
from jinja2 import Environment, FileSystemLoader
import os
import yaml

# Obtain the directory of the current python script. This is used later to form paths to other directories.
file_dir = os.path.dirname(os.path.abspath(__file__))

# Join the current directory's parent ('..') with the 'configs' subdirectory to form the path to the configs directory
configs_dir = os.path.abspath(os.path.join(file_dir, '..', 'dag_configs'))
dags_dir = os.path.abspath(os.path.join(file_dir, '..', 'dags'))
templates_dir = os.path.abspath(os.path.join(file_dir, '..', 'templates'))

# Instantiate a Jinja Environment object with the FileSystemLoader configured to the '../templates' directory
# This tells Jinja where to look for template files
env = Environment(loader=FileSystemLoader(templates_dir))

# Iterate over every file in the configs directory
for filename in os.listdir(configs_dir):
    # If the file has a .yaml extension...
    if filename.endswith(".yaml"):
        # Open the yaml file
        with open(f"{configs_dir}/{filename}", "r") as configfile:
            # Parse the yaml file into a Python dictionary using yaml.safe_load
            config = yaml.safe_load(configfile)
            
            # Extract the dag_id and template name from the config dictionary
            dag_id = config['dag_id']
            template_name = config['dag_template']

            # Use the Jinja Environment to load the appropriate template
            template = env.get_template(f'{template_name}.j2')

            # Open a new .py file in the 'dags' directory, named with the dag_id
            with open(os.path.join(dags_dir, f'{dag_id}.py'), 'w') as f:
                # Render the template with the config dictionary as context (filling in the variables in the template),
                # and write the rendered template to the new .py file
                f.write(template.render(config))
