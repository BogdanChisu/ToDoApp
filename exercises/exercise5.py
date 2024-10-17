member_name = input("Add a new member: ")

file = open("members.txt", "r")
members = file.readlines()
file.close()

members.append(member_name)

file = open("members.txt", "w")
file.writelines(members)
file.close()
