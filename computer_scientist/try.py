# def a(li):
#     print(li is h)
#     print(li == h)
#     li[1] = 4

# h = [1, 2]
# a(h)
# print(h)


# import turtle
# tess = turtle.Turtle()
# wn = turtle.Screen()
# alex = tess 
# alex.color("hotpink")
# alex.forward(50)
# wn.mainloop()


# this = ["hello", "bro"]
# that = ["hello", "bro"]
# print("test1:", this is that)
# this = that
# print("test2:", this is that)


n = [1,2,4,5,6,7,8,0,10,23,56,87]
lon = n[0]
for i in n:
    if i > lon:
        lon = i
print(lon)
