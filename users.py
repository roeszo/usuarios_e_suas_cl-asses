class User():
  def __init__(self, first_name, last_name, age, email, username ):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.email = email
    self.username = username

  def user_info(self):
    print("User infos")
    print("NAME: ", self.first_name.title(),  self.last_name.title() )
    print("AGE: ", str(self.age))
    print("EMAIL: ", self.email)
    print("USER: ", self.username)

  def greet_user(self):
    print("Be welcome: ", self.first_name.title(),  self.last_name.title()  )


user0 = User('Jon', 'Doe', 23, 'jondoe@mail.com', 'jonjond')
user1 = User('Mary', 'Jane', 26, 'mjparker@mail.com', 'mj97')


user0.user_info()
user0.greet_user()
print()

user1.user_info()
user1.greet_user()


#muito bom
