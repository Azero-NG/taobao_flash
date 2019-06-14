from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.close()
wait = WebDriverWait(driver, 10)
def order(id,skuId):
    driver.get("https://detail.tmall.com/item.htm?id=%s&skuId=%s"%(id,skuId))
    driver.find_element_by_css_selector('#J_LinkBuy').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="提交订单"]'))).click()

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--proxy-server=http://" + "127.0.0.1" + ":" + '8080');
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()
driver.get("https://login.taobao.com/member/login.jhtml")
# 获取图片
driver.find_element_by_css_selector('.qrcode-img > img').get_attribute('src')








driver.find_element_by_css_selector('#J_Quick2Static').click()
driver.find_element_by_css_selector('#TPL_username_1').send_keys("a酒久久久")
driver.find_element_by_css_selector('#TPL_password_1').send_keys("amd:ryzen:1800x")
slide = driver.find_element_by_css_selector('.btn_slide')
action = ActionChains(driver)
action.click_and_hold(slide).perform()
action.reset_actions()
action.move_by_offset(298, 0).perform()
