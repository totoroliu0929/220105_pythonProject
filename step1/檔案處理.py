import json
import time
import datetime
print(time.localtime()[0])
print(time.localtime()[1])
print(time.localtime()[2])
print(datetime.date.today())

def 讀取json檔案():
    try:
        with open("test.json") as f:
            x = f.read()
            y = json.loads(x)
            print(y)
            y["c"]=19
            儲存json檔案(y)
    except FileNotFoundError:
        print("找不到這個檔案")

def 儲存json檔案(arr):
    import json
    try:
        with open("test2.json", "w") as f:
            z = json.dumps(arr)
            json.dump(z,f)
            #f.write(z)
    except FileNotFoundError:
        print("找不到這個檔案")

def 讀取檔案():
    try:
        with open("test.txt") as f:
            print(type(f))
            #print(f.read())
            for line in f:
                line = line.replace("\n","")
                print(line)
    except FileNotFoundError:
        print("找不到這個檔案")

def 儲存檔案():
    lotto=[1,2,3,4]
    with open("test.txt", "w") as f:
        for x in lotto:
            y = str(x)
            y += "\n"
            f.write(y)

讀取json檔案()
#讀取檔案()
#儲存檔案()