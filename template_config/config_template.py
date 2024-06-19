import yaml

def config_template():
    config = load_yaml('template_config/config.yaml')
    return config


# Function to load YAML file
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
