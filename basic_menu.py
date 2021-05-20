#!/usr/bin/python3

print()
print("content-type: text/html")
print("Integrating Py with HTML")
import cgi
y = cgi.FieldStorage("x")
command = y.getvalue("x")
print(command)
import subprocess as sp
z = sp.getoutput(command)
print(z)
