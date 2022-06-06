from enum import Enum

class CodeNMsgEnum(Enum):

    HOST_SIGN_UP_SUCCESS = (10, "註冊成功")
    HOST_SIGN_UP_FAIL = (11, "註冊失敗")    

    PET_ADD_SUCCESS = (20, "新增寵物資料成功!")
    PET_ADD_FAIL = (21, "新增寵物資料失敗!")

    def __new__(self, value, message):
        obj = object.__new__(self)
        obj._value_ = value
        obj.code = value
        obj.message = message

        return obj

    def get_dict(self, data = None , extra_msg = None):   
        if extra_msg:
            message = extra_msg
        else:
            message = self.message
                
        result = {
            "code": self.code,
            "message": message,
            "data": data
        }

        return result