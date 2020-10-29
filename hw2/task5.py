from re import split as resplit

# task 5

text = 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, \
    totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta \
    sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia \
    consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, \
    qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi \
    tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima \
    veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea \
    commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam \
    nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'

def sentencesCount(text):
    sentCount = 0
    tokens = resplit(r'\. |! |\? ',text)
    for token in tokens: 
        if token[0].isupper(): sentCount += 1
    return sentCount
 
def wordCount(text, word):
    text = text.lower()
    word = word.lower()
    words = resplit(r' |\.|,|!|\?', text)
    return words.count(word)

def charCount(text,noWhiteSpases = False):
    if noWhiteSpases: 
        text = text.replace(' ', '')
    return len(text)

def firtsNChars(text, N):
    if len(text) <= N or len(text) == 0: return text
    end = N
    while text[end].isalpha() and end > 0: end -= 1
    return text[0:end] + '...'


def main():
    print('Sentences: ', sentencesCount(text))
    print('\'{:s}\' enteres {:d} time(s)'.format('quis', wordCount(text, 'quis')))
    print('Length: ', charCount(text))
    print('Length without whitespace: ', charCount(text, True))
    print('First {:d} chars:\n{:s}'.format(120,firtsNChars(text, 120)))

if __name__ == '__main__':
    main()