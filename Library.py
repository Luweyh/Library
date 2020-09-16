# Author: Luwey Hon
# Description:  This program represent a library. It consist of a Libraryitem class
# which has Book, Album, and Movies as its subclasses since these are items that
# can be checked out in a library. It also has a Patron class which has Patron's
# information for checking out items and paying. It also consist of a library class
# that has all the information about the library and all the things they can do in
# the library.

class LibraryItem:
    """ Represents the library items """

    def __init__(self, library_item_id, title):
        """ Initializes parts of the library items """
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0

    def get_library_item_id(self):
        """ Gets Library Item ID """
        return self._library_item_id

    def get_title(self):
        """ Get the Title """
        return self._title

    def get_location(self):
        """ Gets location """
        return self._location

    def get_checked_out_by(self):
        """ Gets the checked out by """
        return self._checked_out_by

    def get_requested_by(self):
        """ Gets the requested by"""
        return self._requested_by

    def get_date_checked_out(self):
        """ Gets the date checked out by"""
        return self._date_checked_out

    def set_location(self, location):
        """ Sets the location of the item"""
        self._location = location

    def set_checked_out_by(self, patron):
        """ Sets the patron that checked out """
        self._checked_out_by = patron

    def set_requested_by(self, patron):
        """ Sets the patron that requested it """
        self._requested_by = patron

    def set_date_checked_out(self, date):
        """ Sets the date checked out"""
        self._date_checked_out = date


class Book(LibraryItem):
    """ Represents the book in the Library"""

    def __init__(self, library_item_id, title, author):
        """ Initializes the ID, title, and author of book """
        super().__init__(library_item_id, title)
        self._author = author

    @staticmethod
    def get_check_out_length():
        """ Gets the check out length for a book"""
        return 21

    def get_author(self):
        """ Gets the author of the book """
        return self._author

    def set_author(self, author):
        """ Sets the author of the book"""
        self._author = author

class Album(LibraryItem):
    """ Represents the albulms in the library"""

    def __init__(self, library_item_id, title, artist):
        """ Initializes the ID, title, and author of album"""
        super().__init__(library_item_id, title)
        self._artist = artist

    @staticmethod
    def get_check_out_length():
        """ Check out length for an album"""
        return 14

    def get_artist(self):
        """ Gets the artist of the album"""
        return self._artist

    def set_artist(self, artist):
        """ Set the artist name of the album"""
        self._artist = artist


class Movie(LibraryItem):
    """ Represent the Movies in the library"""

    def __init__(self, library_item_id, title, director ):
        """ Initializes the ID, title, and director for the movie """
        super().__init__(library_item_id, title)
        self._director = director

    @staticmethod
    def get_check_out_length():
        """ Check out length of movies"""
        return 7

    def get_director(self):
        """ Get the director name of the movie """
        return self._director

    def set_director(self, director):
        """ Set the director name of the movie """
        self._director = director


class Patron:
    """ Represents the patron for the library """

    def __init__(self, patron_id, name):
        """ Initializes the Patron's ID and name """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """ Gets the patron's ID """
        return self._patron_id

    def get_name(self):
        """ Gets the patron's name"""
        return self._name

    def get_check_out_items(self):
        """ Gets the checked out items """
        return self._checked_out_items

    def get_fine_amount(self):
        """ Gets the fine amount """
        return self._fine_amount

    def amend_fine(self, amount):
        """ Sets the fine amount """
        self._fine_amount += amount

    def add_library_item(self, item):
        """ Adds the item to the checked out items"""
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """ Removes the library item from the checked out items """
        self._checked_out_items.remove(item)


class Library:
    """ Represents the library """

    def __init__(self):
        """ has the library holdings, members, and current date"""
        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_holdings(self):
        """ Gets the items in the library """
        return self._holdings

    def get_members(self):
        """ Gets the member in the library """
        return self._members

    def get_current_date(self):
        """ Gets the current date """
        return self._current_date

    def set_current_date(self, date):
        """ Sets the current date """
        self._current_date = date

    def add_library_item(self, item):
        """ Adds the item into the library's holdings"""
        self._holdings.append(item)

    def add_patron(self, patron):
        """ Adds the patron to a lit of members """
        self._members.append(patron)

    def get_library_item_from_id(self, id):
        """ Gets the library object from the id """

        # iterates through the library items
        for item in self._holdings:

            # finds the item based off of ID
            if item.get_library_item_id() == id:
                return item

        # no item is found by the given ID
        return None

    def get_patron_from_id(self, id):
        """ Finds the patron based off ID """

        # iterates through the members list
        for patron in self._members:

            # finds the patron based off of ID
            if patron.get_patron_id() == id:
                return patron

        # no patron is found by the given ID
        return None

    def check_out_library_item(self, patron_id, item_id):
        """ Checks out the library item """

        # finds the patron based off of ID
        patron = self.get_patron_from_id(patron_id)

        # finds the library item based off ID
        library_item = self.get_library_item_from_id(item_id)

        # if patron is not found based off the ID
        if patron is None:
            return "patron not found"

        # if the library item is not found based off ID
        elif library_item is None:
            return "item not found"

        # if the item is checked out
        if library_item.get_location() == "CHECKED_OUT":
            return "item already checked out"

        # if the item is on hold by another person
        elif library_item.get_location() == "ON_HOLD_SHELF" and library_item.get_requested_by() != patron:
            return "item on hold by other patron"

        else:
            # update the new patron that checks it out
            library_item.set_checked_out_by(patron)

            # updates the date checked out
            library_item.set_date_checked_out(self.get_current_date())

            # updates the item location to checked out
            library_item.set_location("CHECKED_OUT")

            # puts the item off hold if the patron requested it before
            if library_item.get_requested_by() == patron:
                library_item.set_requested_by(None)

            #  adds the specified library item to checked_out_items
            patron.add_library_item(library_item)

        return "check out successful"

    def return_library_item(self, item_id):
        """ returns the library item """

        # finds the library item based off id
        item = self.get_library_item_from_id(item_id)

        # if the item is not found in the holdings
        if item is None:
            return "item not found"

        # if the item is not checked out
        elif item.get_checked_out_by() is None:
            return "item already in library"

        # removes the Patron's checked out item
        patron = item.get_checked_out_by()
        patron.remove_library_item(item)

        # checks if the item is requested
        if item.get_requested_by() is None:

            # if it is not on hold, put on regular shelf
            item.set_location("ON_SHELF")

        else:
            # if it is on hold, put item to hold shelf
            item.set_location("ON_HOLD_SHELF")

        # update the library item checked out by
        item.set_checked_out_by(None)

        return "return successful"

    def request_library_item(self, patron_id, item_id):
        """ Request the library item """

        # gets the patron based on ID
        patron = self.get_patron_from_id(patron_id)

        # gets the item based on ID
        item = self.get_library_item_from_id(item_id)

        # if the patron is not a library member
        if patron is None:
            return "patron not found"

        # if the item is not found
        elif item is None:
            return "item not found"

        # if the item is on the hold shelf
        elif item.get_location() == "ON_HOLD_SHELF":
            return "item already on hold"

        # makes the item requested by the patron
        item.set_requested_by(patron)

        # sets the item location to on hold if it is on the regular shelf
        if item.get_location() == "ON_SHELF":
            item.set_location("ON_HOLD_SHELF")

        return "request successful"

    def pay_fine(self, patron_id, owe):
        """ Pays the Patron's fine"""

        # get the patron based off id
        patron = self.get_patron_from_id(patron_id)

        # if the patron is not found
        if patron is None:
            return "patron not found"

        # paying the fines on account
        patron.amend_fine(-owe)

        return "request successful"

    def increment_current_date(self):
        """ Increases the current of the checked item """

        # increment the date by 1
        self._current_date += 1

        # iterates through the members
        for patron in self._members:

            # iterates through the Patron's checked out item
            for item in patron.get_check_out_items():

                # Amend 10 cents for each item that is overdue
                if self._current_date - item.get_date_checked_out() > item.get_check_out_length():
                    patron.amend_fine(.10)



if __name__ == "__main__":
    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_patron(p1)
    lib.add_patron(p2)

    lib.check_out_library_item("bcd", "456")
    loc = a1.get_location()
    lib.request_library_item("abc", "456")
    for i in range(57):
        lib.increment_current_date()  # 57 days pass
    p2_fine = p2.get_fine_amount()
    lib.pay_fine("bcd", p2_fine)
    lib.return_library_item("456")





