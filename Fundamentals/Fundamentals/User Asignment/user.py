class User:
    def __init__(self, first_name, last_name, email, age, rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.rewards_member = rewards_member
        self.gold_card_points = gold_card_points
        
        

#  PRINTS ALL OF THE USERS DETAILS ON SEPERATE LINES
    def display_info(self):
        print("==============")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("==============")
        return self

# METHOD CHANGES THE GOLD CARD POINTS AND MEMBER STATUS OF USER 
    def enroll(self):
        if self.rewards_member:
            print("User already a member")
            return self
        else: 
            self.rewards_member = True
            self.gold_card_points = 200
            return self
            # print(f"{self.rewards_member}\n{self.gold_card_points}")


#  THIS METHOD DECREASES THE USERS POINTS BY THE AMOUNT SPECIFIED

    def spend_points(self, amount):
        self.gold_card_points -= amount 
        print(f"{self.gold_card_points}")
        return self

User1 = User('Gary', 'Magill', 'garymagill22@gmail.com', '32')
User1.display_info().enroll().display_info().spend_points(100).display_info()


