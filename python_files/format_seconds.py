def convert_time(time):
    # get values
    h = time // 3600
    mins = (time - h * 3600) // 60
    secs = time % 60
    # convert to mm and ss
    if mins < 10:
        mm = f"0{mins}"
    else:
        mm = str(mins)
    if secs < 10:
        ss = f"0{secs}"
    else:
        ss = str(sec)
    
    return f"{h}:{mm}:{ss}"

seconds = 3665
print(convert_time(seconds))