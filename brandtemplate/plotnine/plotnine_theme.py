from plotnine import theme_bw, theme

from plotnine.themes.elements import (
  element_blank,
  element_line,
  element_rect,
  element_text
)

class branded_plotnine_theme(theme_bw):
  """
  A custom theme for plotnine.

  Args:
      base_size (int, optional): The base font size for the plot. Defaults to 15.
      base_family (str, optional): The base font family for the plot. Defaults to 'Inter'.
      gridlines (str, optional): Determines which gridlines to display. Values are 'X', 'Y' or 'XY'. Defaults to 'X'.
      axis_title (str, optional): Determins the title for the axes to display. Values are 'X', 'Y' or 'XY'. Defaults to ''.
      axis_line (str, optional): Determines if axis lines are displayed. Values are 'X', 'Y' or 'XY'. Defaults to 'X'.
      axis_start_zero (str, optional): Recolors the axis if it doesn't start at zero. Values are 'X', 'Y' or 'XY'. Defaults to 'X'.
      title_size (int, optional): Font size for the plot title. Defaults to 32.
      subtitle_size (int, optional): Font size for the plot subtitle. Defaults to 20.
      caption_size (int, optional): Font size for the plot caption. Defaults to 15.

  Returns:
      None
  """

  def __init__(
      self, 
      base_size=15, 
      base_family='Inter',
      gridlines='X',
      axis_title='',
      axis_line='X',
      axis_start_zero='X',
      title_size=32,
      subtitle_size=20,
      caption_size=15

      ):
    super().__init__(base_size, base_family)
    self += theme(
      line=element_rect(color='#36454f'),
      rect=element_rect(fill='white', color='black'),
      text=element_text(color='#36454f', fontweight='regular'), 
      title=element_text(color='#36454f'),
      
      plot_background=element_rect(color='white', fill='white'),
      strip_background=element_rect(fill='white'),

      plot_title=element_text(color='#36454f', fontweight='bold', size=title_size),
      plot_subtitle=element_text(color='#5E6A72', fontweight='regular', size=subtitle_size),
      plot_caption=element_text(color='#5E6A72', fontweight='regular', size=caption_size),

      plot_margin=0, #check this

      panel_border=element_blank(),
      panel_grid_major=element_line(color = '#ededed'),
      panel_grid_major_x=element_line(color='#ededed') if 'X' in gridlines.upper() else element_blank(),
      panel_grid_major_y=element_line(color='#ededed') if 'Y' in gridlines.upper() else element_blank(),
      panel_grid_minor=element_blank(),

      axis_title_x=element_text() if 'X' in axis_title.upper() else element_blank(),
      axis_title_y=element_text() if 'Y' in axis_title.upper() else element_blank(),
      axis_ticks=element_blank(),
      axis_line_x=element_blank if 'X' not in axis_line.upper() else element_line() if 'X' in axis_start_zero.upper() else element_line(color='#ededed'),
      axis_line_x=element_blank if 'Y' not in axis_line.upper() else element_line() if 'Y' in axis_start_zero.upper() else element_line(color='#ededed'),

      legend_background=element_blank(),
      legend_position='bottom',
      legend_box='vertical',
      legend_direction='horizontal'
      )