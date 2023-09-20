FirstName = input("What is your Firstname ")
LastName = input("What  is your LastName ")
Username = input("HEY give your username")
saved_password = "12345"
password = input("Type your password")
print("So your fullname was", FirstName, LastName)
Fullname = FirstName + LastName
print("This is your Username ", Username)
email = Fullname+"@gmail.com"
print("Your email generate by us was ", email)
print(saved_password==password)