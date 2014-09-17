import nltk
from collections import defaultdict
from nltk.corpus import reuters
tokenizer = nltk.TreebankWordTokenizer()

def summarize(storyid):
    stopwords = ['a','an','and','are','as','at','be','but','by','for','if','in','into','is','it','no','not','of','on','or','s','such','t','that','the','their','then','there','these','they','this','to','was','will','with']
    text="".join(reuters.raw(storyid).split("\n"))
    dictW=defaultdict(int)
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    ls=sent_detector.tokenize(text.strip())
    for l in ls:
        tokens=tokenizer.tokenize(l)
        for token in tokens:
          if token.lower not stopwords:
              if token not in dictW:
                  dictW[token]=1
              else:
                dictW[token]+=1
    title=ls[:1]
    ls=ls[1:]
    MAX_SUMMARY_SIZE=int(0.20*len(ls))
    ls.sort(key=lambda s: sum((dictW[token] for token in tokenizer.tokenize(s))), reverse=1)
    ls= ls[:MAX_SUMMARY_SIZE]
    ls.sort(lambda s1, s2:text.find(s1)-text.find(s2))
    ls=title+ls
    print "".join(ls)
    print
    
stories=[]
for fil in reuters.fileids(['gas','income','jobs']):
    if "test" in fil and len(reuters.raw(fil))>2500:
        stories.append(fil)
for story in stories:
    summarize(story)
        



    

