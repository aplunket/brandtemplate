import importlib.resources
import shutil
from pathlib import Path




def copy_template_files(file_names, destination_dir):
    """
    Copy a list of template files from the package to the specified directory.

    :param file_names: List of template file names to copy
    :param destination_dir: Directory to copy the files to
    """
    destination_path = Path(destination_dir)
    destination_path.mkdir(parents=True, exist_ok=True)

    # Get the package name dynamically
    package_name = __package__

    for file_name in file_names:
        with importlib.resources.path(f'{package_name}.template_files', file_name) as template_path:
            shutil.copy(template_path, destination_path / file_name)
