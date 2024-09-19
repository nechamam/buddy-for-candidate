import re

def clean_markdown(text):
    # Convert Markdown bold to HTML bold
    text = re.sub(r'(\*\*|__)(.*?)\1', r'<b>\2</b>', text)
    # Convert Markdown headers to HTML headers
    text = re.sub(r'^\s*###\s+(.*)', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*##\s+(.*)', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*#\s+(.*)', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    # Convert Markdown lists to HTML lists
    text = re.sub(r'^\s*-\s+(.*)', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+(.*)', r'<li>\1</li>', text, flags=re.MULTILINE)
    # Convert Markdown links to HTML links
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)
    # Replace newlines with <br> tags
    text = text.replace('\n', '<br>')
    return text