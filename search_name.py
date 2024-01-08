from difflib import get_close_matches
import csv

def search(name,dep):
    x, y,z = None , None, None
    with open (dep, "r", encoding='utf-8') as f :
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if len(row) != 0:
                if row[1] == name:
                    x = row[0]
                    y = row[2]
                    try:
                        z = row[3]
                    except:
                        z= None
                
    f.close()
    return x, y, z

def find_students(name, dep):
    students = []
    with open(dep, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == name:
                students.append(row)
    return students
def search_names(stu_name, dep):
    names=[]
    with open (dep, "r", encoding='utf-8') as f :
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if len(row) != 0:
                    name = row[1]
                    names.append(name)
    f.close()
    i =0
    dic={}
    for name in names:
        x = name.split(" ")
        o = 0
        p = False
        for nam in x:
            if nam == "بنت":
                p = True
                break
            elif nam == "ابن":
                p = True
                break
            o+=1
        if p ==True:
            x = x [:o]
            new_name = " ".join(x)
            while dic.get(new_name, 0) != 0:
                new_name = f"{new_name} "
            dic[new_name]=name
            names [i] = new_name
        i+=1
    matches = get_close_matches(stu_name, names, n=5 , cutoff=0.8)
    m = 0
    for match in matches:
        if match in dic :
            matches [m] = dic.get(match, 0)
        m+=1
    return (matches)


if __name__ == "__main__" :
    x,y,z = search("حسن الحم يدي","english.csv")
    # print(x)
    if x == None:
        matches = search_names("هند الاحمد", "english.csv")
        # print(matches)
        for i in matches:
            x, y, z = search(i,"english.csv")
            print (f"{i} : {x}")