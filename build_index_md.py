
import os

posts_dir = "posts"
output_file = "index.html"

entries = []
for filename in sorted(os.listdir(posts_dir)):
    if filename.endswith(".md"):
        date = filename.split("_")[0]
        entries.append(f'<li><a href="posts/{filename}">{date}</a></li>')

with open(output_file, "w") as f:
    f.write("""<html>
<head><link rel="stylesheet" href="style.css"><title>Muja Garden</title></head>
<body>
<h1>Muja Garden</h1>
<ul>
""")
    f.writelines("\n".join(entries))
    f.write("</ul></body></html>")
