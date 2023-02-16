#!/bin/bash

# instructions:
# place this file in the same directory as the html file
# on the github repository webpage go to settings and add a webhook
# use the following as the payload URL: https://web.engr.oregonstate.edu/~duqueocj/github-helloearth/deploy.sh
# leave all settings on default

# Fetch the latest changes from Github
# cd /path/to/your/website
git pull origin master
