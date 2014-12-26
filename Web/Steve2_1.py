#!/usr/bin/python
import os
import platform
print "Content-Type: text/html"
print
print """\
<!DOCTYPE html>
<html lang="en">
<head>  <meta charset="utf-8">
  <title>Hello World from Python by Steve</title>
 </head>


    <h1>Hello World!</h1>
    <h2>From Python </h2>
    <img src="/graphics/photo.jpg" alt="picture of me">
    <p></p>
</html>
"""
print "but wait there's more"
a = 5
b = 6
print str(a + b)

