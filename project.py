
"""Creating a social media(Facebook) bot 
   tha run on schedule time which 
   will save as a logger
   
   showing image randomly to advertize what 
   you are dealing with"""



import schedule
import time
import random
import logging
import os
import sys
import tkinter as tk
from PIL import Image, ImageTk



# RESOURCE PATH 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



# CONFIGURATION
CHAT_ID = "0246277997"

MESSAGES = [
    "Good product",
    "All kinds of Africa wear",
    "Local wear",
    "Ladies and gent traditional wear"
]

HASHTAGS = [
    "#GentWear",
    "#LadiesWear",
    "#WeddingDecoration",
    "#KenteWear"
]

POST_TIMES = ["06:53", "06:54", "06:55"]

IMAGE_FOLDER = resource_path("images")

DISPLAY_TIME = 5000  # milliseconds (5 seconds)



# LOGGER SETUP 
LOG_FILE = os.path.join(os.getcwd(), "Facebook_bot.log")

logging.basicConfig(
    filename = LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Log file location:", LOG_FILE)



# GENERATE HASHTAGS
def generate_hashtag():
    return " ".join(random.sample(HASHTAGS, 2))


# SHOW IMAGE 
def show_image(image_path):
    try:
        root = tk.Tk()
        root.title("Product Display")

        img = Image.open(image_path)
        img = img.resize((500, 500)) 

        photo = ImageTk.PhotoImage(img)

        label = tk.Label(root, image = photo)
        label.pack()

# Close after 5 seconds
        root.after(DISPLAY_TIME, root.destroy)

        root.mainloop()

    except Exception as e:
        print("Error showing image:", e)
        logging.error(f"Image error: {e}")



# GET RANDOM IMAGE
def get_random_image():
    print("Checking images in:", IMAGE_FOLDER)

    if not os.path.exists(IMAGE_FOLDER):
        logging.error("Image folder not found")
        return None

    images = [
        img for img in os.listdir(IMAGE_FOLDER)
        if img.lower().endswith((".jpg", ".png", ".jpeg"))
    ]

    if not images:
        logging.warning("No images found")
        return None

    return os.path.join(IMAGE_FOLDER, random.choice(images))



# SIMULATED FACEBOOK POST
def simulate_post(chat_id, message, tags=None, image=None):
    print("\nConnecting to facebook API...")
    time.sleep(random.uniform(1, 2))

    print("Chat ID:", chat_id)
    print("Message:\n", message)

    if tags:
        print("Tags:", tags)

    if image:
        print("Displaying image:", image)
        show_image(image)

    logging.info(f"POST SENT | {message} | {tags} | {image}")

    return {"ok": True, "status": "SIMULATED SUCCESS"}



# GIVEN FACEBOOK BOT A TASK
def post_content():
    message = random.choice(MESSAGES)
    tags = generate_hashtag()
    image = get_random_image()

    full_message = f"{message}\n{tags}"

    if image:
        full_message += f"\n{image}"

    response = simulate_post(
        CHAT_ID,
        full_message,
        tags = tags,
        image = image
    )

    print("Response:", response)



# RUNNING BOT

def run_bot():
    print("Odonti Fashion 🧵 Bot Running...")
    logging.info("Bot started")

    for t in POST_TIMES:
        schedule.every().day.at(t).do(post_content)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    run_bot()