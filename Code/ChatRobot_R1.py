#-*- encoding:utf-8 -*-
'''
    1.Extract words from lrcs;
    2.Build a static lib of words;
    3.Chat with it through GUI or command line;
    e.g:
    Q:give me reason;
    A:

    
'''
# "答案"
def GiveMeAnswer():
    # similarity words
    simi_word = {"答案":1,"答":0.8,"想要":0.75,"需要":0.75,\
    "要":0.5,"期望":0.75,"渴求":0.8,"希望":0.6}
    # for i in simi_word:
    #     print(simi_word[i])
    

    
    print("this is the end of function")


if __name__ == "__main__":
    print("at least there is a word")
    GiveMeAnswer()