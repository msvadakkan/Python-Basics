n=int(input())
if(n>=10):
    s=int(n/2000)
    n=n-(s*2000)
    if(s!=0):
        print("2000 ....",s)
    s=int(n/500)LanguageLanguage
    n=n-(s*500)
    if(s!=0):
        print("500 ....",s)
    s=int(n/100)
    n=n-(s*100)
    if(s!=0):
        print("100 ....",s)
    s=int(n/50)
    n=n-(s*50)
    if(s!=0):
        print("50 ....",s)
    s=int(n/20)
    n=n-(s*20)
    if(s!=0):
        print("20 ....",s)
    s=int(n/10)
    n=n-(s*10)
    if(s!=0):
        print("10 ....",s)
    s=int(n/5)
    n=n-(s*5)
    if(s!=0):
        print("5 ....",s)
    s=int(n/2)
    n=n-(s*2)
    if(s!=0):
        print("2 ....",s)
    s=int(n/1)
    n=n-(s*1)
    if(s!=0):
        print("1 ....",s)
else:
    print("error: amount should be greater than 10")
