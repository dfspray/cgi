#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print("")

form = cgi.FieldStorage()
listval = form.getlist('operand')
try:
    result = 0
    for value in listval:
        result += int(value)
    print(str(result))
except (ValueError, TypeError):
    error_message = "Whoops, that wasn't supposed to happen... Please use integers"
    print(error_message)

print("Did I get 113?")
