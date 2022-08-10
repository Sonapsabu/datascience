with open ("nj.txt","r")as f1:
    for str in f1:
        output=str.replace("hai","hello")
        print(output)
