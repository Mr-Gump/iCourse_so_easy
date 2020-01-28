import selenium,time,json,re,requests
from selenium import webdriver

url = input('请输入URL')
driver = webdriver.Chrome()
para0 = url[-10:]
title_pattern = re.compile(r'title=.*(http.?://[^\s]*)\"')
content_pattern = re.compile(r'answer=true;.*(http.?://[^\s]*)\"')
choice_pattern = re.compile(r'answer=true;.*.content="\\u(.*?);')
Answers = {}

def write_html(dic):
    File = open(r'C:\Users\mi\Desktop\高等数学题库\第16周.html','w',encoding='utf-8')
    head = '''<html>
    <table border="1">
    <tr><td>序号</td><td>题目</td><td>答案</td>
    '''
    tail = '''</table>
    </html>
    '''
    File.write(head)
    count = 1
    for i in dic:
        line = '<tr><td>'+str(count)+'</td><td><img src= "'+i+'"/></td><td>'+'<img src= "'+dic[i]+'"/></td></tr>'
        File.write(line)
        count += 1
    File.write(tail)
    File.close()

def get_answer(param0,param1,cookie):
    data = {
        'callCount':'1',
        'scriptSessionId':'${scriptSessionId}190',
        'httpSessionId':'955ed742170d4ecc8d0d99638ea1ec94',
        'c0-scriptName':'MocQuizBean',
        'c0-methodName':'getQuizPaperDto',
        'c0-id':'0',
        'c0-param0':str(param0),
        'c0-param1':param1,
        'c0-param2':'true',
        'batchId':str(int((time.time())*1000))
    }
    headers ={
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    url = 'https://www.icourse163.org/dwr/call/plaincall/MocQuizBean.getQuizPaperDto.dwr'
    content = requests.post(url,headers=headers,data=data).text
    return content

def login():
    driver.get('https://www.icourse163.org/')
    button1 = driver.find_element_by_class_name("m-index-person-loginBtn")
    button1.click()
    time.sleep(4)
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)
    button2 = driver.find_element_by_class_name("tab0")
    button2.click()
    phone = driver.find_element_by_id('phoneipt')
    phone.send_keys('15545370759')
    time.sleep(0.5)
    pass_word = driver.find_elements_by_name('email')[1]
    pass_word.send_keys('Gan000803')
    time.sleep(1)
    login_button = driver.find_element_by_id('submitBtn')
    login_button.click()
    time.sleep(1)
    cookie = driver.get_cookies()
    jsonCookies = json.dumps(cookie)
    with open('jwc.json', 'w') as f:
        f.write(jsonCookies)
    with open('jwc.json','r',encoding='utf-8') as f:
        listCookies=json.loads(f.read())
    cookie = [item["name"] + "=" + item["value"] 
    for item in listCookies]
    cookiestr = '; '.join(item for item in cookie)
    return cookiestr


def get_param(url):
    driver.get(url)
    time.sleep(2)
    start_button = driver.find_element_by_class_name('u-btn-primary')
    start_button.click()
    time.sleep(2)
    submit_button = driver.find_element_by_class_name('j-submitBtn')
    submit_button.click()
    sure_button = driver.find_element_by_class_name('j-ok-txt')
    sure_button.click()
    time.sleep(2)
    url = driver.current_url
    para1 = re.search('aid=(.*)',url).group(1)
    return para1

cookie = login()


for i in range(10):
    para1 = get_param(url)
    content = get_answer(para0,para1,cookie)
    questions = re.findall(title_pattern,content)
    normal_answers = re.findall(content_pattern,content)
    check_answers = re.findall(choice_pattern,content)
    count = 0
    for check_answer in check_answers:
        if check_answer == '6B63\\u786E"':
            check_answers[count] = 'http://ku.90sjimg.com/element_pic/01/01/73/3456f3fb34ee6f8.jpg'
        else:
            check_answers[count] = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1578067787959&di=3bf41c1ef7a605e8b31126d740ee8a90&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_pic%2F01%2F02%2F36%2F2356f415bbeb1d6.jpg'
        count += 1
    answers = normal_answers+check_answers
    count = 0
    answer_dict = {}
    for i in questions:
        answer_dict[i] = answers[count]
        count += 1
    for answer in answer_dict:
        if answer not in Answers:
            Answers[answer] = answer_dict[answer]

driver.close()
write_html(Answers)
print('成功！')
time.sleep(2)
