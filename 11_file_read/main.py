#同じフォルダに test.txt を作って、適当に文字入れる

with open("test.txt","r",encoding="utf-8")as file:
    content = file.read()
    print(content)