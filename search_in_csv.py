import csv

def search(id,dep):
    x, y, z = None , None, None
    with open (dep, "r", encoding='utf-8') as f :
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if len(row) != 0:
                if row[0] == id:
                    x = row[1]
                    y = row[2]
                    try:
                        z = row[3]
                    except:
                        z=None
    f.close()
    return x, y, z

if __name__ == "__main__" :
    x,y = search("30002","arabic.csv")
    print(x,y) 
    lines = y.split("\n")
    for line in lines :
        if line != "" :
            line = line.split(" : ")[1]
            line = line.split("من السنةس")
            year = line[1]
            mark = line[0].split(" في ")[0]
            sub = line[0].split(" في ")[1]

            try:
                mark = int(mark)
                
            except Exception as e:
                print (e)