#!/bin/bash
echo "Content−type: text/html"
echo ’’
echo \<html\>
echo \<head\>
echo \<title\>
echo The current date on the Raspberry Pi
echo \</title\>
echo \</head\>
echo \<body\>
echo \<h1\>
date
echo \</h1\>
echo \</body\>
echo \</html\>
