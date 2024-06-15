from itertools import cycle

def plotnine_titles(
    plotnine_fig,
    title=None,
    subtitle=None,
    caption=None,
    fontfamily=None,
    title_size=32,
    title_color='black',
    subtitle_size=20,
    subtitle_color='darkgrey',
    caption_size=15,
    caption_color='grey',
    draw_fig=True,
    **kwargs
    ):
  """
  
  """
  if draw_fig:
    plotnine_fig = plotnine_fig.draw()

  y_title = 1.02 if subtitle is None or subtitle == '' else 1.13
  if title is not None:
    plotnine_fig = plotnine_text(
      plotnine_fig=plotnine_fig, 
      text=title, 
      x=0, 
      y=y_title, 
      size=title_size, 
      color=title_color,
      ha='left', 
      va='bottom', 
      fontfamily=fontfamily,
      draw_fig=False,
      **kwargs
      )
    
  if subtitle is not None:
    plotnine_fig = plotnine_text(
      plotnine_fig=plotnine_fig,
      text=subtitle, 
      x=0, 
      y=1.02, 
      size=subtitle_size, 
      color=subtitle_color,
      ha='left', 
      va='bottom', 
      fontfamily=fontfamily, 
      draw_fig=False,
      **kwargs
      )

  if caption is not None:
    plotnine_fig = plotnine_text(
      plotnine_fig=plotnine_fig,
      text=caption, 
      x=0, 
      y=-0.05, 
      size=caption_size, 
      color=caption_color,
      ha='left', 
      va='top', 
      fontfamily=fontfamily, 
      draw_fig=False,
      **kwargs
      )

  return plotnine_fig

def plotnine_coloured_axis_labels(
    plotnine_fig,
    label_color_dict,
    default_label_color='#36454f',
    axis='X',  
    draw_fig=True      
    ):
  if draw_fig:
    plotnine_fig = plotnine_fig.draw()
  
  for ax in plotnine_fig.axex:
    if 'X' in axis.upper():
      for l in ax.get_xticklabels():
        c = label_color_dict.get(l.get_text())
        if c is None:
          c = default_label_color
        l.set_color(c)

    if 'Y' in axis.upper():
      for l in ax.get_yticklabels():
        c = label_color_dict.get(l.get_text())
        if c is None:
          c = default_label_color
        l.set_color(c)
       
  return plotnine_fig

def plotnine_text(
    plotnine_fig,
    x,
    y,
    text,
    color='black',
    weight='regular',
    size=20,
    style='normal',
    va='bottom',
    ax_id=0,
    draw_fig=True,
    **kwargs
  ):

  if draw_fig:
    plotnine_fig = plotnine_fig.draw()

  ax = plotnine_fig.axes[ax_id]

  #convert to lists if not already so can iterate through
  text = text if isinstance(text, list) else [text]
  color = color if isinstance(color, list) else [color]
  weight = weight if isinstance(weight, list) else [weight]
  size = size if isinstance(size, list) else [size]
  style = style if isinstance(style, list) else [style]

  for idx, (t, c, w, sz, st) in enumerate(zip(text, cycle(color), cycle(weight), cycle(size), cycle(style))):
    if idx == 0:
      text = plotnine_fig.text(s=t, x=x, y=y, fontweight=w, size=sz, color=c, style=st, va=va, **kwargs)
    else:
      text = ax.annotate(text=t, xycoords=text, xy=(1,0), fontweight=w, size=sz, color=c, style=st, va=va, **kwargs)
  
  return plotnine_fig