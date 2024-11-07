import time 

while True:
    for i in range(0,5):
        text = "loading" + "."*i
        print(text, end="\r")
        time.sleep(0.5)
    print("loading" + " "*5, end="\r")
    time.sleep(0.5)
