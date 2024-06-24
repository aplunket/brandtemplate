import yaml
import jsondiff
from pathlib import Path

def config_template():
  '''
  Config the template based on the values in template_config/config.yaml
  '''
  config = load_yaml('template_config/config.yaml')
  config_prev = load_yaml('template_config/previous_config.yaml')
  config_diff = jsondiff.diff(config_prev, config)

  current_name=config_prev['package_name']
  new_name=config['package_name']

  #---------------------------------------------------------------------------------
  # Overall
  #---------------------------------------------------------------------------------

  if 'package_name' in config_diff:
    #rename overall folder
    rename_folder(current_name, new_name)
    #update name in pyproject.toml
    replace_line_containing_string(
      'pyproject.toml', 
      f'name = "{current_name}"', 
      f'name = "{new_name}"'
      )
    replace_line_containing_string(
      'pyproject.toml', 
      f'name = "{current_name}"', 
      f'name = "{new_name}"'
      )
    #update name in _extension.yml
    replace_line_containing_string(
      f'{new_name}/template_files/_extension.yml', 
      f'{current_name}-import = "{current_name}.qmd_template.cli_import_template:_cli_import_template"',
      f'{new_name}-import = "{new_name}.qmd_template.cli_import_template:_cli_import_template"'
      )
    #update name in template.qmd
    replace_line_containing_string(
      f'{new_name}/template_files/template.qmd', 
      f'  {current_name}-revealjs:',
      f'  {new_name}-revealjs:',
      )
    #update name in plotnine_theme.py
    replace_line_containing_string(
      f'{new_name}/plotnine/plotnine_theme.py', 
      f'class {current_name}_plotnine_theme(theme_bw):',
      f'class {new_name}_plotnine_theme(theme_bw):',
      )
    #update name in import_template.py
    replace_line_containing_string(
      f'{new_name}/qmd_template/import_template.py', 
      f"  quarto_dir = destination_dir.joinpath('_extensions/{current_name}')",
      f"  quarto_dir = destination_dir.joinpath('_extensions/{new_name}')",
      )
    #update name in README.md
    replace_in_md('README.md', current_name, new_name)
    #update name in PACKAGE.md
    replace_in_md('PACKAGE.md', current_name, new_name)
    
  if 'version' in config_diff:
    replace_line_containing_string(
      'pyproject.toml', 
      f'version = "{config_prev["version"]}"', 
      f'version = "{["version"]}"'
      )
    
  if 'authors' in config_diff:
    replace_line_containing_string(
      'pyproject.toml', 
      f'authors = {config_prev["authors"]}'.replace("'", '"'),
      f'authors = {config_diff["authors"]}'.replace("'", '"')
      )

  #---------------------------------------------------------------------------------
  # Font
  #---------------------------------------------------------------------------------

  if 'font' in config_diff:

    #update fonts.css
    font_path = f'{new_name}/template_files/fonts.css'

    font_family = config['font']['font-family']
    font_family_prev = config_prev['font']['font-family']
    font_type = config['font']['font-type'].lower()
    font_regular = config['font']['font-regular']
    font_bold = config['font']['font-bold']
    font_italic = config['font']['font-italic']
    font_bolditalic = config['font']['font-bolditalic']

    # update font type to be used below
    if font_type == 'ttf':
      font_type = "truetype"
    elif font_type == 'otf':
      font_type = "opentype"
    elif font_type in ['woff', 'woff2', 'truetype', 'opentype']:
      pass #don't need to update in this case as these are valid options
    else:
      raise ValueError("Error: Font type should be one of ttf, otf, woff, woff2")
    
    line_font_regular = f'@font-face {{ font-family:{font_family}; font-style:normal; font-weight:400; font-display:swap; src:url(./font/{font_regular}) format("{font_type}"); }}'
    line_font_italic = f'@font-face {{ font-family:{font_family}; font-style:italic; font-weight:400; font-display:swap; src:url(./font/{font_italic}) format("{font_type}"); }}'
    line_font_bold = f'@font-face {{ font-family:{font_family}; font-style:normal; font-weight:700; font-display:swap; src:url(./font/{font_bold}) format("{font_type}"); }}'
    line_font_bolditalic = f'@font-face {{ font-family:{font_family}; font-style:italic; font-weight:700; font-display:swap; src:url(./font/{font_bolditalic}) format("{font_type}"); }}'

    with open(font_path, 'w') as file:
      file.write(str(line_font_regular) + '\n')
      file.write(str(line_font_italic) + '\n')
      file.write(str(line_font_bold) + '\n')
      file.write(str(line_font_bolditalic) )

    #update font in plotnine_theme.py
    if 'font-family' in config_diff['font']:
      replace_line_containing_string(
        f'{new_name}/plotnine/plotnine_theme.py', 
        f"BASE_FAMILY='{font_family_prev}'",
        f"BASE_FAMILY='{font_family}'",
        )

  #---------------------------------------------------------------------------------
  # Quarto
  #---------------------------------------------------------------------------------

  if 'quarto' in config_diff:
    #update theme.scss
    quoted_variables = ['section-background', 'thank-you-background', 'slide-background', 'page-size']
    true_false_variables = ['logo', 'slide-background-image']

    for item in config_diff['quarto']:
      variable = f'${item.lower()}'
      value = str(config["quarto"][item])

      if item in quoted_variables:
        value = f"'{value}'"
      if item in true_false_variables:
        value = str(value).lower()

      replace_line_containing_string(
        f'{new_name}/template_files/theme.scss', 
        f'{variable}',
        f'{variable}: {value};',
        start_of_line_only=True
        )

    #update _extension.yml
    if 'logo-file' in config_diff['quarto']:
      replace_line_containing_string(
        f'{new_name}/template_files/_extension.yml', 
        f"      logo: '{config_prev['quarto']['logo-file']}'",
        f"      logo: '{config['quarto']['logo-file']}'"
      )

    if 'title-background' in config_diff['quarto']:
      replace_line_containing_string(
        f'{new_name}/template_files/_extension.yml', 
        f"        data-background-image: '{config_prev['quarto']['title-background']}'",
        f"        data-background-image: '{config['quarto']['title-background']}'"
      )

  #---------------------------------------------------------------------------------
  # plotnine
  #---------------------------------------------------------------------------------

  if 'plotnine' in config_diff:
    for item in config_diff['plotnine']:
      variable = item.upper().replace("-", "_")
      value = config["plotnine"][item]
      if not isinstance(value, (int, float)):
        value = f"'{value}'"

      replace_line_containing_string(
        f'{new_name}/plotnine/plotnine_theme.py', 
        f'{variable}',
        f'{variable}={value}',
        start_of_line_only=True
        )

  #---------------------------------------------------------------------------------
  # great-tables
  #---------------------------------------------------------------------------------

  if 'great-tables' in config_diff:
    print(True)

  #---------------------------------------------------------------------------------
  # overwrite previous-config.yaml file after all changes are made
  #---------------------------------------------------------------------------------

  comment = "# This YAML file is automatically generated. Do not edit manually.\n\n"

  with open('template_config/previous_config.yaml', 'w') as file:
      file.write(comment)
      yaml.safe_dump(config, file)


#-----------------------------------------------------------------------------------
# Supporting functions
#-----------------------------------------------------------------------------------

# Function to load YAML file
def load_yaml(file_path):
  with open(file_path, 'r') as file:
    return yaml.safe_load(file)
    
def rename_folder(old_folder_path:str, new_folder_name:str):
  old_folder_path = Path(old_folder_path)
  parent_directory = old_folder_path.parent
  new_folder_path = parent_directory / new_folder_name
  old_folder_path.rename(new_folder_path)

def replace_line_containing_string(file_path: str, search_string: str, replacement: str, start_of_line_only: bool = False):
  with open(file_path, 'r') as file:
    lines = file.readlines()

  found = False
  for i, line in enumerate(lines):
    if start_of_line_only:
      if line.startswith(search_string):
        lines[i] = replacement + '\n'  # Replace the line
        found = True
        break
    else:
      if search_string in line:
        lines[i] = replacement + '\n'  # Replace the line
        found = True
        break
  
  if found:
    with open(file_path, 'w') as file:
      file.writelines(lines)

def replace_in_md(file_path, old_str, new_str):
    try:
        # Read the entire content of the file
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Perform the replacement
        updated_content = file_content.replace(old_str, new_str)

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

    except FileNotFoundError:
        print(f'Error: File not found - {file_path}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
  config_template()