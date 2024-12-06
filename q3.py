class Student:
    def __init__(self,name):
        self.name = name
        self.clubs = []

    def join_club(self,club):
        if club not in self.clubs:
            self.clubs.append(club)
            club.add_member(self)

    def display_clubs(self):
        for club in self.clubs:
            print(club.name)
        else:
            return "This student has not joined any clubs."
           
class Club:
    def __init__(self,name):
        self.name = name
        self.member = []

    def add_member(self,student):
        if student not in self.member:
             self.member.append(student)

    def display_members(self):
        for student in self.member:
            print(student.name)
                     
        
student1 = Student("Zuruel") 
student2 = Student("David")  

club1 = Club("Robotics")
club2 = Club("Art Club")

student1.join_club(club1)
student2.join_club(club2)

print(f"{student1.name} belongs to ")
student1.display_clubs()

# club1.add_member(student1)
# club2.add_member(student2)

print(f"{club1.name}")
club1.display_members()