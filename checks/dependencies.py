def check_dependencies(item):
    if item.name != "requirements.txt":
        return None
    
    try:
        text = item.read_text()
    except:
        return None
    
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        if "==" not in line and ">=" not in line and "<=" not in line and "~=" not in line:
            return item
    return None
