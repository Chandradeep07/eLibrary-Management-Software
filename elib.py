import shutil
class Library:
    def __init__(self,name,address):
        pass
class Book:
    def __init__(self,title,ISBN,genre,author):
        self.title=title
        self.ISBN=ISBN
        self.genre=genre
        self.author=author
        self.list=[self.title,self.ISBN,self.genre,self.author]
    def display_catalog(self):
        return self.list
    def add_book(self):
        f = open(self.title+".txt" , "w+")
        f.close()
        # move the file
        shutil.move('C:\\Users\\pratyaksh\\Desktop\\SIH\\%s.txt'%(self.title),'C:\\Users\\pratyaksh\\Desktop\\SIH\\books')


class Account:
    def __init__(self,librarian,members):
        pass



# Book Catalog
book1=Book("Rich Dad Poor Dad", 9783161484100,"Self help book","Robert T. kiyosaki")
book2=Book("Core Python Programming", 9783161484100,"Computer","Dr. R. Nageswara Rao")

# book1.add_book()
book2.add_book()