from DrissionPage import Chromium
from DrissionPage.common import Keys
from DrissionPage import SessionPage

def download_url(url, path):
    page = SessionPage()
    save_path = path

    res = page.download(url, save_path)
    print(res)

def rename_file(name_ls, path = "./Data"):
    import os
    files = os.listdir(path)
    for index, file in enumerate(files):
        print(file)
        postion = file.split(".")[0].replace("OpenFile", "").split("_")
        print(postion)
        postion[0] = "0"
        postion_i = int(postion[-1])
        name = name_ls[postion_i]
        os.rename(os.path.join(path, file), os.path.join(path, "{}.pdf".format(name[0])))


def drissionmain(where = "Data"):
    # 启动或接管浏览器，并创建标签页对象
    browser = Chromium()
    tab = browser.latest_tab
    print(id(tab))
    # 跳转到登录页面
    tab.get('https://data.rmtc.org.cn/gis/DocfileList.html#')
    # tab.wait.load_start() 
    tab.wait(2)

    ele = tab.ele('x://*[@id="confirminfo"]/div[3]/a[1]')
    if ele is None:
        print("没有找到")
    else:
        ele.click(by_js=True)

    eles = tab.eles('x://*[@id="selection1"]/div/h5[*]/a')
    name_ls = []
    for index,ele in enumerate(eles):  # 筛选出显示的元素列表并逐个打印文本
        ele_str = ele.text
        download_name = list([ele_str[:8]])
        name_ls.append(download_name)
        download_url(ele.link, "./{}".format(where))
        # if index+1 > 0:
        #     break
    txt_path = "./name.txt"
    with open(txt_path, "w") as f:
        f.write(str(name_ls))
    return name_ls

if __name__ == '__main__':
    name_ls = drissionmain()
    rename_file(name_ls)