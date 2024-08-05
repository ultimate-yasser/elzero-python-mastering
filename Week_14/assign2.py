class User:

    def __init__(self, fname, sname, age, gender):
        self.fname = fname
        self.sname = sname
        self.age = age
        self.gender = gender

    def full_details(self):
        return(f"Hello {'Mr' if self.gender == 'Male' else 'Ms'}\
 {self.fname} {self.sname[0]}. [{40 - self.age}] Years To Reach 40")
        

user_one = User('Yasser', 'Salah', 18, 'Male')
print(user_one.full_details())
