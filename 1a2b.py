import random 
list = [n for n in range(10)]
answer = random.sample(list,4)
print(answer)
def  abab(string) :
    a=0
    b=0    
    for n in range(4):
        if int(string[n]) == answer[n]:
            a+=1
        elif int(string[n]) in answer :
            b+=1
    print(a,"a",b,"b")
    return a 


xxx=input("請輸入數字：")
guess = str(xxx) 
while(abab(guess) != 4):
    xxx=input("請輸入數字：")
    guess = str(xxx) 
print("恭喜！！")




