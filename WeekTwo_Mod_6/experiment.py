""" Problem:
    Download and change desktop wallpapers automatically
 """
# import json
# import requests
import PyWallpaper
# api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"


# # Get the json
# response = requests.get(api_url)
# content = response.content.decode('UTF-8')

# # Convert string to json
# dict_content = json.loads(content)
# # print(dict_content)

# # Get the image url
# image_url = dict_content['url']
# # print(image_url)

# # Download the image
# res = requests.get(image_url)
# # print(res)

# # Save the image
# with open('apod.png','wb') as image:
#     image.write(res.content)

# Set as wallpaper
PyWallpaper.change_wallpaper('./apod.png')