def search_summary(summary, query):
    lines = summary.split('\n')
    matched = [line for line in lines if query.lower() in line.lower()]
    return '\n'.join(matched) if matched else "No matching events found."