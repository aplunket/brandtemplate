import pkg_resources
import shutil
import os

def copy_files(file_paths, destination='/_extensions/brandtemplate'):
  """
  Copy files from the package to the specified destination directory.

  :param file_paths: List of file paths within the package.
  :param destination: Directory to copy files to (default is current directory).
  """
  package_name = __name__.split('.')[0]
  
  if not os.path.exists(destination):
    os.makedirs(destination)
    
  for file_path in file_paths:
    resource = pkg_resources.resource_filename(package_name, file_path)
    if os.path.isfile(resource):
        shutil.copy(resource, destination)
              

'''
p = importlib.resources.as_file(importlib.resources.files('resources') / 'resource.toml')
with p as f:
    my_toml = tomllib.load(f.open('rb'))    # as an example
'''