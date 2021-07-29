from selenium import webdriver
from selenium.webdriver.support.select import Select

def _select_value(elm, val):
    dropdown = webdriver.find_element_by_id(elm)
    select_y = Select(dropdown)
    select_y.select_by_value(val)

if __name__ == '__main__':
    # options = Options()
    # options.add_argument('--headless')
    webdriver = webdriver.Chrome("/Users/ota/Downloads/chromedriver")

    webdriver.get("https://www.vaccine.mrso.jp/sdftokyo/VisitNumbers/visitnoAuth")


    # 市区町村コード
    webdriver.find_element_by_xpath('//*[@id="VisitnoAuthName"]').send_keys("")
    # 接種券番号
    webdriver.find_element_by_xpath('//*[@id="VisitnoAuthVisitno"]').send_keys("")
    # 生年月日
    _select_value('VisitnoAuthYear', '')
    _select_value('VisitnoAuthMonthMonth', '')
    _select_value('VisitnoAuthDayDay', '')

    # ボタンクリック
    webdriver.find_element_by_class_name("auth-btn").click()
    webdriver.find_element_by_class_name("btn-next").click()
    # 詳細ボタン
    print(webdriver.find_element_by_class_name("covid19_move_plan_detail"))

    for detail_btn in webdriver.find_elements_by_class_name("covid19_move_plan_detail"):
        url = detail_btn.get_attribute('href')
        webdriver.execute_script("window.open(arguments[0], '_blank')", url)
