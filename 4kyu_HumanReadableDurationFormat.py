def format_duration(seconds):
    if seconds == 0:
        return 'now'
    else:
        y = seconds // (365*24*60*60)
        d = seconds // (24*60*60)
        h = seconds // (60*60)
        m = seconds // (60)
        s = seconds % 60
        
        if d >= 365:
            d %= 365 
        if h >= 24:
            h %= 24
        if m >= 60:
            m %= 60
        if s >= 60:
            s %= 60
            
        times = {'years':y,'days':d,'hours':h,'minutes':m,'seconds':s}
        
        result = ''
        for key in times.keys():
            if times[key] != 0:
                if times[key] == 1:
                    result += str(times[key]) + ' ' + key[:-1] + ', '
                else:
                    result += str(times[key]) + ' ' + key + ', '
        
        result = result[:-2]
        
        k = result.rfind(',')
        if k == -1:
            return result
        else:
            result = result[:k] + ' and' + result[k+1:]
            return result