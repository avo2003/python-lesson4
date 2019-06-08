from bs4 import BeautifulSoup
with open ("ecologicalpyramid.html","r") as ecological_pyramid:
        soup=BeautifulSoup(ecological_pyramid,features="html.parser")
producer_entries = soup.find("ul")
next_producer_entries=producer_entries.find_next_sibling("ul")
previous_producer_entries = next_producer_entries.find_previous_sibling("ul")
primary_consumers = soup.find(id="primaryconsumers")
# print(producer_entries)
print(producer_entries.li.div.string)
print(next_producer_entries.li.div.string)
print(previous_producer_entries.li.div.string)
print(primary_consumers.li.div.string)
# tag_li = soup.find("li")
# print(type(tag_li))
# search_for_stringonly = soup.find(text="lion")
# print(search_for_stringonly)