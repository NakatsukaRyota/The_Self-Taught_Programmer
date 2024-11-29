user_info = {
    "name": "Nakatsuka Ryota",
    "height": 165,
    "place": "Osaka",
    "favorite_color": "purple",
    }

key = input("取得する情報を指定してください: ")
if key in user_info:
    print(user_info[key])