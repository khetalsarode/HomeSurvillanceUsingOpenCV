from twilio.rest import Client

def write():
    account_sid = "Enter account sid from twilio account"
    auth_token = "Enter auth token from twilio account"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to="enter your number",
        from_="enter the twilio generated number",
        url="https://drive.google.com/drive/my-drive/samplw.xml"
    )
