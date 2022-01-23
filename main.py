"""
Ref: https://jinja.palletsprojects.com/en/3.0.x/

Ref: https://www.youtube.com/watch?v=q9na89PgzGk
Ref: https://www.youtube.com/watch?v=9v6kDoUjIs4
"""

from jinja2 import Environment, FileSystemLoader
import json

with open("infoblox_faz.json", "r") as fin:
    faz = json.load(fin)['result']

headings = ["ipv4addr", "name", "network", "mac"]

fileloader = FileSystemLoader("templates")
env = Environment(loader=fileloader)

rendered = env.get_template("faz.html").render(faz=faz, title= "fixed addresses NU Infoblox", headings=headings)

with open ("infoblox_faz.html", "w") as fout:
    fout.write(rendered)

