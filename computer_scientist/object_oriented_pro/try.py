class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


    def distance(self,a):
        """ Compute my distance from the origin """
        return "((self.x ** 2) + (self.y ** 2)) ** 0.5 " + a


    def reflex_x(self):
        ''' Compute reflex co-ordinate of x-axis '''
        if self.x >= 0:
            return (-self.x, self.y)
        elif self.x == 0:
            return (self.x, self.y)
        return (-self.x, self.y)


    def slope_from_origin(self):
        ''' Calculates slope from origin. '''
        return round(self.y / self.x, 2)


    def __str__(self):
        ''' Returns the value of object. '''
        return f"{self.x}, {self.y}"


class SMS_store:
    ''' Store messages '''

    def __init__(self):
        ''' messages as tuples '''
        self.message = []
        self.viewed_messages = []


    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        '''
        Makes a new SMS tuple, inserts after other messages
        in the store. When creating this message,
        its has_been_viewed status is set False.
        '''
        self.message.append((from_number, time_arrived, text_of_sms))
        self.viewed_messages.append(False)


    def message_count(self):
        ''' Returns number of messages. '''
        return len(self.message)


    def get_unread_indexes(self):
        ''' Returns number of unread messages. '''
        unread = []
        for i,read in enumerate(self.viewed_messages):
            if not read:
                unread.append(i)
        return unread


    def get_message(self, i):
        ''' Returns the message using index if it exists. '''
        try:
            self.viewed_messages[i] = True
            return self.message[i]
        except:
            return None


    def delete(self, i):
        ''' Deletes message using index. ''' 
        self.message.pop(i)
        self.viewed_messages.pop(i)


    def clear(self):
        ''' Deletes all the messages. '''
        self.message = []
        self.viewed_messages = []



class Rectangle:
    ''' Draw a rectangle. '''

    def __init__(self, pos, w, h):
        ''' pos refers to position of top-left corner,
            w for width and h for height. '''
        self.pos = pos
        self.w = w
        self.h = h


    def grow(self, dw, dh):
        ''' grow the rectangle by dw and dh '''
        self.w += dw
        self.h += dh


    def move(self, dx, dy):
        ''' move the rectangle by dx and dy. '''
        self.pos.x += dx
        self.pos.y += dy
    

    def area(self):
        ''' returns the area of rectangle. '''
        return self.w * self.h


    def flip(self):
        ''' flips the value of width and height of object. '''
        self.w, self.h = self.h, self.w


    def cord_rect(self):
        ''' returns the co-ordinates of the rectangle (all corners).'''
        rect = []
        rect.append((self.pos.x, self.pos.y))
        rect.append((self.pos.x+self.w, self.pos.y))
        rect.append((self.pos.x+self.w, self.pos.y+self.h))
        rect.append((self.pos.x, self.pos.y+self.h))
        return rect


    def contains(self, new_pos):
        ''' returns true if a certain point falls on the rectangle. '''
        self.new_pos = new_pos
        if self.pos.x <= self.new_pos.x and self.new_pos.x < self.pos.x + self.w:
            if self.pos.y <= self.new_pos.y and self.new_pos.y < self.pos.y + self.h:
                return True
        return False


def has_colided(rectangle1, rectangle2):
    ''' returns true if any two rectangle has collided. '''
    if rectangle1.area() <= rectangle2.area():
        cord = rectangle1.cord_rect()
        for x,y in cord:
            if rectangle2.contains(Point(x,y)):
                return True
        return False
    else:
        cord = rectangle2.cord_rect()
        for x,y in cord:
            if rectangle1.contains(Point(x,y)):
                return True
        return False



a = Rectangle(Point(0,0), 15,15)
b = Rectangle(Point(), 10, 10)
print(a.cord_rect())
print(b.cord_rect())
print(a.area())
print(b.area())
print(has_colided(a,b))


# inbox = SMS_store()
# inbox.add_new_arrival(9865678, 8.20, "hey bro you remember me? ")
# inbox.add_new_arrival(9865678, 8.20, "hey bro you remember me? ")
# inbox.add_new_arrival(9865678, 8.20, "hey bro you remember me? ")
# inbox.add_new_arrival(9865678, 8.20, "hey bro you remember me? ")
# inbox.add_new_arrival(9865678, 8.20, "hey bro you remember me? ")
# inbox.add_new_arrival(9865678, 8.20, "hey bro you remember me? ")


# num_msg = inbox.get_unread_indexes()
# num = inbox.get_unread_indexes()
# print(num)
# print(inbox.get_message(num[0]))

# num = inbox.get_unread_indexes()
# print(num)

# inbox.delete(0)

# i = inbox.get_unread_indexes()
# print(i)

# print(inbox.get_message(2))
# print(inbox.get_unread_indexes())


# print(inbox.message_count())
# inbox.clear()


# print(inbox.message_count())


# r = Rectangle(Point(0, 0), 10, 5)

# print(r.contains(Point(0, 0)))
# print(r.contains(Point(3, 3)))
# print(not r.contains(Point(3, 7)))
# print(not r.contains(Point(3, 5)))
# print(r.contains(Point(3, 4.99999)))
# print(not r.contains(Point(-3, -3)))
# print(r.contains(Point(0,0)))


