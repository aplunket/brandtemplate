# include this in top of qmd file
# import polars as pl
# from plotnine import *
# from mizani.formatters import *
# import matplotlib.pyplot as plt
#
# from _extensions.branded_template.plotnine_theme import branded_theme
#
# %config InlineBackend.figure_format = 'svg'
# 
# from matplotlib import font_manager as fm
# font_dir = '_extensions/branded_template'
# font_files = fm.findSystemFonts(fontpaths=font_dir)
# for file in font_files:
#   fm.fontManager.addfont(file)

from plotnine import theme_bw, theme

from plotnine.themes.elements import (
  element_blank,
  element_line,
  element_rect,
  element_text
)

from os import path 

import matplotlib.font_manager as fm

class branded_theme(theme_bw):
  """
  Add description of values here
  """

  def __init__(
      self, 
      base_size=15, 
      base_family=None,
      font_file='_extensions/branded-template/Inter-Regular.woff2',
      font_file_title='_extensions/branded-template/Inter-Bold.woff2'
      ):
    super().__init__(base_size, base_family)
    if path.isfile(font_file):
      self += theme(
        text=element_text(fontproperties=fm.FontProperties(fname=font_file, size=20))
      )
    if path.isfile(font_file_title):
      self += theme(
        plot_title=element_text(ha='left', fontproperties=fm.FontProperties(fname=font_file_title, size=30))
      )
    self += theme(
      panel_border=element_blank(),
      plot_background=element_rect(color='white', fill='white'),
      line=element_rect(color='#36454f'),
      rect=element_rect(fill='white', color='black'),
      text=element_text(color='#36454f'), 
      title=element_text(color='#36454f')
      )
    
'''
panel.border = element_rect(fill=NA),
legend.background = element_rect(color = NA),
line = element_line(linetype = 1, color = "#36454f"),
rect = element_rect(fill = "white", color = "black", linetype = 0),
text = element_text(color = "#36454f"),
title = element_text(family = "Georgia", color = "#36454f", size = rel(1)),
axis.title = element_blank(),
axis.text = element_text(face = "bold", size = rel(1)),
axis.text.x = if(grepl('X', axis_title, ignore.case=TRUE)) {element_text(face = "bold", size = rel(1))} else {element_blank()},
axis.text.y = if(grepl('Y', axis_title, ignore.case=TRUE)) {element_text(face = "bold", size = rel(1))} else {element_blank()},
axis.ticks = element_line(color = NULL),
axis.ticks.y = if(grepl('Y', axis_line, ignore.case=TRUE))
              {if(grepl('Y', axis_start_zero, ignore.case=TRUE)) {element_line(color = NULL)} else {element_line(color = NULL)}}
              else {element_blank()},
axis.ticks.x = if(grepl('X', axis_line, ignore.case=TRUE))
              {if(grepl('X', axis_start_zero, ignore.case=TRUE)) {element_line(color = NULL)} else {element_line(color = NULL)}}
              else {element_blank()},
axis.line = element_line(),
axis.line.x = if(grepl('Y', axis_line, ignore.case=TRUE))
              {if(grepl('Y', axis_start_zero, ignore.case=TRUE)) {element_line()} else {element_line(color = "#ededed")}}
              else {element_blank()},
axis.line.y = if(grepl('X', axis_line, ignore.case=TRUE))
              {if(grepl('X', axis_start_zero, ignore.case=TRUE)) {element_line()} else {element_line(color = "#ededed")}}
              else {element_blank()},
legend.position = "top",
legend.direction = "horizontal",
legend.box = "vertical",
panel.grid.major = element_line(color = "#ededed"),
panel.grid.major.x = if(grepl('X', gridlines, ignore.case=TRUE)) {element_line(color = "#ededed")} else {element_blank()},
panel.grid.major.y = if(grepl('Y', gridlines, ignore.case=TRUE)) {element_line(color = "#ededed")} else {element_blank()},
panel.grid.minor = element_blank(),
plot.title = ggtext::element_markdown(hjust=0, family="Georgia", face="bold", padding=unit(c(0, 0, 20, 0), "pt")),
plot.subtitle = ggtext::element_markdown(hjust=0, family="Georgia", face="plain", padding=unit(c(0, 0, 20, 0), "pt")),
plot.caption = ggtext::element_markdown(hjust=0, family="Georgia", face="plain"),
plot.title.position = "plot",
plot.caption.position = "plot",
plot.margin = unit(c(1,1,1,1), "lines"),
strip.background = element_rect(fill = "white")
'''