import json
import urllib.request
from yt_dlp import YoutubeDL


channel_id = input('Past channel ID: ')
api_key = "your Google Cloud API key"


# Getting all videos from channel

def get_videos(channel_id):
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    start_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)

    videos = []
    url = start_url

    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)

        except:
            break

    return videos

# /. Getting all videos from channel


videos = get_videos(channel_id) # all videos from the channel

# Creating a file that stores data about each video
with open(f"YT-channel-videos_{channel_id}.txt", 'w') as channel_file:
    channel_file.write(f'''Videos from the channel: {channel_id}
    
[//] Total videos: {len(all_video_links)} [\\\\]
    
--------------- Videos & stats ---------------''')


for video in videos:
    video_id = video.split('https://www.youtube.com/watch?v=')[1]


    # Information about video

    youtube_dl_opts = {
        'ignoreerrors': True,
        'quiet': True
    }

    with YoutubeDL(youtube_dl_opts) as ydl:
        info_dict = ydl.extract_info(video, download=False)
        video_id = info_dict.get("id", None)
        video_views = info_dict.get("view_count", None)
        video_likes = info_dict.get("like_count", None)
        video_date = str(info_dict.get("upload_date", None))[0:4] + '.' + str(info_dict.get("upload_date", None))[4:6] + '.' + str(info_dict.get("upload_date", None))[6:]
        video_duration = info_dict.get("duration", None)
        video_title = info_dict.get('title', None)

    # /. Information about video


    # Writing video information to a file
    with open(f"YT-channel-videos_{channel_id}.txt", 'a') as channel_file:
        channel_file.write(f'''
------------------------------
        
Video ID: {video_id}
Link to the video: {video} 

Title: {video_title}
Release date: {video_date}

Duration: {video_duration} sec 

View statistics:
-> Views: {video_views}
-> Likes: {video_likes}

------------------------------


''')


print(f'''Parsing is completed!

File with the received videos: "YT-channel-videos_{channel_id}.txt"''')
