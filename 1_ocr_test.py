import easyocr
import re

def transfer():
    result = '[[[hsufhaoiuhf北京大学]]]'
    a_list = re.findall(r'[\u4e00-\u9fa5]',result)
    print(a_list)

def ocr():
    reader = easyocr.Reader(
        ['ch_sim','en'],
        gpu = False,
        detect_network= 'craft',
        download_enabled= False,
        model_storage_directory= '/mnt/d/projectB/py/model/'
    )
    result = reader.readtext('https://mmbiz.qpic.cn/mmbiz_png/uIPoFMWGibHEUXqXeiaBfKdibpe55kr5vvggia3dpvzLGXRMXO3Phm0ArrQucfbx6RvGmCib5gX73AibG0GwImZhQASQ/640?wx_fmt=png')
    
    for i in result:
        print(i[1]+' '+str(i[2]))
        

ocr()

