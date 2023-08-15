import time
import random
import instaloader
from pyrogram import Client


bot = instaloader.Instaloader()
TELEGRAM_CHANNEL_ID = -1001951565322
API_ID = 15354199
API_HASH = "4b42c4babb1f7866c005b8c5a967add7"

bot.load_session_from_file("botforern2", filename="./session-botforern2")
posts = instaloader.Profile.from_username(bot.context, "ernest_kuhni").get_posts()


def send_message(post):
    try:
        caption_with_media = ""
        if post.caption and len(post.caption) > 1024:
            print("Огромный пост... разбиваю на 2 поста...")
            for i in post.caption:
                caption_with_media += i
                if len(caption_with_media) > 700 and i in [".", "!", "?"]:
                    if post.is_video:
                        app.send_video(TELEGRAM_CHANNEL_ID, post.video_url, caption=caption_with_media)
                    else:
                        app.send_photo(TELEGRAM_CHANNEL_ID, post.url,
                                       caption=caption_with_media)
                    break
            app.send_message(TELEGRAM_CHANNEL_ID, post.caption[len(caption_with_media):len(post.caption)])
        else:
            if post.is_video:
                app.send_video(TELEGRAM_CHANNEL_ID, post.video_url, caption=post.caption)
            else:
                app.send_photo(TELEGRAM_CHANNEL_ID, post.url, caption=post.caption)
    except Exception as e:
        print(f"[-] Пост не отправился\nОшибка: {e}")


def get_new_post(posts):
    for i in posts:
        return i


with Client("my_acc", API_ID, API_HASH) as app:
    posts_ = [post for post in posts]
    while True:
        posts = instaloader.Profile.from_username(bot.context, "ernest_kuhni").get_posts()
        last_post = get_new_post(posts)
        if last_post not in posts_:
            send_message(last_post)
            posts_.append(last_post)

        time.sleep(random.randint(6000,8000))
