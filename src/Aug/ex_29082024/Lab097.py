squares = [1, 4, 9, 16, 25]
# List is Mutable in nature
# mutable - change -

squares[3] = 64
print(squares)  # [1, 4, 9, 64, 25]

# Tuple - Collection of Items
my_tuple = (1, 4, 9, 16, 25)
# my_tuple[3] = 64 # Immutable in nature
print(my_tuple)  # 'tuple' object does not support item assignment

shopping_list_wife = ["bread", "butter", "paneer"]
shopping_list_wife[2] = "milk"
print(shopping_list_wife)

# Real world project
# thetestingacademy.com, sdet.live
my_tuple = ("tta.com", "sdet.live")
my_api_list = list(my_tuple) # conversion
print(my_api_list)
my_api_list = tuple(my_api_list) # conversion
print(my_api_list)


# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])