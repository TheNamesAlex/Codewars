def make_readable(seconds):
    hour = seconds // 3600
    seconds = seconds % (24 * 3600) 
    
    seconds %= 3600
    minutes = seconds // 60
    
    seconds %= 60
    
    return "%02d:%02d:%02d" % (hour, minutes, seconds) 