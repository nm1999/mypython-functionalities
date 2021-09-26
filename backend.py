print "Content-type: text/html\n\n";
import cgi
form = cgi.FieldStorage()

username = form.getvalue("user")

print username