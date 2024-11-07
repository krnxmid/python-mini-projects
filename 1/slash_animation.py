import time

def slash():
    while True:
        print("|", end="\r")
        time.sleep(0.1)
        
        print("/", end="\r")
        time.sleep(0.1)
        
        print("-", end="\r")
        time.sleep(0.1)
        
        
        print("\\", end="\r")
        time.sleep(0.1)
        
text = slash()
print(text)
