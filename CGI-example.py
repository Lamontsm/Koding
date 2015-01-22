import os
ip = os.getenv("IP", "0.0.0.0")
port = int(os.getenv("PORT", 8080))

#!/usr/bin/env python

print "Content-Type: text/html"
print
print """\
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
"""