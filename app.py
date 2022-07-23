import mechanicalsoup

url = "https://cit.ac.in/"
browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},  # Use the lxml HTML parser
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)
browser.open(url)

# Store 5 recent notice urls to list

links = browser.get_current_page().find("div",class_="noticeContent")
link_list = []
for index, link in enumerate(links.find_all('a',href=True)):
    link_list.append((link['href']))
    if index==4:
        break

# List of dates of publishing of notice

publish_dates=[]
dates = (browser.get_current_page().find_all("span", class_="block text-xs text-grey-dark"))
for index,d in enumerate(dates):
    publish_dates.append(d.text)
    if (index == len(link_list) - 1):
        break

# Storing date, title, notice_type

for index,link in enumerate(link_list) :
    print()
    print(publish_dates[index])
    
    browser.open(link)

    title = (browser.get_current_page().find("span",class_="block text-grey-darkest text-lg")).text
    print(title)
    
    notice_type=(browser.get_current_page().find("h1"))
    if (notice_type is None):
        notice_type = "NOTICE"
        print(notice_type)
    else:
        print(notice_type.text)