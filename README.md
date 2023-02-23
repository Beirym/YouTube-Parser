# youtube-parser
Parsing videos from YouTube, information about them and statistics into a separate text file

# Libraries

The list of libraries that were used to run the parser

	json
  	yt_dpl
  	urllib.request

# How it works

The user sends the program the ID of the YouTube channel from which the video needs to be parsed, after which the parser receives all the videos from this YouTube channel. When all the videos are received, the program creates a file to which information and video statistics will be added later. Then the parser receives information about each received video in turn and writes it to a file.

# What you need to work

You must have an account with an API key and connected Youtube API v3 in Google Cloud

# Important

The daily quota for a free Google Cloud account for Youtube API v3 is 10,000 requests
