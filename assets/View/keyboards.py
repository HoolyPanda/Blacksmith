import json


mKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"зарегистрировать\"}",
                        "label": "Зарегестрировать"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"владелец\"}",
                        "label": "Добавить новго владельца"
                    },
                "color": "secondary"
            }
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"Завершить\"}",
                        "label": "Завершить"
                    },
                "color": "positive"
            }   
        ]
    ]
}


wcKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"weaponCreationMenu\":\"производитель\"}",
                        "label": "Производитель"
                    },
                "color": "secondary"
            }
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"weaponCreationMenu\":\"модель\"}",
                        "label": "Модель"
                    },
                "color": "secondary"
            }   
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"weaponCreationMenu\":\"тип\"}",
                        "label": "Тип"
                    },
                "color": "secondary"
            }   
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"weaponCreationMenu\":\"завершить\"}",
                        "label": "Завершить"
                    },
                "color": "negative"
            },    
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"weaponCreationMenu\":\"подтвердить\"}",
                        "label": "Подтвердить"
                    },
                "color": "positive"
            }
        ]
    ]
}


manKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"manufacturer\":\"ShoGun\"}",
                        "label": "ShoGun"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"manufacturer\":\"Volkov Sec.\"}",
                        "label": "Volkov Sec"
                    },
                "color": "secondary"
            }
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"manufacturer\":\"-\"}",
                        "label": "Дописать"
                    },
                "color": "secondary"
            }   
        ]
    ]
}


tKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"type\":\"Пистолет\"}",
                        "label": "Пистолет"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"type\":\"Пистолет-Пулемет\"}",
                        "label": "Пистолет-Пулемет"
                    },
                "color": "secondary"
            }
        ],    
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"type\":\"Автомат\"}",
                        "label": "Автомат"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"type\":\"Дробовик\"}",
                        "label": "Дробовик"
                    },
                "color": "secondary"
            }
        ],        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"type\":\"Тяжелый Пулемет\"}",
                        "label": "Тяжелый Пулемет"
                    },
                "color": "secondary"
            }
        ]
    ]
}

weaponTypesKB = json.dumps(tKB)
manufacturersKb = json.dumps(manKB)
weaponCreationKB = json.dumps(wcKB)
mainKB = json.dumps(mKB)