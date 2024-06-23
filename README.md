# brandtemplate

A customisable package to enable the creation of [Quarto](https://quarto.org/) presentations using your own brand to share the output of your python based analysis to stakeholders. 

The template uses plotnine and great-tables to create graphs and tables and has themes for both of these that go with the quarto template.

The template uses the presoutput package ([PYPI](https://pypi.org/project/presoutput/) or [github](https://github.com/aplunket/presoutput)) to convert the .qmd files into either PDF or PPTX documents that can be shared with stakeholders.

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

*You might need to update this command if you have customised this template and you are using a private repository to store your package.*

## Usage

### Add the quarto template to a project

Run the following command via `brandtemplate-import` to import the template into the current working directory.

This command has the following optional arguments:
- `-n` or `--name`: Renames the qmd file when importing the template. Defaults to "template.qmd" if omitted.
- `-d` or `--directory`: Specifies what directory to copy the template into. Defaults to the current working directory if omitted.

### Plotnine functions

#### Add theme to graph 

```{python}
from plotnine import *
from plotnine.data import mpg

(
ggplot(mpg, aes(x='class')) +
  geom_bar() +
  brandtemplate_plotnine_theme() #adds base formatting theme to graph
)
```

#### Add standard titles to graph 

#### Add multi coloured titles to the graph

#### Recolour axis labels 

## Features

### Quarto template

The quarto template has been designed to match your current brand presentation theme so that you can focus on the content rather than having to focus on the formatting. 

- New slides are created by creating a H2 in the qmd file (using `## Slide title goes here`).
- To create a section divider slide you can add the following line `## Slide title goes here {.section-slide}`
- To create a final thank you slide you can add the following line `## Thank you {.thank-you-slide}`
- Multiple columns can be created using the following code:
  ```{quarto}
  :::: {.columns}

  ::: {.column width="50%"}
  Left column
  :::

  ::: {.column width="50%"}
  Right column
  :::
 
  ::::
  ```

See full documentation on revealjs in quarto [here](https://quarto.org/docs/presentations/revealjs/).

Once ready to share then can use the presoutput package ([PYPI](https://pypi.org/project/presoutput/) or [github](https://github.com/aplunket/presoutput)) to convert the file to either PDF or PPTX format.

### Plotnine 

### Great-tables