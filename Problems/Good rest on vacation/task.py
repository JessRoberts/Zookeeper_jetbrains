days = int(input())
food = int(input())
flight = int(input()) * 2
duration = days - 1
hotel = int(input()) * duration
print((days * food) + flight + hotel)
