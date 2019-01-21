from twilio.rest import Client
import socket
from time import sleep
import deets

# Your Account SID from twilio.com/console
print (deets.twilio_sid)
account_sid = deets.twilio_sid
# Your Auth Token from twilio.com/console
auth_token  = deets.twilio_token

import socket
host_name = socket.gethostname()

ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
print(ip)
client = Client(account_sid, auth_token)
message = client.messages.create(
    to= deets.my_phone, 
    from_= deets.twilio_phone,
    body="Card: {}, IP: {}".format(deets.card, ip))
