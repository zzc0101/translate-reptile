import requests
from bs4 import BeautifulSoup
import pickle, time

# 加载 pickle 数据
def load_pickle_data():
    with open('contents.pkl', 'rb') as f:
        load_data = pickle.load(f)
    return load_data

current_unix_timestamp_int = int(time.time())

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    'cookie': "Imported_MUID=190A5641A43369113DDC44A7A5C368FE; MUID=2CD58FA5864865C80DCE9CCD870D64E6; MUIDB=2CD58FA5864865C80DCE9CCD870D64E6; ANON=A=686C927A7639099D9423290FFFFFFFFF; MUIDV=NU=1; _UR=QS=0&TQS=0; _TTSS_OUT=hist=WyJ6aC1IYW5zIl0=; MicrosoftApplicationsTelemetryDeviceId=6e6db2b7-b885-4912-be0a-18f155d25128; _HPVN=CS=eyJQbiI6eyJDbiI6MTMsIlN0IjoxLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjEzLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMywiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wMi0xN1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoyMywiVG9ibiI6MH0=; EDGSRCHHPGUSR=CIBV=1.1645.0; _tarLang=default=zh-Hans&newFeature=tonetranslation; mapc=rm=1; _TTSS_IN=hist=WyJlcyIsImVuIiwiYXV0by1kZXRlY3QiXQ==&isADRU=0; MMCASM=ID=DF9450DB826A49428C35D7513B4F2D98; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=8FB11F83624245128EA4C160AED18603&dmnchg=1; ABDEF=V=13&ABDV=13&MRNB=1716963552930&MRB=0; btstkn=bYLNnMjwpXxkmRG8V1Un%252B%252Bl2ggkOIoNO%252FXTzUlnHerOchf9JV5SE72aFW5v91HAiQPLHBQZ30M6W6BDHfUSElJpdp0Q5QthxGJFjFppBAIg%253D; SRCHUSR=DOB=20230401&T=1716970976000; WLS=C=d4e1d4f2481f8f57&N=%e6%ad%a3%e6%98%8c; _U=1pECBXLx_DWC-w_9VSIDXGXdoDEIT_d0ONWdnpayOeOfJdB7kyPgX091z74fy1Mw7HUgdCLiUzEuZSUrMEE8GJ98vzwN18l-90lmsBBclcehuLajV1JZiA09TIFGRr0UVdYxBko-YTsy-5ILeduAmYZ4LEdoRwd-eSFWKXU9fxyw7j4XTR9G31wxD5fa10rpmLkmP2t8J_IxAqCYyQ6VVlmRwKIwQoRUlIG0_OG7aKQQ; SRCHS=PC=U531; _Rwho=u=d&ts=2024-05-29; USRLOC=HS=1&ELOC=LAT=39.956424713134766|LON=116.2601089477539|N=%E6%B5%B7%E6%B7%80%E5%8C%BA%EF%BC%8C%E5%8C%97%E4%BA%AC%E5%B8%82|ELT=2|&CLOC=LAT=39.95642316776295|LON=116.26011183115178|A=733.4464586120832|TS=240529082420|SRC=W&BID=MjQwNTI5MTYyNDE3XzAyYjIwZjRiNGFmYmZlZTk1ZjIyMzY4OTAyZDY1MmNiYzNiYTUwMDc5YmQ3MjcwZTg5NDI4ZDliNThiNjg1MmY=; _C_ETH=1; GC=VEhfO3EIvMtvx0dpDUh-htV47l6S7pOe0EypqAJ3mLmQ37qcOgkwM47Z8hZsUT8s4GmGrstI_dZY50T6LjbMWQ; _RwBf=r=0&ilt=13&ihpd=1&ispd=0&rc=1450&rb=1450&gb=0&rg=0&pc=1447&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=12&l=2024-05-29T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=BINGCOPILOTWAITLIST&c=MR000T&t=173&s=2023-04-07T13:21:03.7866356+00:00&ts=2024-05-29T08:34:53.7713787+00:00&rwred=0&wls=2&wlb=0&lka=0&lkt=0&TH=&aad=0&wle=0&ccp=2&ard=0001-01-01T00:00:00.0000000&rwdbt=0001-01-01T16:00:00.0000000-08:00&rwflt=2023-09-19T07:57:44.2389901-07:00&cpt=0&mta=0&e=DTTFydHxodauHWOBasb2opz-duIIFa-hw_UZVnhiVnhHyBzpn4cA4QjYXNs5AXwSRqe_L_cL-PB_NZZq2NmlYyQyin7Z8bQIBgCW8-lho8Q&A=; _SS=SID=015064F1DB7A6EE620B2707FDAE86F6E&PC=U531&R=1450&RB=1450&GB=0&RG=0&RP=1447; dsc=order=BingPages; ipv6=hit=1716975296376; _EDGE_S=mkt=zh-CN&ui=zh-cn&SID=015064F1DB7A6EE620B2707FDAE86F6E; SNRHOP=I=&TS=; SRCHHPGUSR=SRCHLANG=zh-Hans&BRW=XW&BRH=M&CW=1920&CH=969&SCW=1905&SCH=2660&DPR=1.0&UTC=480&DM=0&IG=155F9B974F8E4D89A164810FA4AA788E&PV=10.0.0&PRVCW=1920&PRVCH=969&WTS=63852110384&HV=1716971816&BZA=0&EXLTT=31"
}

form_data = {
    "from": "en",
    "to": "zh-Hans",
    "token": "kmUxyUediVIEET_EvFOCRSyKcpw4eCpq",
    "key": current_unix_timestamp_int,
    "tryFetchingGenderDebiasedTranslations": True
}


# 目标URL
url = "https://cn.bing.com/ttranslatev3?isVertical=1&&IG=CAA5589357224E0FAA677149FE25313D&IID=translator.5025"

form_data['text'] = load_pickle_data()[1]

# 发起 POST 请求
response = requests.post(url, data=form_data)

# 检查请求是否成功
if response.status_code == 200:
    
    print(response)

    # 解析HTML
    # soup = BeautifulSoup(response.text, 'html.parser')

    # 查找网页标题
    # title = soup.title.string

    # 打印标题
    # print('Title:', title)
else:
    print('Failed to fetch the page with status code:', response.status_code)


