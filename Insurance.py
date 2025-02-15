file_path = "Just in case.txt"


with open(file_path,'w') as personal_details:
    personal_details.write("My name is Yifan Lu")
    personal_details.write("\nI live in United States")
    personal_details.write("\nI'm a fast learner")

print("\nFile created!\n")


# read back in
with open(file_path,'r') as personal_details:
    my_details = personal_details.read().splitlines()
    my_name, my_place, my_extra = my_details

    print(my_name)
    print(my_place)
    print(my_extra)