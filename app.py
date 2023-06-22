import subprocess
import time

def open_instagram(device_name):
    subprocess.Popen(["adb", "-s", device_name, "shell", "am", "start", "-a", "android.intent.action.MAIN", "-n", "com.instagram.android/com.instagram.mainactivity.MainActivity"])

def click_on_top_bar(device_name):
    subprocess.Popen(["adb", "-s", device_name, "shell", "input", "tap", "700", "100"])

def click_on_first_message(device_name):
    subprocess.Popen(["adb", "-s", device_name, "shell", "input", "tap", "150", "700"])

def tap_on_input_field(device_name):
    subprocess.Popen(["adb", "-s", device_name, "shell", "input", "tap", "200", "1500"])

def write_message(device_name, message):
    subprocess.Popen(["adb", "-s", device_name, "shell", "input", "text", f"'{message}'"])
    time.sleep(3)

def send_btn(device_name):
    subprocess.Popen(["adb", "-s", device_name, "shell", "input", "tap", "650", "1000"])

def go_back_home(device_name):
    subprocess.Popen(["adb", "-s", device_name, "shell", "input", "keyevent", "KEYCODE_BACK"])

def slide_home(device_name):
    subprocess.Popen(["adb", "-s", device_name, "shell", "input", "swipe","0","800","120","800"])


def scroll_to_post(device_name):
    for i in range(5):
        subprocess.Popen(["adb","-s", device_name ,"shell", "input","swipe", "370","600","370","0"])
        time.sleep(4)

if __name__ == "__main__":
    device_name = "CE5LUKRC5DNBPNH6"
    message = "Yoo"

    open_instagram(device_name)
    time.sleep(2)
    click_on_top_bar(device_name)
    time.sleep(2)
    click_on_first_message(device_name)
    time.sleep(2)
    tap_on_input_field(device_name)
    time.sleep(2)
    write_message(device_name, message)
    send_btn(device_name)
    go_back_home(device_name)
    time.sleep(2)
    slide_home(device_name)
    time.sleep(2)
    slide_home(device_name)
    time.sleep(2)
    scroll_to_post(device_name)
