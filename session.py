from datetime import datetime
from  datetime import time
from system_en import Mains
count = 2
serial_no = 108
trigger_up = 1
trigger_dwn = 1
if (trigger_dwn == 1 and trigger_up == 1):
    count = count + 1
class Session:

    # instance attribute
    def __init__(self, date, time, rpm_up, rpm_dwn, serial_no, create=0, create_month=0, create_day=0, create_h=0, create_m=0,
                 create_s=0):
        self._create = create
        self._create_month = create_month
        self._create_day = create_day
        self._create_h = create_h
        self._create_m = create_m
        self._create_s = create_s

        self.rpm_up = trigger_up
        self.rpm_dwn = trigger_dwn
        self.time = datetime.date(date)
        self.date = datetime.now()
        self.num = serial_no

    ############################# Check ##################################
    def check(self,session_ID):
        if(session_ID == self.num):
            if (self.rpm_up == 1 and self.rpm_dwn == 1):
                if (count >= 3):

                    now = datetime.now()
                    print(now)
                    print(".")
                    check = Mains()
                    check.init_interrupt()
                    'session start'
                elif (count <= 3 and count != 1):

                    print("!!! Session End")
                    now = datetime.now()
                    print(now)

                else:
                    print("Garbage")
            else:
                print("garbage")
        else: print("envalid id")

    ############################### Create ################################
    def get_create(self):
        return self._create

    def get_create_month(self):
        return self._create_month

    def get_create_day(self):
        return self._create_day

    def get_create_h(self):
        return self._create_h

    def get_create_m(self):
        return self._create_m

    def get_create_s(self):
        return self._create_s

    # setter method
    def set_create(self, x):
        self._create = x

    def set_create_month(self, y):
        self._create_month = y

    def set_create_day(self, z):
        self._create_day = z

    def set_create_h(self, a):
        self._create_h = a

    def set_create_m(self, b):
        self._create_m = b

    def set_create_s(self, c):
        self._create_s = c

    ############################## Read ##################################
    def read(self):

        def get_create(self):
            return self._create

        def get_create_month(self):
            return self._create_month

        def get_create_day(self):
            return self._create_day

        def get_create_h(self):
            return self._create_h

        def get_create_m(self):
            return self._create_m

        def get_create_s(self):
            return self._create_s

        # setter method
        def set_create(self, x):
            self._create = x

        def set_create_month(self, y):
            self._create_month = y

        def set_create_day(self, z):
            self._create_day = z

        ########################### delete #####################################

    def delete(self):
        del self._create
        del self._create_month
        del self._create_day
        del self._create_h
        del self._create_m
        del self._create_s
