===================
minidetector README
===================


This application is a simple middleware and associated decorator that will
add a ".mobile" attribute to your request objects, which, if True, means the
requester is coming to you from a mobile phone (cellphone), PDA, or other
device that should be considered small screened, or have an underpowered
browser, such as games consoles.

This mostly works using a list of search strings, though there are a couple of
other tricks, like detecting the presence of Opera Mini. The strings are in an
easily-parseable text file, and thus can be used for other similar projects.

It also includes a pretty extensive list of user agents to test against.

You can see it in use on http://AmIOnAMobile.com/ and http://AmIOnACellphone.com/