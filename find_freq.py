# find the freq of occurences of any given word

def find_freq(book):
    book_dict = {}
    var_list = book.split()
    for var in var_list:
        if var not in book_dict:
            book_dict[var] = 1
        else:
            book_dict[var] += 1
    return book_dict

sentence = '''If you have a branch set up to track a remote branch
(see the next section and Chapter 3 for more information),
you can use the git pull command to automatically fetch
and then merge a remote branch into your current branch.
This may be an easier or more comfortable workflow for you;
and by default, the git clone command automatically sets up
your local master branch to track the remote master branch
(or whatever the default branch is called) on the server you
cloned from. Running git pull generally fetches data from the
server you originally cloned from and automatically tries to
merge it into the code you¡¯re currently working on.
'''
print find_freq(sentence)
