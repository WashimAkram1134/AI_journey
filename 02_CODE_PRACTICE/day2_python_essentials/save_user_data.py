name=input("Enter your name please: ")
Age=input("Enter your age please: ")

with open("user_data.txt","w") as file:
    file.write(f"name:{name}\wn")
    file.write(f"Age:{Age}")
print("User data save sucessfully")