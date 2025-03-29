class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def func(index, width, max_height):
            if index >= len(books):
                return books[max_height][1]
            # something with width here

            # place it next if we can
            curr_book = books[index]
            book_width = curr_book[0]
            book_height = curr_book[1]

        
            # nothing placed yet
            if max_height == -1:
                return func(index + 1, width - book_width, index)
            

            curr_book_with_max_height = books[max_height]
            tallest_height_on_row = curr_book_with_max_height[1]

            # we can place it
            if width - book_width >= 0:
                #either place it next row, or into the next in current row
                place = books[max_height][1] + func(index + 1, shelfWidth - book_width, index)
                if book_height > tallest_height_on_row:
                    max_height = index
                next_place = func(index + 1, width - book_width, max_height)
                return min(place, next_place)
            else:
                # must place it on next row
                return books[max_height][1] + func(index + 1, shelfWidth - book_width, index)
        return func(0, shelfWidth, -1)
                
