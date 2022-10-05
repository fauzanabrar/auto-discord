from twocaptcha import TwoCaptcha

url = 'https://cdn.discordapp.com/attachments/1025838862649540629/1027169472798277663/captcha.png'

def solveChaptcha(url):
    solver = TwoCaptcha('d48130f88087c7b46fae7ef52dff8f6a')
    url = 'https://cdn.discordapp.com/attachments/1025838862649540629/1027169472798277663/captcha.png'
    result = solver.normal(url, caseSensitive=1)

    return result['code']

print(solveChaptcha(url))