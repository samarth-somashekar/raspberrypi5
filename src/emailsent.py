import yagmail # type: ignore

# Read password from hidden file
with open("/home/smrth/.local/share/.email_password", "r") as f:
    password = f.read().strip()

# Set up yagmail SMTP client
yag = yagmail.SMTP("rapberrypi28@gmail.com", password)

# Send email
yag.send(
    to="tejaswibr@gmail.com",
    subject="henge email sent",
    contents="hello this is samarth's raspberrypi here"
)

print("Email sent")

