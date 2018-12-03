import PyChromeDevTools as pcd
import time


def wait_dom_complete(chrome):
    print(chrome.Runtime.evaluate(expression="document.readystate === 'complete'"))
    while chrome.Runtime.evaluate(expression="document.readystate === 'complete'")['result']['result']['value']:
        return
    else:
        print('-----')
        time.sleep(0.15)


chrome = pcd.ChromeInterface(host='127.0.0.1', port=9222)
chrome.Networ.enable()
chrome.Page.enable()
chrome.Runtime.enable()
chrome.Security.setIgnoreCertificateErrors(ignore=True)
navigate_result = chrome.Page.navigate(url='https://cx.zfgjj.cn/dzyw-grwt/index.do')
wait_dom_complete(chrome)
# chrome.Runtime.evaluate(expression='alert(1);')
