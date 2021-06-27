import mysql.connector

def Menu():
    print("Menu")
    print("1.Add Student")
    print("2.Get a Student")
    print("3.Get all Student")
    print("4.update a student")
    print("5.delete a student")
    print("6.Exit")

Menu()
con=mysql.connector.connect(host="localhost",user="root",password="",database="learn")


while True:
    Option=int(input("Enter a option value"))
    if Option==1:
        cur=con.cursor()
        Id=int(input("ENter the ID"))
        Name=input("Enter the Name")
        College=input("ENter the College")
        Dept=input("Enter the Dept")
        M1=int(input("Enter M1 marks "))
        M2=int(input("Enter M2 marks "))
        M3=int(input("Enter M3 marks "))
        M4=int(input("Enter M4 marks "))
        M5=int(input("Enter M5 marks "))
        Grade=""
        Total=M1+M2+M3+M4+M5
        Average=Total/5
        if Average>=80:
            Grade='A'
        elif Average>=70 and Average<=79:
            Grade='B'
        elif Average>=60 and Average<=69:
            Grade='C'
        elif Average<=59:
            Grade='D'
        


        query="insert into student (Id ,Name , College ,Dept,M1,M2,M3, M4,M5,Total,Average, Grade) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cur.execute(query,(Id,Name,College,Dept,M1,M2,M3,M4,M5,Total,Average,Grade,))    
        con.commit()
        print("------------------inserted----------------")

    elif Option==2:
        cur=con.cursor()
        
        Id=input("enter the Id to fetch details")
        query2="select * from student where id=%s"
        cur.execute(query2,(Id,))
        
        result=cur.fetchall()
        
        for i in result: 
         print(i)
        con.commit()

    elif Option==3:

      cur=con.cursor()
      cur.execute("select * from student")
      result=cur.fetchall()

      for i in result: 
        print(i)
    
    elif Option==4:
        cur=con.cursor()
        Name=input("enter the name")
        Id=int(input("enter the id"))
        query4="update student set Name=%s where Id=%s"
        cur.execute(query4,(Name,Id,))
        print("----------updated-----------")
    
    elif Option==5:
        cur=con.cursor()
        Id=input("enter the id")
        query5="delete from student where Id=%s"
        cur.execute(query5,(Id,))
        print("-------deleted----------")
        con.commit()
    elif Option==6:
        print("Bye")
        exit()
        
    else:
        print("--------------invalid option---------------")
    
    Menu()
