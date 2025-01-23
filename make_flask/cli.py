import os
import shutil
import sys
import tarfile
import urllib.request


def setup_structure(project_path):
    """Downloads a tar.gz file, extracts it, and moves files to the project root."""
    url = "https://niton.dev/flask-source.tar.gz"
    archive_path = os.path.join(project_path, "flask-source.tar.gz")

    # Download the tar.gz file
    print("[ + ] Downloading source files ...")
    try:
        urllib.request.urlretrieve(url, archive_path)
    except Exception as e:
        print(f"Error downloading the source archive: {e}")
        return False

    # Unpack the tar.gz archive
    print("[ + ] Unpacking the archive ...")
    try:
        with tarfile.open(archive_path, "r:gz") as archive:
            archive.extractall(project_path)
    except Exception as e:
        print(f"Error unpacking the archive: {e}")
        return False

    # Move files to the root project directory
    extracted_folder = os.path.join(project_path, "flask-source")
    if os.path.exists(extracted_folder):
        for item in os.listdir(extracted_folder):
            item_path = os.path.join(extracted_folder, item)
            target_path = os.path.join(project_path, item)
            try:
                if os.path.isdir(item_path):
                    shutil.move(item_path, target_path)
                else:
                    shutil.move(item_path, target_path)
            except Exception as e:
                print(f"Error moving file/folder {item}: {e}")
                return False

        # Remove the extracted folder after moving contents
        try:
            shutil.rmtree(extracted_folder)
        except Exception as e:
            print(f"Error removing extracted folder: {e}")
            return False
    else:
        print(f"Error: Extracted folder '{extracted_folder}' does not exist.")
        return False

    # Remove the tar.gz file after extraction
    os.remove(archive_path)

    return True


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
        print(f"Error: Project '{project_name}' already exists.")
        return False

    try:
        os.makedirs(project_path, exist_ok=True)
        print(f"Project '{project_name}' created at: {project_path}")

        # Download and extract source files after project creation
        if not setup_structure(project_path):
            print(f"Failed to download or unpack source files for '{project_name}'.")
            return False

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
