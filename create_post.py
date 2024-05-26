from PIL import Image
from datetime import datetime


def cut_image_horizontally(image):

    width, height = image.size

    # Calculate the midpoint
    midpoint = height // 2

    # Cut the image into two halves
    top_half = image.crop((0, 0, width, midpoint))
    bottom_half = image.crop((0, midpoint, width, height))

    return top_half, bottom_half


def resize_image(image, target_width):
    # Get original dimensions
    original_width, original_height = image.size

    # Calculate the new height to maintain aspect ratio
    new_height = int((target_width / original_width) * original_height)

    # Resize the image
    resized_image = image.resize((target_width, new_height))

    return resized_image


def cut_image_vertically(image_path):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size

    # Calculate the midpoint
    midpoint = width // 2.05

    # Cut the image into two halves
    left_half = image.crop((0, 0, midpoint, height))
    right_half = image.crop((midpoint, 0, width, height))

    return left_half, right_half

def merge_images_top_to_bottom(image1, image2):
    # Get dimensions
    width1, height1 = image1.size
    width2, height2 = image2.size

    # Create a new image with the width of the wider image and the height of both images combined
    new_image = Image.new('RGB', (max(width1, width2), height1 + height2))

    # Paste images into the new image
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, height1))

    # Save the new image
    return new_image

def merge_images_left_to_right(image1, image2):
    # Get dimensions
    width1, height1 = image1.size
    width2, height2 = image2.size

    # Create a new image with the width of both images combined and the height of the taller image
    new_width = width1 + width2
    new_height = max(height1, height2)
    new_image = Image.new('RGB', (new_width, new_height))

    # Paste images into the new image
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (width1, 0))

    return new_image

def filter_images():
    try:
        print("------------------->>> Data Cleaning Started")
        date = datetime.today().date()
        # Open an image
        image = Image.open(f'daily_ss/upper_half_{date}.png')

        # Crop the image
        box = (1030, 220, 1400, 400)
        cropped_image = image.crop(box)

        cropped_image.save(f"daily_ss/fear_greed_{date}.png")

        # Crop the image
        box = (20, 13, 850, 40)
        cropped_image = image.crop(box)

        cropped_image.save(f"daily_ss/dominance_gas_{date}.png")

        left_half, right_half = cut_image_vertically(f"daily_ss/dominance_gas_{date}.png")

        size = 1000
        left_half = resize_image(left_half,size)
        right_half = resize_image(right_half,size)



        # Merge the halves top to bottom
        image2 = Image.open(f"daily_ss/fear_greed_{date}.png")
        image2 = resize_image(image2,size)

        img = merge_images_top_to_bottom(left_half, right_half)

        img = merge_images_top_to_bottom(img,image2)

        img.save(f"daily_ss/fear_greed_dominance_{date}.png")

        image = Image.open(f'daily_ss/lower_half_{date}.png')
        # Crop the image Left Upper Right Lower
        box = (100, 20, 1500, 870)
        cropped_image = image.crop(box)

        cropped_image.save(f"daily_ss/top_10_cryptos_{date}.png")


        image = Image.open(f'daily_ss/trending_cryptos_{date}.png')
        # Crop the image Left Upper Right Lower
        box = (100, 320, 1500, 1170)
        cropped_image = image.crop(box)

        cropped_image.save(f"daily_ss/trending_cryptos_{date}.png")


        image = Image.open(f'daily_ss/gainers_{date}.png')
        # Crop the image Left Upper Right Lower
        box = (100, 300, 1500, 1100)
        cropped_image = image.crop(box)

        cropped_image.save(f"daily_ss/gainers_{date}_1.png")

        image = Image.open(f'daily_ss/losers_{date}.png')
        # Crop the image Left Upper Right Lower
        box = (100, 50, 1500, 800)
        cropped_image = image.crop(box)

        cropped_image.save(f"daily_ss/losers_{date}_1.png")


        gainers_up, gainers_down = cut_image_horizontally(Image.open(f'daily_ss/gainers_{date}_1.png'))


        losers_up, loosers_down = cut_image_horizontally(Image.open(f'daily_ss/losers_{date}_1.png'))


        merge_images_top_to_bottom(gainers_up,losers_up).save(f"daily_ss/gainers_losers_{date}.png")

        print("------------------->>> Data Cleaning Completed")

        return True

    except Exception as e:
        print("------------------------->>>",e)
        return False

