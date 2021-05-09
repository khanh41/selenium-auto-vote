import re
import time
from selenium import webdriver
# from fp.fp import FreeProxy
from bs4 import BeautifulSoup
from random import randint, choice
import string
from multiprocessing import Pool






start_time = time.time()

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(length))
    return result_str

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
	s = ''
	for c in input_str:
		if c in s1:
			s += s0[s1.index(c)]
		else:
			s += c
	return s

file1 = open('data/name.txt', 'r', encoding="utf-8")
lines = file1.readlines()
# lines = [ remove_accents(x.strip().lower().replace(" ","")) for x in lines ]
print("====================0=============================")

def runabc(domainemail):
    u = 0
    for nameemail in lines:
        file3 = open('data/'+domainemail+'.txt', 'r', encoding="utf-8")
        linesfile3 = file3.readlines()
        linesfile3 = [ x.strip() for x in linesfile3 ]
        u += 1
        if(u<60):
            continue

        tmpName = nameemail + "5"
        nameemail = remove_accents(nameemail.strip().lower().replace(" ","")) + "5"
        
        if(nameemail in linesfile3):
            print("da tao")
            continue
        
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver = webdriver.Chrome(executable_path="./chromedriver",options=op)
        driver.set_window_size(500, 500)
        print("====================1=============================")
        url = "https://my.vnexpress.net/authen/users/register"
        # url = "https://vnexpress.net/co-cau-868-nguoi-ung-cu-quoc-hoi-khoa-xv-4270659.html"
        driver.get(url)
        time.sleep(1)
        
        # time.sleep(2)
        # driver.find_element_by_id("myvne").click()
        # time.sleep(4)
        # driver.find_element_by_id("myvne_register_link").click()
        
        # exit()

        print("====================2=============================")
        driver.find_element_by_id("myvne_email_input").send_keys(nameemail+'@'+domainemail)
        driver.find_element_by_id("myvne_password_input").send_keys('123456')
        driver.find_element_by_id("myvne_button_register").click()
        time.sleep(1)

        # driver.refresh()
        # time.sleep(5)

        # print("====================2=============================")
        # driver.find_element_by_id("myvne_email_input").send_keys(nameemail+'@'+domainemail)
        # driver.find_element_by_id("myvne_password_input").send_keys(get_random_string(7))
        # driver.find_element_by_id("myvne_button_register").click()
        # time.sleep(3)
        # exit()

        file2 = open('data/'+domainemail+'.txt',"a")
        file2.write(nameemail+" \n")
        file2.close()

        n = 0
        while True:
            driver.get("https://generator.email/"+domainemail+"/"+nameemail)
            soup=BeautifulSoup(driver.page_source, 'lxml')
            # print(driver.page_source)
            time.sleep(3)
            print("====================3=============================")
            link = False
            for a in soup.find_all('a', href=True):
                if('https://my.vnexpress.net/users/active' in a['href']):
                    link = a['href']
                    print(link)
                    break
            status = False

            try:
                driver.get(link)
                time.sleep(3)
                status = True
            except:
                pass
            
            n += 1
            time.sleep(1)
            if(n == 3):
                break

            if(status):
                break
            
        
        time.sleep(2)

        m = 0
        while True:
            try:
                urlregis = "https://my.vnexpress.net/vi/authen/users/updateprofile?refer=register"
                driver.get(urlregis)
                driver.find_element_by_id("myvne_fullname_input").send_keys(tmpName)
                txtphone = '0935'+str(random_with_N_digits(7))
                driver.find_element_by_id("myvne_mobile_input").send_keys(txtphone)
                driver.find_element_by_id("myvne_address_input").send_keys('Việt Nam')
                time.sleep(2)
                driver.find_element_by_id("myvne_button_profile").click()
                time.sleep(2)
                print("====================4=============================")

                urlregis = "https://my.vnexpress.net/users/chi-tiet-tai-khoan"
                driver.get(urlregis)
                time.sleep(2)
                driver.find_element_by_id("btn_change_fullname").click()
                driver.find_element_by_id("txtFullname").send_keys(tmpName)
                driver.find_element_by_id("btn_save_fullname").click()
                time.sleep(2)

                urlvote = "https://vnexpress.net/nguyen-van-minh-duc-4267915.html"
                driver.get(urlvote)
                time.sleep(1)
                driver.find_elements_by_class_name("main-button.button-vote.like.vote_article_button.txt_vote_article")[0].click()
                time.sleep(2)
                print(time.time()-start_time)
                break
            except:
                m += 1
                if(m==4):
                    break

        driver.delete_all_cookies()
        time.sleep(3)
        driver.quit()




if __name__ == '__main__':
    with Pool(5) as p:
        listdomain = ["mexcool.com", "gmailsl.com", "furnitt.com", "ilvain.com", "acmta.com", "shinisetoriyose.net", "gmailvn.net", "morina.me", "luxmet.ru", "chambraycoffee.com", "p-response.com", "kuontil.buzz"]
        for fi in listdomain:
            o = open("data/"+fi+".txt", "a")
            o.write("11")
            o.close()
        p.map(runabc, listdomain)
