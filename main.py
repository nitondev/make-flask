import os
import sys

def create_project(path):
    """Creates a project directory at the given path."""
    # Expand user (~) and normalize the path
    full_path = os.path.expanduser(path)

    # Extract the final folder name (project name)
    project_name = os.path.basename(full_path)

    # Determine the parent directory
    parent_dir = os.path.dirname(full_path) or os.getcwd()

    # Ensure the parent directory exists
    if not os.path.exists(parent_dir):
        print(f"Error: Parent directory does not exist: {parent_dir}")
        return False

    # Create the project directory
    project_path = os.path.join(parent_dir, project_name)
    if os.path.exists(project_path):
        print(f"Error: Project '{project_name}' already exists at: {project_path}")
        return False

    try:
        os.makedirs(project_path, exist_ok=True)
        print(f"Project '{project_name}' created at: {project_path}")
        return True
    except Exception as e:
        print(f"Error creating project: {e}")
        return False

def prompt_project_name():
    """Prompt the user for a valid project name or path."""
    while True:
        project_input = input("What is your project called? ").strip()
        if project_input:
            return project_input
        print("Error: No project name or path provided.")

def main():
    if len(sys.argv) == 2:
        project_input = sys.argv[1]
    else:
        project_input = prompt_project_name()

    while not create_project(project_input):
        project_input = prompt_project_name()

if __name__ == "__main__":
    main()
