import os

# ANSI escape codes for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

project_slug = "{{ cookiecutter.project_slug }}"

print(f"{GREEN}SUCCESS!{ENDC}")
print(f"Project '{project_slug}' created successfully.")
print("
---")
print(f"{YELLOW}Next steps:{ENDC}")
print(f"1. cd {project_slug}")
print("2. (Optional) Create and populate your .env file for production secrets.")
print("3. docker-compose up -d --build")
print(f"4. Your API will be running at http://localhost:{{ cookiecutter.app_port }}")
print("---")
