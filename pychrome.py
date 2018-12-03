import PyChromeDevTools as pcd
import time
import subprocess

DEFAULT_ARGS = ('--disable-translate', '--disable-extensions', '--disable-background-networking',
                '--safebrowsing-disable-auto-update', '--disable-sync', '--metrics-recording-only',
                '--disable-default-apps',
                '--mute-audio', '--no-first-run', '--no-default-browser-check', '--disable-plugin-power-saver',
                '--disable-popup-blocking', '--disable-background-timer-throttling', '--disable-breakpad',
                '--disable-dev-shm-usage', '--disable-hang-monitor', '--disable-client-side-phishing-detection',
                '--disable-ipc-flooding-protection', '--disable-prompt-on-repost',
                '--disable-renderer-backgrounding',
                '--password-store=basic', '--use-mock-keychain', '--disable-infobars', '--process-per-tab',
                'about:blank')


def wait_dom_complete(chrome):
    while chrome.Runtime.evaluate(expression="document.readystate === 'complete'")['result']['result']['value']:
        return
    else:
        time.sleep(0.15)


CHROME_PROCESS = None


def launch(path, port=9222, open_dev_tools=False, incognito=False):
    args = [path, '--remote-debugging-port=' + str(port)]
    args = args + list(DEFAULT_ARGS)
    CHROME_PROCESS = subprocess.Popen(args=args)


# chrome = pcd.ChromeInterface(host='127.0.0.1', port=9222)
# chrome.Network.enable()
# chrome.Page.enable()
# chrome.Security.setIgnoreCertificateErrors(ignore=True)
# navigate_result = chrome.Page.navigate(url='https://cx.zfgjj.cn/dzyw-grwt/index.do')
# wait_dom_complete(chrome)
# chrome.Runtime.evaluate(expression='alert(1);')

if __name__ == '__main__':
    launch(path='/Users/wangchao/.cdp4j/chromium-605198/Chromium.app/Contents/MacOS/Chromium')
