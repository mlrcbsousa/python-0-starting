ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# List
ft_list[1] = "World!"

# Tuple
temp_list = list(ft_tuple)
temp_list[1] = "Belgium!"
ft_tuple = tuple(temp_list)

# Set
ft_set.remove("tutu!")
ft_set.add("Brussels!")

# Dictionary
ft_dict["Hello"] = "Campus 19!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
