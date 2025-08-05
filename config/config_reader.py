import yaml
import os

def load_config(filename):
    config_path = os.path.join(os.path.dirname(__file__), filename)
    with open(config_path, encoding='utf-8') as f:
        return yaml.safe_load(f)