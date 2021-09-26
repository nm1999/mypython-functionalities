import webbrowser
import time
import cgi
name = "Nyanzi Matia is not sick"
age = 13
html_content = f"<html><head><h1>{name}</h2><i>{age}</i> <form><input type='text'></form></head></html>"

with open("index.html","w") as html_file:
    html_file.write(html_content)
    print("html file created")

time.sleep(0.2)
webbrowser.open_new_tab("index.html")