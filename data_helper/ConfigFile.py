import os

class ConfigFile(object):
    def WriteConfig(self,items):
        with open('./config.ini','w+',encoding='utf-8') as config:
            for item in items:
                config.writelines(item+'\n')

    def ReadConfig(self):
        if os.path.exists('./config.ini')==False:
            return []
        with open('./config.ini','r+',encoding='utf-8') as config:
            items=config.readlines()
            return items

if __name__ == '__main__':
    cf=ConfigFile()
    items=['a:1',
           'b:2',
           'c:3']
    cf.WriteConfig(items)
    rc=cf.ReadConfig()
    for i in rc:
        print(i)

