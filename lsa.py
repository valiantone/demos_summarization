from nltk.corpus import reuters
from gensim import corpora, matutils
from scipy import linalg, sparse
list=reuters.fileids('jobs')
test=[]
train=[]
for l in list:
    if "test" in l:
        if len(reuters.words(l))>500:
            test.append(l)
    else:
        if len(reuters.words(l))>500:
            train.append(l)


def condensify(train):
    """
    Takes input either a string or a list of string
    Returns a list of all summaries;
    For a string returns a list with singleton document
    """
    summ_list = []
    if isinstance(train,string):
        train = [train]
    for t in train:
        summ=[]
        k=0
        #corpus = [dictionary.doc2bow(text) for text in texts]
        dictionary = corpora.Dictionary([w for w in reuters.sents(t)])
        corpus = [dictionary.doc2bow(w) for w in reuters.sents(t)]
        matrix = matutils.corpus2csc(corpus)
        #print matrix
        u,sigma,vt = sparse.linalg.svds(matrix)
        (k,l)= vt.shape
        while k>=1:
            if reuters.sents(t)[vt[k-1].argmax()] not in summ:
                summ.append(reuters.sents(t)[vt[k-1].argmax()])
            k-=1
        v=[]
        for s in summ:
            v.append(" ".join(s))
        summ = "".join(v)
        summ_list.append(summ)
    return (summ_list)
