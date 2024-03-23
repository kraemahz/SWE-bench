#!/usr/bin/env python3
import yaml
import sys


def conda_env_to_pip_requirements(env_file: str, requirements_file: str) -> None:
    """
    Convert a Conda environment.yml file to a pip requirements.txt file.
    """
    try:
        with open(env_file, 'r') as file:
            env = yaml.safe_load(file)
            dependencies = env.get('dependencies', [])
            pip_req = None
            for dep in dependencies:
                if isinstance(dep, dict):
                    pip_req = dep["pip"]
            if not pip_req:
                print(f"Error getting pip req {env_file}",
                      file=sys.stderr)
            with open(requirements_file, 'w') as req_file:
                for pkg in pip_req:
                    req_file.write(f"{pkg}\n")
        print(f"Requirements file '{requirements_file}' created successfully.")
    except Exception as e:
        print(f"Error converting {env_file} to {requirements_file}: {e}",
              file=sys.stderr)


conda_env_to_pip_requirements('environment.yml', 'requirements.txt')
