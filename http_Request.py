# -*- coding: utf-8 -*-

import requests
import json
import time

Predict_Text='中度贫血的原因和治疗'

start_time=time.time()


#实体提取
# r2=requests.post("http://172.18.0.63:8088/entity_yiliao",data=Predict_Text.encode('utf-8'))
#分类
r2=requests.get('http://172.16.13.119:8000/test_model?content=肾病综合征有哪些症状呢？&train_id=017a7ca0-4695-4c00-8e81-bfd15aa2ac9f&model_id=222')
# result=json.loads(r2.text)
# print(str(result['疾病有']))
# print(str(result['症状有']))


print(r2.text)

'''
print('药品：'+str(result['药品']))
print('疾病有：'+str(result['疾病有']))
print('疾病无：'+str(result['疾病无']))
print('诱因：'+str(result['诱因']))
print('体征有：'+str(result['体征有']))
print('体征无：'+str(result['体征无']))
print('检验结果：'+str(result['检验结果']))
print('检查结果有：'+str(result['检查结果有']))
print('检查结果无：'+str(result['检查结果无']))
print('手术：'+str(result['手术']))
print('生活习惯：'+str(result['生活习惯']))
print('症状有：'+str(result['症状有']))
print('症状无：'+str(result['症状无']))
end_time=time.time()
dif_time=end_time-start_time
print('总耗时：'+str(dif_time))
'''

