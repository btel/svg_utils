from svgutils.compose import *

CONFIG["svg.file_path"] = "files"
CONFIG["image.file_path"] = "files"

svg1 = SVG("example.svg")
svg2 = SVG("example.svg")

Figure(
    svg1.width + svg2.width,
    max(svg1.height, svg2.height),
    Panel(svg1.scale(2.0, 1.0), Text("(a)", 8, 18, size=14, font="sans")),
    Panel(svg2.scale(1.0, 0.5), Text("(b)", 8, 18, size=14, font="sans")).move(
        svg1.width, 0
    ),
).save("compose_scaling.svg")
