#!/usr/bin/python

from gimpfu import *

def add_caption(timg, tdrawable, caption="bottom text", font="Impact Condensed", location="bottom"):
  width = tdrawable.width
  height = tdrawable.height

  text_height = height / 5
    
  text_layer = pdb.gimp_text_fontname(timg, None, 0, 0, caption, 10, True, text_height, PIXELS, font)
  pdb.gimp_text_layer_set_color(text_layer, (255,255,255))
  
  text_x = (width / 2) - (text_layer.width / 2)
  text_y = height - text_layer.height
  text_layer.set_offsets(text_x, text_y)

  pdb.gimp_image_select_item(timg, 2, text_layer)
  pdb.gimp_selection_grow(timg, text_height / 20)

  pdb.gimp_context_set_paint_mode(29) # behind
  pdb.gimp_context_set_opacity(100)
  pdb.gimp_context_set_foreground((0,0,0))
  pdb.gimp_drawable_edit_fill(text_layer, 0)
  pdb.gimp_selection_none(timg)
  
  timg.flatten()


register(
  "add_caption",
  "Add Caption",
  "Adds a caption to a predefined location on the image.",
  "Alex Shoup",
  "Alex Shoup",
  "2018",
  "<Image>/Filters/Artistic/Caption",
  "RGB*, GRAY*",
  [
    (PF_STRING, "caption", "Text string to act as the caption", "BOTTOM TEXT"),
    (PF_FONT, "font", "Font", "Impact Condensed"),
    (PF_STRING, "location", "Where the caption will go", "bottom"),
  ],
  [],
  add_caption
)

main()
