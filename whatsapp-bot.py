import pywhatkit
from datetime import datetime


messages = [
 {"chat_id": " ", "message": " ", "send_time": "08-15 09:02"},
]

for data in messages:
    chat_id = data["chat_id"]
    message = data["message"]
    send_time_str = data["send_time"]
    
    send_time = datetime.strptime(send_time_str, "%m-%d %H:%M")
    send_time = send_time.replace(year=datetime.now().year)  
    hour = send_time.hour
    minute = send_time.minute


    pywhatkit.sendwhatmsg_to_group(chat_id, message, hour, minute)
    print(f"Nachricht '{message}' wird um {hour}:{minute} am {send_time_str} an Chat-ID {chat_id} gesendet")