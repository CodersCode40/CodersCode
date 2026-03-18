import schedule
import time
import random
import logging
import os
import cv2
import sys



# RESOURCE PATH (FOR PYINSTALLER)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



# WHATSAPP CONFIGURATION
CHAT_ID = "0246277997"

MESSAGES = [
    "Good product",
    "All kinds of African wear",
    "Local wear",
    "Ladies and gent traditional wear"
]

HASHTAGS = [
    "#GentWear",
    "#LadiesWear",
    "#WeddingDecoration",
    "#KenteWear"
]

POST_TIMES = ["05:25", "05:26", "05:27"]

IMAGE_FOLDER = resource_path("images")

DISPLAY_TIME = 5000   # 5 seconds



# LOGGER SETUP
logging.basicConfig(
    filename="WhatsApp_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



# GENERATE HASHTAGS
def generate_hashtag():
    selected = random.sample(HASHTAGS, 2)
    return " ".join(selected)



# IMAGE DISPLAY FUNCTION
def show_image(image_path):

    img = cv2.imread(image_path)

    if img is None:
        print("Image not found:", image_path)
        logging.error(f"Image not found: {image_path}")
        return

    cv2.imshow("Product Display", img)
    cv2.waitKey(DISPLAY_TIME)
    cv2.destroyAllWindows()



# GET RANDOM IMAGE
def get_random_image():

    if not os.path.exists(IMAGE_FOLDER):
        print("Image folder not found")
        logging.error("Image folder not found")
        return None

    images = [
        img for img in os.listdir(IMAGE_FOLDER)
        if img.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    if not images:
        print("No images available")
        logging.warning("No images in folder")
        return None

    selected_image = random.choice(images)

    return os.path.join(IMAGE_FOLDER, selected_image)



# SIMULATED WHATSAPP API
def simulate_whatsapp_post(chat_id, message, tags=None, image=None):

    print("Connecting to WhatsApp API...")
    time.sleep(random.uniform(1, 2))

    print("Chat ID:", chat_id)
    print("Message:", message)

    if tags:
        print("Tags:", tags)

    if image:
        print("Image:", image)
        show_image(image)

    response = {
        "ok": True,
        "status": "Message delivered (SIMULATED)"
    }

    if response["ok"]:
        logging.info(f"POST SENT | Chat:{chat_id} | Message:{message} | Tags:{tags} | Image:{image}")
    else:
        logging.error("Failed to send message")

    return response



# BOT TASK
def post_content():

    message = random.choice(MESSAGES)

    tags = generate_hashtag()

    image = get_random_image()

    full_message = f"{message}\n{tags}\n{image}"

    response = simulate_whatsapp_post(
        CHAT_ID,
        full_message,
        tags=tags,
        image=image
    )

    print("API Response:", response)



# SCHEDULER
def run_bot():

    print("Odonti Fashionaire 🧵 Bot Running...")
    logging.info("Bot started")

    for post_time in POST_TIMES:
        schedule.every().day.at(post_time).do(post_content)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    run_bot()