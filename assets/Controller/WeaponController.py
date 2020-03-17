from assets.Model.WeaponModel import Weapon

class WeaponController:
    def __init__(self):
        self.weapon =  Weapon()
        pass

    def UpdateParams(self, param: {}):
        for k in param.keys():
            a = list(self.weapon.__dict__.keys())            
            if k in list(self.weapon.__dict__.keys()):
                self.weapon.UpdateParams(param)
                return True
            else:
                return False

    def ConfirmRegistration(self):
        if self.weapon.GenerateID():
            if self.weapon.GenerateQR():
                if self.weapon.SaveToJsonFile():
                    return True
        return False

    def GetQRCodeURL(self):
        return self.weapon.QRcodeURL