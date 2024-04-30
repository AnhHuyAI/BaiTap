'''
# thử đường dẫn xem có nhận không
paths = 'C:\\Users\\Admin\\Documents\\Final Project MMC\\Files\\file1.txt'
a = open(paths,"r")
print(a.read())
'''
def OpenClass():
    while True:
        # nhập vào 1 data
        filename = input("Nhập vào file cần tìm : ")
        filesInput = "C:\\Users\\Admin\\Documents\\Final Project MMC\\Files\\" + filename + ".txt"
        try:
            f = open(filesInput,"r+")
            print("File name : " + filename)
            answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(",")
            count = 0
            errors = 0
            success = []
            grade =[]
            student_number= []

            # kiểm tra data
            for i in f.readlines():
                slit = i.rstrip('\n').split(",")
                count +=1
                if len(slit) != 26:
                    print("Dữ liệu sai : ", i)
                    errors += 1
                elif len(slit[0]) != 9 or not (slit[0].startswith("N") and slit[0][1:].isnumeric()):
                    print("Data này sai:",i)
                    errors += 1
                else : 
                    success.append(slit)
            print("Số dòng đúng là : " ,count)

            # chấm điểm
            for i in success:
                student_number.append(i[0])
                answer = i[1:]
                score = 0
                for j in range(25):
                    if answer[j] == answer_key[j]:
                        score += 4
                    elif answer[j] == "":
                        score += 0
                    else:
                        score -=1
                grade.append(score)
            # đưa ra kết quả
            print(grade)
            print("Điểm cao nhất: ", max(grade))
            print("Điểm thấp nhấp: ", min(grade))
            print("Miền giá trị của điểm : ", max(grade)- min(grade))
            print("Điểm trung bình là : ",sum(grade)/len(grade))

            sorts = sorted(grade)
            dodaimang = len(grade)
            if dodaimang % 2 == 0:
                giatritrungvi = sorts[dodaimang//2]
            else:
                giatritrungvi = sum(sorts[dodaimang//2 - 1: dodaimang//2 + 1])/2.0
            print("Giá trị trung vị là: ",giatritrungvi,"\n")

            #in ra
            File_grade_path = "C:\\Users\\Admin\\Documents\\Final Project MMC\\Files\\"+ filename +"_grade.txt"
            with open(File_grade_path,"w+") as fgrade:
                for thanhVien,diemSo in zip(student_number,grade):
                    fgrade.write("STT: " + thanhVien + "," + "Grade: " + str(diemSo) + "\n")
            print("Thành công - file tên là : ", filename + "_grade.txt")
            if errors == 0:
                print("Khong thay loi")
            choice = input("ban muon nhap them khong, 0 la khong, 1 la co")
            if choice == "0":
                print("good bye")
                break            
        except Exception as e :
            print("Khong ton tai",e)
        
        else : 
            f.close()
            break
           
OpenClass()