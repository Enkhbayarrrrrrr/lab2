course_id=input("хичээлийн код:")
course_name=input("хичээлийн нэр:")
credit=input("хичээлийн кредит:")
madlib="энэ хичэлийн код нь {}".format(course_id).upper()+\
",хичээлийн нэр:{}".format(course_name).title()+\
"бөгөөд уг хичээл нь {}".format(credit)+ "кредитийн хичээл юм."
print(madlib.lower())
print(madlib.lower())