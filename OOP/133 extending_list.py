class SuperList(list):
    def __len__(self):  # override __len__ method
        return 1000


super_list1 = SuperList()  # instantiate superList object from SuperList class

print(len(super_list1))  # print len of superList1
super_list1.append(5)  # add new element of 5 to superList
print(super_list1[0])
print(issubclass(list, object))
