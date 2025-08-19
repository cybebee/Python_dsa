import webbrowser

# Word to search
search_query = "strivekishan dsa day in life day wokring okay  "

# Create the Google search URL
url = f"https://www.youtube.com/search?q={search_query}"

print("its working okay ")

# Open in Google Chrome
# Optional: Set path to Chrome if default browser is not Chrome
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open(url)
