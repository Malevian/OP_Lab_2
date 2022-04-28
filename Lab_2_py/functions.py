import pickle

class info:
    def __init__(self, name1, DateOfBirth1, FormOfStudying1, GroupName1, GroupNumber1, AverageMark1):
        self.name = name1
        self.DateOfBirth = DateOfBirth1
        self.FormOfStudying = FormOfStudying1
        self.GroupName = GroupName1
        self.GroupNumber = GroupNumber1
        self.AverageMark = AverageMark1


def create_info():
    Students = []
    stop_botton = chr(19)
    print("Enter the name of the group: ")
    GroupName = input()
    while True:
        print("Student's name: ")
        additional = input()
        if additional[0] != stop_botton:
            name = additional

            print("Date of Birth(DD.MM.YEAR): ")
            DateOfBirth = input()

            print("Form of studying(Daily or Correspondence): ")
            FormOfStudying = input()

            print("Group number: ")
            GroupNumber = input()

            print("Average mark(0-100): ")
            AverageMark = input()

            print()

            Student = info(name, DateOfBirth, FormOfStudying, GroupName, GroupNumber, AverageMark)
            Students.append(Student)
        else:
            break
    return Students

def output_students(Students):
    print("---------------------------------------------------------------------------")
    print(" Student's name | Date of Birth | Form of studying | Group | Average Mark ")
    print("---------------------------------------------------------------------------")
    for i in range(len(Students)):
        print(" {0} | {1} | {2} | {3}-{4} | {5} ".format(
                        Students[i].name, Students[i].DateOfBirth, Students[i].FormOfStudying,
                        Students[i].GroupName, Students[i].GroupNumber, Students[i].AverageMark))
    print("---------------------------------------------------------------------------")

def CreateBinaryFile(fileName, Students):
    with open(fileName, "wb") as BinaryFile:
        pickle.dump(Students, BinaryFile)
    BinaryFile.close()
    return len(Students)

def FromByteToReadable(fileName):
    InfoList = []
    with open(fileName, "rb") as BinaryFile:
        List = pickle.load(BinaryFile)

    for what in List:
        InfoList.append(what)
    return InfoList

def LowLevelStudents(InfoList):
    MainList = []
    while len(InfoList) - 1 > 0:
        LowestAverageMark = InfoList[0].AverageMark
        GroupNum = InfoList[0].GroupNumber
        LowestStudent = InfoList[0]
        j = 0
        while j < len(InfoList) - 1:

            if InfoList[j].GroupNumber == GroupNum:

                if InfoList[j].AverageMark < LowestAverageMark:

                    LowestAverageMark = InfoList[j].AverageMark
                    LowestStudent = InfoList[j]

                InfoList.remove(InfoList[j])

            else: j += 1
        MainList.append(LowestStudent)
    return MainList

def Identify(ListOfStudents):
    print("Pick the average mark: ")
    average = float(input())
    i = 0
    while i < len(ListOfStudents):
         if int(ListOfStudents[i].GroupNumber) <= 39 or int(ListOfStudents[i].GroupNumber) >= 50 or ListOfStudents[i].FormOfStudying.upper() != "DAILY" or float(ListOfStudents[i].AverageMark) < average and len(ListOfStudents) != 0:
             ListOfStudents.pop(i)
         else: i += 1

    if len(ListOfStudents) > 1:
        for i in range(len(ListOfStudents)):
            for j in range(i+1,len(ListOfStudents)):
                if ListOfStudents[i].name[0] >  ListOfStudents[j].name[0]:
                    ListOfStudents[i], ListOfStudents[j] = ListOfStudents[j], ListOfStudents[i]
    return ListOfStudents
