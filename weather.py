import urllib.request
from bs4 import BeautifulSoup


def location(text):
    if "東京" in text:
        return "/3/16/4410/13104/"
    elif "大阪" in text:
        return "/6/30/6200/27100/"
    elif "名古屋" in text:
        return "/5/26/5110/23100/"
    elif "福岡" in text:
        return "/9/43/8210/40130/"
    elif "札幌" in text:
        return "/1/2/1400/1100/"
    elif "横浜" in text:
        return "/3/17/4610/14100/"
    else:
        return "/9/43/8210/40130/"


# 今日の天気スクレイピング
def get_today_weather(place):
    # 対象のサイトURL
    url = "https://tenki.jp/forecast" + location(place)
    # インスタンス作成
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    # 対象の要素
    weather = soup.find_all("p", class_="weather-telop")
    temp = soup.find_all("dd", class_="high-temp temp")
    low_temp = soup.find_all("dd", class_="low-temp temp")
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", class_="left-style")
    basyo = soup.find_all("h2")

    title = basyo[0].getText()
    tenki = hini[0].getText() + "\n\n" + weather[0].getText()
    kion = "\n最高 " + temp[0].getText()
    low_kion = "  最低 " + low_temp[0].getText()
    rain1 = "\n\n降水確率\n00-06時  " + tds[0].getText()
    rain2 = "\n06-12時  " + tds[1].getText()
    rain3 = "\n12-18時  " + tds[2].getText()
    rain4 = "\n18-24時  " + tds[3].getText()

    a = title + tenki + kion + low_kion + rain1 + rain2 + rain3 + rain4
    return a


# 明日の天気スクレイピング
def get_tom_weather(place):
    # 対象のサイトURL
    url = "https://tenki.jp/forecast" + location(place)
    # インスタンス作成
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    # 対象の要素
    weather = soup.find_all("p", class_="weather-telop")
    temp = soup.find_all("dd", class_="high-temp temp")
    low_temp = soup.find_all("dd", class_="low-temp temp")
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", class_="left-style")
    basyo = soup.find_all("h2")

    title = basyo[0].getText()
    tenki = hini[1].getText() + "\n\n" + weather[1].getText()
    kion = "\n最高 " + temp[1].getText()
    low_kion = "  最低 " + low_temp[1].getText()
    rain1 = "\n\n降水確率\n00-06時  " + tds[4].getText()
    rain2 = "\n06-12時  " + tds[5].getText()
    rain3 = "\n12-18時  " + tds[6].getText()
    rain4 = "\n18-24時  " + tds[7].getText()

    b = title + tenki + kion + low_kion + rain1 + rain2 + rain3 + rain4
    return b


# print(get_today_weather("福岡"))
# print(get_tom_weather("福岡"))
