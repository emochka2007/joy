def app_split(text):
    """app_split"""
    splitted = []
    bracket_open = False
    inner_array = []
    temp_str = ""
    for i in text:
       if i != " ":
           if i == "]":
               splitted.append(inner_array)
               bracket_open=False
           elif bracket_open:
               inner_array.append(i)
           elif i == "[":
               bracket_open=True
           else: 
               temp_str = f"{temp_str}{i}" 
       if i == " " and not bracket_open:
           if temp_str != "":
               splitted.append(temp_str)
           temp_str = ""
    splitted.append(temp_str)