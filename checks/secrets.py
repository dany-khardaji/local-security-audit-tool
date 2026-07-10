def check_for_secrets(item, keywords):
    try:
        text = item.read_text()
    except:
        return None
    
    for keyword in keywords:
        if keyword in text.lower():
            return item
    return None