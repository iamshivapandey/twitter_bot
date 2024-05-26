from scrap_data import get_data
from create_post import filter_images 
import tweepy.client
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv('/home/shiva/my_work/social_media/twitter_bot/.env')
os.chdir("/home/shiva/my_work/social_media/twitter_bot")
date = datetime.today().date()


def clear_directory(directory_path):

    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        
        # Check if the entry is a file or directory
        if os.path.isfile(full_path):
            # Remove the file
            os.remove(full_path)
        elif os.path.isdir(full_path):
            # Recursively clear subdirectories
            clear_directory(full_path)
            # Remove the empty directory
            os.rmdir(full_path)


def do_tweet():
    try:
        print("--------------------->>> making tweet")
        api_key = os.environ['api_key']
        api_secret = os.environ['api_secret']
        bearer_token = os.environ['bearer_token']
        access_token = os.environ['access_token']
        access_token_secret = os.environ['access_token_secret']

        # Authenticate with Twitter using OAuthHandler
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Create API object
        api = tweepy.API(auth)

        # Create a client
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )




        # Paths to your images
        image_text_pairs = [
            ('daily_ss/fear_greed_dominance_{0}.png', "BTC Dominance, ETH Gas Price, Fear & Greed Index"),
            ('daily_ss/top_10_cryptos_{0}.png', "Top 10 Crypto Currencies"),
            ('daily_ss/trending_cryptos_{0}.png', "Trending Crypto Currencies"),
            ('daily_ss/gainers_losers_{0}.png', "Gainers & Losers")
        ]

        media_ids = []
        # Upload images and get media_ids
        for image_path, tweet_text in image_text_pairs:
            # Upload image
            upload_response = api.media_upload(image_path.format(date))
            media_ids.append(upload_response.media_id)
            print(f"Uploaded image: {image_path.format(date)}")


        tweet_text= f'''
🔴 𝐂𝐫𝐲𝐩𝐭𝐨 𝐌𝐚𝐫𝐤𝐞𝐭 𝐔𝐩𝐝𝐚𝐭𝐞 🔴
📅 🅓🅐🅣🅔 - {date} 📅

    Post1️⃣ = Fear & Greed Index🏴‍☠️
    Post2️⃣ = Top 10 Crypto💎
    Post3️⃣ = Top Trending Crypto🚀
    Post4️⃣ = Gainers📈 & Losers📉

#Bitcoin #Ethereum #CryptoCurrencies #trendingcryptos #investing #invest'''

        tweet = client.create_tweet(text=tweet_text, media_ids=media_ids)

        print("Tweet posted successfully!")

        return True
    except Exception as e:
        print("---------------->>>",e)
        return False


def bot():

    print("--------------------------->>> Execution Started")

    try:
        resp1 = get_data()

    except Exception as e:
        print("----------------->>>",e)
        

    if not resp1:
        return
    
    try:
        resp2 = filter_images()

    except Exception as e:
        print("----------------->>>",e)
        

    if not resp2:
        return
    
    try:
        resp3 = do_tweet()

    except Exception as e:
        print("----------------->>>",e)

    if not resp3:
        return
    
    directory_path = 'daily_ss'
    clear_directory(directory_path)

    print("--------------------------->>> Execution Completed")

    return {"success": 200}

print(bot())
    
