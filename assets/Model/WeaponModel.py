import pyqrcode
import base64
import vk_api
from vk_api import VkUpload 
import json
import random
import os

class Weapon:
    def __init__(self):
        self.manufacturer = ''
        self.model = ''
        self.type = ''
        self.owners = []    
        self.QRcodeURL = ''
        self.id = 0    
        pass

    def UpdateParams(self, param:{}):
        self.__dict__.update(param)
        pass

    def GenerateID(self):
        paramsDump = ''
        blacklist = ['owners', "QRcodeURL", 'id']
        for param in self.__dict__.keys():
            if self.__dict__[param] and param not in blacklist:
                paramsDump += f'{self.__dict__[param]}'
            elif not self.__dict__[param] and param not in blacklist:
                return False
        paramsDump += f'{random.randint(1,100000)}'
        self.id = hash(paramsDump)
        return True

    def GenerateQR(self):
        # TODO qr code generation
        try:
            payload = str(base64.b64encode(bytes(f'Weapon {str(self.id)}', 'utf-8')), 'utf-8')
            a = pyqrcode.create(payload)
            QRfile = f'./QRs/{str(self.id)}.png'
            a.png(QRfile, scale=8, module_color= [0, 0, 0, 255], background=[0xff, 0xff, 0xff])

            login = open('./login.cred', 'r').readline()
            password = open("./password.cred", 'r').readline()
            groupID = 193066072
            albumID = 271095205

            client = vk_api.VkApi(login, password)
            client.auth()
            u = VkUpload(client)
            a = u.photo(photos= QRfile, album_id= albumID, group_id= groupID, caption= f'{self.__dict__}')
            a = a[0]
            ownerId = a['owner_id']
            mediaId = a['id']
            self.QRcodeURL = f'photo{ownerId}_{mediaId}'
            return True
        except:
            return False
    
    def SaveToJsonFile(self):
        profile = open('./DB/' + str(self.id) + '.json', 'w+')
        dump = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        profile.write(dump)
        profile.close()
        return dump

    def LoadFromJson(self, id: int):
        a = 0
        for f in os.listdir('./DB/'):
            if f'{id}' in f:
                profile = open(f'./DB/{f}', 'r').read()
                profile = json.loads(profile)
                self.__dict__.update(profile)
                return True
        return False

    def AddNewOwner(self, id: int):
        self.owners.append(id)
        self.SaveToJsonFile()
        return True