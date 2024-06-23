# brandtemplate

A customisable package to enable the creation of [Quarto](https://quarto.org/) presentations using your own brand to share the output of your python based analysis to stakeholders. 

The template uses plotnine and great-tables to create graphs and tables and has themes for both of these that go with the quarto template.

## Customisation of template

- Fork this repo to create your own master template.
- Update `config.yaml` in `template_config` to update the formatting of the template.
  - If changing the fonts add the new font files into `brandtemplate/template_files/font` and delete the existing files.
  - Change the background and logo image files in `brandtemplate/template_files` to the ones for your brand. This can be copied out of your PowerPoint template and saved as an image.
- Run `python template_config/config_template.py` to update the template based on the changes to your `config.yaml`.
- Make any changes to `PACKAGE.md` to update the documentation for how to install the package if using a private repo.


## Build and publish template

- Install poetry - `pip install poetry`
- Install the packages for the template - `poetry install`
- Build the package - `poetry build`
- Add config to enable publishing
  - If publishing to PYPI then can use `poetry config pypi-token.pypi <YOUR_PYPI_API_TOKEN>`
  - If publishing this to a private repository then see the [poetry documentation](https://python-poetry.org/docs/repositories/#publishing-to-a-private-repository) for more information

## Installation

Install the package via `pip install brandtemplate`
*You might need to update this if you are using a private repository*

## Usage

### Add the quarto template to a project

Run the following command via `brandtemplate-import` to import the template into the current working directory.

This has the following optional arguments 
- `-n` or `--name`: Renames the qmd file when importing the template. Defaults to "template.qmd" if omitted.
- `-d` or `--directory`: Specifies what directory to copy the template into. Defaults to the current working directory if omitted.

## Features