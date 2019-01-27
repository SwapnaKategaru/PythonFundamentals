import urllib


def read_text():
    quotes = open("C:\Users\Raj\Desktop\sample_text.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()

    if "true" in output:
        print "Profanity Alert!"
    elif "false" in output:
        print "This document has no curse words."
    else:
        print "There is an error reading the document."


read_text()
