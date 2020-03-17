import json
import base64
import random
from assets.View.keyboards import mainKB, weaponCreationKB, manufacturersKb, weaponTypesKB
from assets.Controller.WeaponController import WeaponController


class MainView:
    def __init__(self, session, userId, event):
        self.vkID = userId
        self.session = session
        self.citizenID = None
        self.weaponCOntroller = WeaponController()
        self.inModelChoose = False

        pass

    def ParseEvent(self, event):
        text = event['text']
        a = text.split(' ')

        if 'payload' in event.keys():
            a = 0
            if "mainMenu" in json.loads(event['payload']):
                payload = json.loads(event['payload'])['mainMenu']
                if payload == 'зарегистрировать':
                    self.session.method('messages.send', {
                        'message': f'Меню регистрации оружия',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': weaponCreationKB
                    }) 
                    pass
                elif payload == 'Завершить':
                    return True
            elif 'weaponCreationMenu' in json.loads(event['payload']):
                menuOption = json.loads(event['payload'])['weaponCreationMenu']
                if menuOption == 'производитель':
                    self.session.method('messages.send', {
                        'message': f'Выберите производителя',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': manufacturersKb
                    }) 
                    pass
                elif menuOption == 'модель':
                    self.inModelChoose = True
                    self.session.method('messages.send', {
                        'message': f'Введите название модели',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000)
                    })
                    pass
                elif menuOption == 'тип':
                    self.session.method('messages.send', {
                        'message': f'Выберите тип оружия',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': weaponTypesKB
                    }) 
                    pass
                elif menuOption == 'подтвердить':
                    if self.weaponCOntroller.ConfirmRegistration():
                        self.session.method('messages.send', {
                            'message': f'Чип нового оружия',
                            'peer_id': self.vkID,
                            'random_id': random.randint(1, 10000000000000),
                            'keyboard': mainKB,
                            'attachment': self.weaponCOntroller.GetQRCodeURL()
                        })
                    a= 0
                elif menuOption == 'завершить':
                    a = 0
                pass
                


            elif 'manufacturer' in json.loads(event['payload']):
                manufacturer = json.loads(event['payload'])
                if self.weaponCOntroller.UpdateParams(json.loads(event['payload'])):
                    self.session.method('messages.send', {
                        'message': f'Параметр задан успешно',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': weaponCreationKB
                    }) 
                else:
                    self.session.method('messages.send', {
                        'message': f'Произошла ошибка, параметр не задан',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': weaponCreationKB
                    }) 
                pass
            elif 'type' in json.loads(event['payload']):
                type = json.loads(event['payload'])
                if self.weaponCOntroller.UpdateParams(type):
                    self.session.method('messages.send', {
                        'message': f'Параметр задан успешно',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': weaponCreationKB
                    }) 
                else:
                    self.session.method('messages.send', {
                        'message': f'Произошла ошибка, параметр не задан',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': weaponCreationKB
                    }) 
                pass
        elif self.inModelChoose:
            if self.weaponCOntroller.UpdateParams({'model': text}):
                self.inModelChoose = False
                self.session.method('messages.send', {
                        'message': f'Параметр задан успешно',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': weaponCreationKB
                    }) 
            else:
                self.inModelChoose = False
                self.session.method('messages.send', {
                    'message': f'Произошла ошибка, параметр не задан',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': weaponCreationKB
                }) 
        elif text.split(' ').__len__() == 1 and text.split('\n').__len__() == 1:
            try:
                # TODO: weapon QR parsing
                a = base64.b64decode(text)
                if len(a[len('TransferMoneyTo '):]) > 0:
                    id = int(a[len('TransferMoneyTo '):])
                    self.citizenID = id
                    self.session.method('messages.send', {
                        'message': f'Профиль гражданина\n\n{paylaod}',
                        'peer_id': self.vkID,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': mainKB
                    })                 
        
            except Exception as e:
                self.session.method('messages.send', {
                    'message': f'Неверный формат введенных данных',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': mainKB
                })   
                return True           
            pass
        else:
            self.session.method('messages.send', {
                    'message': f'Неверный формат введенных данных',
                    'peer_id': self.vkID,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': mainKB
                })  
            return True
        