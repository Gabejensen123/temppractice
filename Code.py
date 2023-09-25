def main():

    infile = open("book of John text.txt", 'r')
    #this line tells the computer to open a book called and get ready 
    #open the file, MUST USE DOUBLE QUOTATIONS - READ FROM THE FILE 
    #how to read to a file, name it with DOUBLE QUOTATIONS, and to be safe make sure it is in the file you are working in 
    #not in the parent folder


    counter = {#here, we're getting ready to count some special words in the book
         #we are starting with a count of zero for each word
    "Father": 0,
    "God": 0,
    "Christ":0,
    "Spirit":0,
    "spirit":0,
    "life":0,
    "man":0
    }
    
#count the words in the file. 
    for rec in infile:#we are going to start reading the book one part at a time, like reading one page at a time. 
        words = rec.strip().split()# make sure that the record you are recording in the infile, is the same name that is being stripped and ripped
        #when we read a part of the book, we want to look at each word on that page. we put all the words in the list and make them on a page. 
        for word in words:#going through and reading one word at a time. 
            if word:# going through and checking if the value is null. if its blank or a value.
                if word in ["Father", "God", "Christ", "Spirit", "spirit", "life", "man"]:
                    #We have a list of special words we care about. This line checks if the word we're looking at is one of those special words.
                    if word in counter:#this connects the list and the counter
                        #We're keeping count of how many times we find each special word. This line checks if we have already started counting this word
                        counter[word] += 1
                        #If we have already started counting this word, we add 1 to the count. 
                        #It's like adding one more tally mark if we've seen the word before. If we haven't seen it before, we start counting it with 1.
                    else:
                        counter[word] = 1

    for word, count in counter.items(): #make sure that the counter is in the main loop that you are defining. s
#After we've read the whole book and counted all the special words, we want to show our count. 
#This line helps us go through our list of special words and the number of times we found each one
            print(f"{word}: {count}")
#Finally, we tell the computer to show us the special word and how many times we found it. 
#It's like showing our list of special words and the number of times each one appears in the book.

    infile.close()
#must close the file when writing to a new one. 
        
main()




