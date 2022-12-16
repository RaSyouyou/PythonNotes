class SalaryAccount:

    def __call__(self,salary):
        print('start')
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//8

        return dict(year=yearSalary,month = salary, day = daySalary , hour= hourSalary)

s = SalaryAccount()
print(s(9000))