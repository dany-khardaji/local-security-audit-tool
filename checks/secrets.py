import re

def check_for_secrets(item, keywords):
    aws_pattern = r"AKIA[0-9A-Z]{16}"

    try:
        text = item.read_text()
    except:
        return None

    for keyword in keywords:
        if keyword in text.lower():
            return item
    
    # Flag anything matching an AWS access key pattern using regex
    if re.search(aws_pattern, text):
        return item
    
    return None
