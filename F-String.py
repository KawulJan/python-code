message="this is an example"
print(f"{message:<30}")
print(f"{message:>30}")
print(f"{message:^30}")
print(f"{message:*<30}")
print(f"{message:*>30}")
print(f"{message:*^30}")

name = input("enter your name: ")
messageLine1=f"welcome {name:.10}"
messageLine2=f"{name:.10}, it is our pleasure"
messageLine3="to see you join us"
print(f"{messageLine1:^30}")
print(f"{messageLine2:^30}")
print(f"{messageLine3:^30}")