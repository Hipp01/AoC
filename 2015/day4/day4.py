import hashlib 

def secret():
    with open("input.txt") as f:
            lines = f.readlines()
    input = lines[0]
    zeros = '00000'
    i = 0
    while True :
        str2hash = input+str(i)  
        result = hashlib.md5(str2hash.encode()) 
        if result.hexdigest()[:5] == zeros:
            print(result.hexdigest())
            return i
        i += 1


def secret_6():
    with open("input.txt") as f:
            lines = f.readlines()
    input = lines[0]
    zeros = '000000'
    i = 0
    while True :
        str2hash = input+str(i)  
        result = hashlib.md5(str2hash.encode()) 
        if result.hexdigest()[:6] == zeros:
            print(result.hexdigest())
            return i
        i += 1



if __name__ == "__main__":
    print(secret())
    print(secret_6())