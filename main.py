import scratchattach as sa
import time

session = sa.login("username", "password") #Returns a sa.Session object
cloud = session.connect_cloud("project_id") #replace with your project id
client = cloud.requests()

@client.request
def timeget(): #called when client receives request
    print("Ping request received")
    x = ("\nGMT: " + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
    return x #sends back 'pong' to the Scratch project

@client.event
def on_ready():
    print("Request handler is running")

client.start(thread=True) # thread=True is an optional argument. It makes the cloud requests handler run in a thread