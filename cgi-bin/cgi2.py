#!/usr/bin/env python

print "Content-type: text/html"
print ""
 
print """
<html>
<head><title>My first CGI program</title></head>
<body>
<h1> Python CGI works!! </h1>
<img src="/cgi-bin/graphics/photo.jpg" alt="picture of me">
<h2> Except for the damn graphic!! </h2>
</body>
</html>
      """

