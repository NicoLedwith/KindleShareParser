import sys
# import pprint
# pp = pprint.PrettyPrinter(indent=4)

def parse():
    with open(sys.argv[1], 'r') as f:   # open file whose name is passed in
        str = f.read()
    str = str.strip()                   #strip white space
    strings = str.split("Highlight: ")
    del strings[0]                      #delete everything before "Highlight: "
    i = 0;
    for string in strings:              # get rid of text after note-text
        strings[i] = string.split('{note-text}',1)[0]
        i += 1
    i = 0;
    for string in strings:              # delete text after 'Amazon'
        strings[i] = string.split('Amazon',1)[0]
        i += 1
    for s in strings:
        print(s + "\n")                 #print results line by line

parse()                                 # call function
