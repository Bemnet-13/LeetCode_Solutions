class Solution:
    def sortPeople(self, names, heights):
        height_book = list(zip(names, heights))

        def sort(book):
            return book[1]
        
        height_book.sort(key = sort, reverse = True)

        lst = []


        for pair in height_book:
            lst.append(pair(1))

        return lst
        