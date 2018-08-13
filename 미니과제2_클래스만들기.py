# class school :
#     name = "건국대학교"
#     establish_year = 1910
#     address = "서울 광진구 자양동"
#
# school1 = school()
# print(school1.name)
# print("{}년".format(school1.establish_year))
# print(school1.address)

class school :
    def __init__(self, name, establish_year, address):
        self.name = name
        self.establish_year = establish_year
        self.address = address

school1 = school('건국대','1910년','서울 광진구 자양동')

print(school1.name)
print(school1.establish_year)
print(school1.address)
