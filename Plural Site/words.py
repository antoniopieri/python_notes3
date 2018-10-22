from urllib.request import urlopen
def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:  # this binds the response to avariabled named story
        story_words = []  # emptry list which will hold all words of text
        for line in story:  # the response for http gives list so we must iterate for each list
            line_words = line.decode('utf-8').split()  # this decodes each line and also splits line into list of words
            for word in line_words:  # nested for loop, this loops over each word in the line
                story_words.append(word)  # The append() method appends a passed obj into the existing list.
    for word in story_words:
        print(word)



#print(__name__)#evaluates to '__main__' or the actual module name depending on how the enclosing module is being used


if __name__ =='__main__':
    fetch_words()

#to make a file that run as a script AND is able to be imported we must do the above.
#This enables us to import the module without unduly executing the function.