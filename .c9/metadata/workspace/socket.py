{"filter":false,"title":"socket.py","tooltip":"/socket.py","undoManager":{"mark":9,"position":9,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":10,"column":56},"action":"insert","lines":["#!/usr/bin/python           # This is client.py file","","import socket               # Import socket module","","s = socket.socket()         # Create a socket object","host = socket.gethostname() # Get local machine name","port = 12345                # Reserve a port for your service.","","s.connect((host, port))","print s.recv(1024)","s.close                     # Close the socket when done"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":["5"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["4"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["3"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["2"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["1"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["8"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["8"]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["0"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":11},"end":{"row":6,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1421713562810,"hash":"63676f64a883b94559424727fe11cbca332273a3"}