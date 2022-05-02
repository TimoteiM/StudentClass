import pandas
def add_student():
    students_number = int(input("How many students do you want to add?"))
    if students_number == 0:
        pass
    else:
        with open("Students.csv", mode="a") as file:
            for x in range(0,students_number):
                file.write("\n")
                id = int(input("Write the student's id: "))
                name = input("Write full name: ")
                grades = input("Write the student's grades: ")
                file.writelines(f"{id},{name},{grades}")

def menu():
    print("1.Incarcare informatii despre studenti\n"
          "2.Afisare Studenti\n"
          "3.Afisare note\n"
          "4.Afisare studenti si notele acestora\n"
          "5.Cautare student dupa nume\n"
          "6.Afisare studenti promovati\n"
          "7.Info autor\n"
          "8.Exit\n")

def Average(lista):
    average = sum(lista)/len(lista)
    return average

data = pandas.read_csv("Students.csv")

menu()


option = 1
while option != 0:
    option = int(input("Introdu o optiune:"))
    if option == 1:
        add_student()

    elif option == 2:
        for (index, row) in data.iterrows():
            print(f"{row.id}\t{row.nume}")

    elif option == 3:
        print(data.to_dict(orient='series')['note'])

    elif option == 4:
        print("id\tnume\tnote")
        for (index, row) in data.iterrows():
            print(f"{row.id}\t{row.nume}\t{row.note}")

    elif option == 5:
        search_by_name = input("Introdu numele cautat:")
        lista_nume = []
        for (index,row) in data.iterrows():
            lista_nume.append(row.nume)
        if search_by_name in lista_nume:
            print(search_by_name)
            print("Studentul a fost gasit")
        else:
            print("Studentul nu se afla in baza de date")

    elif option == 6:
        lista_note = []
        print("Studentii promovati:\n")
        for (index,row) in data.iterrows():
            lista_note = row.note.split()
            lista_note = [int(i) for i in lista_note]
            if Average(lista_note) >= 5.00:
                print(f"{row.id}\t{row.nume}\t{round(Average(lista_note),2)}")
    elif option == 7:
        print("Program realizat de Ing. Timotei Moscaliuc, student anul I - Calculatoare")
    else:
        option = 0


