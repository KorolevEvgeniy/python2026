def merge_student_data(student_id, *args,**kwargs):
    student_data = {}
    for key, value in args:  
        student_data[key] = value
        # student_data = {
        # 'name': 'Evgeniy',
        # 'course': 'Python'
        # }
        for key, value in kwargs.items():
            student_data[key] = value
            # student_data = {
            # 'name': 'Evgeniy',      
            # 'course': 'Advanced Python', 
            # 'city': 'Kazan'         
            # }
    return {student_id: student_data}

def call_merger(args_list, kwargs_dict):
    return merge_student_data(101, *args_list, **kwargs_dict)


result = merge_student_data(101, ("name", "Evgeniy"), ("course", "Python"), city="Kazan", course="Advanced Python")
print(result)

additional_info = [("age", 25), ("hobby", "cycling")]
extra_details = {"score": 95, "age": 26}

result = call_merger(additional_info, extra_details)
print(result)
