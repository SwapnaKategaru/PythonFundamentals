from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+91703XXXXXXX",
    from_="+130XXXXXXXX",
    body="Hello from Python!")

print(message.sid)