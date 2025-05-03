from classroom import ClassRoom
from person import Student,Teacher
from subject import Subject
from school import School

school=School("KKG","Enayetpur")

eight=ClassRoom("Eight")
nine=ClassRoom("Nine")
ten=ClassRoom("Ten")
#add classroom
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)
#add student
rahim=Student("Rahim",eight)
kahim=Student("kahim",eight)
zahim=Student("zahim",nine)
xahim=Student("xahim",ten)
sahim=Student("sahim",ten)
school.student_addmisson(rahim)
school.student_addmisson(kahim)
school.student_addmisson(zahim)
school.student_addmisson(xahim)
school.student_addmisson(sahim)
#adding teacher
abul=Teacher("Abul")
bbul=Teacher("bbul")
kbul=Teacher("kbul")
#adding subject
bangla=Subject("Bangla",abul)
physics=Subject("physics",bbul)
biology=Subject("biology",kbul)
english=Subject("english",abul)
eight.add_subject(bangla)
eight.add_subject(english)
nine.add_subject(physics)
nine.add_subject(biology)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(physics)
ten.add_subject(biology)
eight.take_sem_final_exam()
nine.take_sem_final_exam()
ten.take_sem_final_exam()
print(school)
