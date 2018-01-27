#comment_file = 'E:\MSR 2018\Sentiment Analysis\_libreoffice-female.txt'
#comment_file = 'E:\MSR 2018\Sentiment Analysis\_libreoffice-male.txt'
#comment_file = 'E:\MSR 2018\Sentiment Analysis\_chromium-female.txt'
comment_file = 'E:\MSR 2018\Sentiment Analysis\_chromium-male.txt'
#comment_file = 'E:\MSR 2018\Sentiment Analysis\_omapzoom-female.txt'
#comment_file = 'E:\MSR 2018\Sentiment Analysis\_omapzoom-male.txt'
#comment_file = 'E:\MSR 2018\Sentiment Analysis\_android-female.txt'
#comment_file = 'E:\MSR 2018\Sentiment Analysis\_android-male.txt'
#comment_file = 'E:\MSR 2018\Sentiment Analysis\_ovirt-female.txt'
#comment_file = 'E:\MSR 2018\Sentiment Analysis\_ovirt-male.txt'

positive_file = 'E:\MSR 2018\Sentiment Analysis\_positive-words.txt'
negative_file = 'E:\MSR 2018\Sentiment Analysis\_negative-words.txt'

def main():
    commentFile = open(comment_file, 'r')
    comWordList = list(commentFile.read().split())
    comWordSet = set(comWordList)
    
    posFile = open(positive_file, 'r')
    posWordList = list(posFile.read().split())
    posWordSet = set(posWordList)
    
    negFile = open(negative_file, 'r')
    negWordList = list(negFile.read().split())
    negWordSet = set(negWordList)
    
    print("Number of Word in Comments:")
    print(len(comWordSet))
    
    print("\nTotal Positive Emotion: ")
    print(len(comWordSet.intersection(posWordSet)))
    
    print("\nTotal Negative Emotion: ")
    print(len(comWordSet.intersection(negWordSet)))
    
main()