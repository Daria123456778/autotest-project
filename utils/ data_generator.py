# utils/data_generator.py

import random
import string

def generate_repo_name(prefix="testrepo"):
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{random_part}"