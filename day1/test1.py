from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '14',
    'appPackage': 'com.nowcoder.app.florida',
    'appActivity': '.modules.splash.view.SplashActivity',
    'deviceName': '10AE3610TH0061U'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
