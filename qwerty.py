import pyautogui
import pyperclip
import time
from together import Together

# def is_last_message_from_sender(chat_log, sender_name=" Tushar"):
    # messages = chat_log.strip().split("\n")
    # # Reverse to get last message first
    # for i in reversed(messages): 
    #     parts = i.split(": ", 2)
    #     if len(parts) == 3:
    #         timestamp, sender, text = parts
    #         if sender.strip() == sender_name:
    #             return True
    #         else:
    #             return False
    # return False
def is_last_message_from_sender(chat_log, sender_name="M"):
    messages = chat_log.strip().split("\n")
    for i in reversed(messages):
        try:
            # WhatsApp format: [3:34 AM, 4/14/2025] Tushar: message
            if "]" in i and ": " in i:
                timestamp_and_name, message = i.split("] ", 1)
                name, _ = message.split(":", 1)
                if name.strip() == sender_name.strip():
                    print(f"✅ Last message is from: {name.strip()}")
                    return True
                else:
                    print(f"❌ Last message was from: {name.strip()}")
                    return False
        except Exception as e:
            print("⚠️ Failed to parse line:", i)
            continue
    return False

# Initialize Together AI client once
client = Together(api_key="")

# Step 1: Click on the Chrome icon to open WhatsApp Web
pyautogui.click(557, 749)
time.sleep(3)  # Let WhatsApp Web load

while True:
    try:
        # Step 2: Drag to select the text
        pyautogui.moveTo(525,245, duration=0.5)
        pyautogui.dragTo(1342,658, duration=1, button='left')

        # Step 3: Copy selected text
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)  # Allow clipboard to update

        # Step 4: Get text from clipboard
        chat_history = pyperclip.paste()
        print("Chat History:\n", chat_history)

        # Step 5: Check if last message is from sender
        if is_last_message_from_sender(chat_history):
            # Step 6: Generate response using Together AI
            completion = client.chat.completions.create(
                model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
                messages=[
                    {"role": "system", "content": "You are Gaurav, a friendly coder from India who speaks Hindi and Respond like Gaurav would and write short messages not to long messages."},
                    {"role": "user", "content": chat_history}
                ]
            )

            response = completion.choices[0].message.content
            print("AI Response:\n", response)

            # Step 7: Copy response and paste
            pyperclip.copy(response)
            time.sleep(1)

            # Click on input field and send message
            pyautogui.click(875,688)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')
        pyautogui.click(500,394)
        time.sleep(5)  # Wait before checking again

    except Exception as e:
        print("Error:", e)
        time.sleep(5)

