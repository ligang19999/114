import ssl
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
ssl._create_default_https_context = ssl._create_unverified_context
"""
pip install bs4
"""

def get_df(url):
    print(url)
    html = urlopen(url)
    html_text = bytes.decode(html.read())
    soup = BeautifulSoup(html_text, 'html.parser')
    blocks = soup.find('div','w list-main clearfix').find_all("li")

    result = []
    for block in blocks:
        mydict = OrderedDict()
        mydict['name'] = block.find("div", 'name').text
        mydict['pos']  = block.find("div", 'p').text
        mydict['dep']  = block.find("div", 'dep').text
        mydict['link'] = block.a['href']
        result.append(mydict)
    df = pd.DataFrame(result)
    return df

def url_to_df(key, urls):
    result = []
    for url in urls:
        mydf = get_df(url)
        result.append(mydf)
    result_df = pd.concat(result)
    result_df.reset_index(inplace = True)

    del result_df['index']
    result_df['college'] = key
    return result_df

if __name__ == '__main__':
    sci_urls = [
       "https://www.sustech.edu.cn/zh/colleges/mathematics.html#4",
       "https://www.sustech.edu.cn/zh/colleges/physics.html#5",
       "https://www.sustech.edu.cn/zh/colleges/chemistry.html#5",
       'https://www.sustech.edu.cn/zh/colleges/earth-and-space-sciences.html#4',
       'https://www.sustech.edu.cn/zh/colleges/department-of-statistics-and-data-science.html#2'
    ]
    engineer_urls = [
        'https://www.sustech.edu.cn/zh/colleges/mechanics-and-aerospace-engineering.html#5'
        "https://www.sustech.edu.cn/zh/colleges/mechanical-and-energy-engineering.html#5",
        "https://www.sustech.edu.cn/zh/colleges/materials-science-and-engineering.html#5",
        'https://www.sustech.edu.cn/zh/colleges/electronic-and-electrical-engineering.html#4',
        'https://www.sustech.edu.cn/zh/colleges/computer-science-and-engineering.html#3',
        'https://www.sustech.edu.cn/zh/colleges/ocean-science-and-engineering.html#4',
        'https://www.sustech.edu.cn/zh/colleges/biomedical-engineering.html#4',
        'https://www.sustech.edu.cn/zh/colleges/environmental-science-and-engineering.html#5',
        'https://www.sustech.edu.cn/zh/colleges/school-of-microelectronics.html#4',
        'https://www.sustech.edu.cn/zh/colleges/school-of-system-design-and-intelligent-manufacturing.html#2',

    ]
    bio_urls = [
        'https://www.sustech.edu.cn/zh/colleges/biology.html#5'
    ]
    medical_urls = [
        'https://www.sustech.edu.cn/zh/colleges/department-of-medical-neuroscience.html',
        'https://www.sustech.edu.cn/zh/colleges/department-of-pharmacology.html#2',
        'https://www.sustech.edu.cn/zh/colleges/department-of-biochemistry.html#2',
        'https://www.sustech.edu.cn/zh/colleges/department-of-human-cell-biology-and-genetics.html#2',
        'https://www.sustech.edu.cn/zh/colleges/school-of-public-health-and-emergency-management.html#2'
    ]
    business_urls = [
        'https://www.sustech.edu.cn/zh/colleges/finance.html#2',
        'https://www.sustech.edu.cn/zh/colleges/department-of-information-systems-and-management-engineering.html#3'
    ]
    art_urls = [
        'https://www.sustech.edu.cn/zh/colleges/centre-for-humanities.html#2',
        'https://www.sustech.edu.cn/zh/colleges/social-science-center.html#2',
        'https://www.sustech.edu.cn/zh/colleges/research-center-for-higher-education.html#2',
        'https://www.sustech.edu.cn/zh/colleges/center-for-language-education.html#2',
        'https://www.sustech.edu.cn/zh/colleges/art-center.html#2',
    ]

    research_urls = [
        'https://www.sustech.edu.cn/zh/colleges/international-center-for-mathematics.html#2'
        'https://www.sustech.edu.cn/zh/colleges/grubbs-institute.html#2',
        'https://www.sustech.edu.cn/zh/colleges/institute-for-quanfum-science-and-engineering.html#5',
        'https://www.sustech.edu.cn/zh/colleges/academy-for-advanced-interdisciplinary-sciences.html#5'
    ]

    other_urls = [
        'https://www.sustech.edu.cn/zh/colleges/political-education-and-research-center.html#2',
        'https://www.sustech.edu.cn/zh/colleges/sports-center.html#2',
        'https://www.sustech.edu.cn/zh/colleges/school-of-innovation-and-entrepreneurship.html'
    ]
    ############### dict ############
    urls_dict = {
        'science':  sci_urls,
        'engineer': engineer_urls,
        'bio':      bio_urls,
        'medical':  medical_urls,
        'business': business_urls,
        'art':      art_urls,
        'research': research_urls, 
        'others':   other_urls,
    }

    for key, urls in urls_dict.items():
        print("--- {} fetching ---".format(key))
        df1 = url_to_df(key, urls)
        df1.to_csv(key+".csv")
        print("--- {} fetched successfully ---".format(key))
