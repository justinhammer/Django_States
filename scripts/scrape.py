#!/usr/bin/env python
import urllib
import urllib2
from lxml import etree
import StringIO
import re, sys, os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import State

result = urllib.urlopen('http://www.50states.com/')

html = result.read()

parser = etree.HTMLParser()

tree = etree.parse(StringIO.StringIO(html), parser)

# "//*[@class='ar-hp-states-capitals-box'
href_xpath = "//*[@id='ar-full-homepage']/div/ul/li/a/@href"

filtered_html = tree.xpath(href_xpath)

links = [link for link in filtered_html if 'htm' in link]

for link in links:
    # state_name_pattern = "(?<=\W).*(?=.htm)"
    # state_name_search = re.search(state_name_pattern, link)
    # state_name = "%s" % state_name_search.group()
    #use the xpath to the abbreviation to get the abbreviation
    #use a get instead of a filter to find the state object

    # state_object = State.objects.get(name__icontains=state_name.strip('new').strip('nc').strip('vv').strip('north')).first()

    state_page = urllib.urlopen("http://www.50states.com/%s" % link)
    state_page_html = state_page.read()
    tree = etree.parse(StringIO.StringIO(state_page_html), parser)

    state_name_path = '//*[@id="content"]/div[1]/div[2]/div/div[1]/h1/text()'
    state_name_xpath_search_results = tree.xpath(state_name_path)
    # print tree.xpath(state_name_path)
    # print link

    if state_name_xpath_search_results:
        state_pattern = "(?<=\()(.*)(?=\))"
        state_search = re.search(state_pattern, state_name_xpath_search_results[0])
        state_abbrev = state_search.group()

        state_object = State.objects.get(abbrev=state_abbrev)

    state_population_xpath = "//*[@id='collapseQuick-Facts']/div/ul/li[6]/div/text()"
    state_population_string = tree.xpath(state_population_xpath)

    #How can I clean up this string so the regex is more simple?
    #Look at strip and replace to clean up this string
    # print state_population_string

    state_population_pattern = "\d+,\d+,\d+"
    cleaned_pop_string = re.search(state_population_pattern, '%s' % state_population_string)

    try:
        # print cleaned_pop_string.group()
        state_object.pop = cleaned_pop_string.group()
        state_object.save()

    except AttributeError, e:
        pass

    if state_name_xpath_search_results:
        state_map_link_xpath = '//*[@id="collapseGovernment"]/div/ul/li[2]/div/a/@href'
        state_map_link = tree.xpath(state_map_link_xpath)[0]

        state_map_page = urllib.urlopen(state_map_link)
        state_map_page_html = state_map_page.read()

    tree = etree.parse(StringIO.StringIO(state_map_page_html), parser)

    # print state_map_page_html

    image_link_xpath = '//*[@id="innerPage"]/img/@src'
    state_map_image = tree.xpath(image_link_xpath)[0]

    url = 'http://quickfacts.census.gov/%s' % state_map_image

    image_response = urllib2.urlopen(url).read()
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(image_response)

    try:
        state_object.state_map.save('map_img.gif', File(img_temp))
    except Exception, e:
        pass

# if state_name_xpath_search_results:
#     state_nickname_link_xpath = "//*[@id='collapseQuick-Facts]/div/ul/li[5]/div/a/@href"
#     print state_nickname_link_xpath
#     state_nickname_link = tree.xpath(state_nickname_link_xpath)[0]
#     print state_nickname_link

#     state_nickname_page = urllib.urlopen(state_nickname_link)
#     state_nickname_page_html = state_nickname_page.read()

#     tree = etree.parse(StringIO.StringIO(state_nickname_page_html), parser)










