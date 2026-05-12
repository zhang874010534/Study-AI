def employee_set_id (list):
    for i in range(len(list)):
        list[i]['id'] = f"{i:03d}"
