ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# List
ft_list[1] = "World!"

# Tuple
ft_tuple = ft_tuple[:1:] + ("Belgium!",)

# Set
ft_set.remove("tutu!")
ft_set.add("Brussels!")

# Dictionary
ft_dict["Hello"] = "Campus 19!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
