from selenium import webdriver

def get_chrome_driver():
    # 初始化Chrome浏览器
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 如果不需要可视化，可以使用无头模式
    options.add_argument('--incognito')
    options.add_argument('--disable-gpu')  # 避免某些系统问题
    # options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"' )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    return driver
