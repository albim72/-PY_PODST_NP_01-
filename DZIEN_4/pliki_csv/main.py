import csv

with open("firma.csv",encoding="utf-8") as pc:
    csv_reader = csv.reader(pc,delimiter=";")
    line_count=0
    for row in csv_reader:
        if line_count==0:
            print(f'Nazwa Kolumny: {", ".join(row)}')
            line_count+=1
        else:
            print(f'\t{row[0]} pracuje na stanowisku {row[1]} i ma urodziny w miesiącu: {row[2]},'
                  f'otrzymuje nagrodę finansową w wysokości: {row[3]} zł')
            line_count+=1

    print(f'dodano {line_count} linii')
    print(f'dodano {line_count + 1} osób')

print("_"*50)
print("utworzenie pliku CSV")

with open('pracownik.csv','w',encoding='utf-8',newline='') as ef:
    emp_writer = csv.writer(ef,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC)

    emp_writer.writerow(('Karol','Krot','Finanse',10))
    emp_writer.writerow(('Anna','Nowak','Finanse',8))
    emp_writer.writerow(('Jacek','Bień','IT',11))
    emp_writer.writerow(('Nadia','Ozrik','IT',3))
