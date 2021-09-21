def test():
    import mysql.connector
    connectiontosql = mysql.connector.connect(host="whateverhostyouareusing", user="whateveryourusernameis", passwd="whateveryourpasswordis", database="yourdatabasename")
    thecursor = connectiontosql.cursor()
    print("Hello there.")
    print("Ok so you can store your passwords here.")
    login = "Yes"
    logout = "No"
    usernameedit = "Username"
    passwordedit = "Password"
    websiteedit = "Website"
    while True:
        application = str(input("Do you want start using the tool: "))
        if application == login:
                print("Logged in to the application")
                def operations():
                    operation1 = str(input("Do you want to insert a row: "))
                    if operation1 == login:
                        username = str(input("Enter the username: "))
                        password = str(input("Enter the password: "))
                        website = str(input("Enter the website name: "))
                        tableinsert = "insert into yourtablename values ('%s', '%s', '%s')"%(username, password, website)
                        thecursor.execute(tableinsert)
                        connectiontosql.commit()
                        print("Table successfully updated")
                    elif operation1 == logout:
                        pass
                    operation2 = str(input("Do you want to delete a row: "))
                    if operation2 == login:
                        rowusername = str(input("Enter the username of the account whose details you want to delete: "))
                        tabledelete = "delete from yourtable where username=('%s')"%(rowusername)
                        thecursor.execute(tabledelete)
                        connectiontosql.commit()
                        print("Row successfully deleted")
                    elif operation2 == logout:
                        pass
                    operation3 = str(input("Do you want to edit a row: "))
                    if operation3 == login:
                        operationedit = str(input("What do you want to edit: "))
                        if operationedit == usernameedit:
                            usernameafteredit = str(input("Enter the username you want it to be changed to: "))
                            rowusername = str(input("Enter the username: "))
                            tableedit = "update yourtablename set username=('%s') where username=('%s')"%(usernameafteredit, rowusername)
                            thecursor.execute(tableedit)
                            connectiontosql.commit()
                            print("Username successfully edited")
                        elif operationedit == passwordedit:
                            passwordafteredit = str(input("Enter the password you want it to be changed to: "))
                            rowusername = str(input("Enter the username: "))
                            tableedit = "update yourtablename set password=('%s') where username=('%s')"%(passwordafteredit, rowusername)
                            thecursor.execute(tableedit)
                            connectiontosql.commit()
                            print("Password successfully edited")
                        elif operationedit == websiteedit:
                            websiteafteredit = str(input("Enter the website you want it to be changed to: "))
                            rowusername = str(input("Enter the username: "))
                            tableedit = "update yourtablename set website=('%s') where username=('%s')"%(websiteafteredit, rowusername)
                            thecursor.execute(tableedit)
                            connectiontosql.commit()
                            print("Website name successfully edited")
                    elif operation3 == logout:
                        pass
                    operation4 = str(input("Do you want to display the table: "))
                    if operation4 == login:
                        tabledisplay = "select * from yourtablename;"
                        thecursor.execute(tabledisplay)
                        wholetabledisplay = thecursor.fetchall()
                        for i in wholetabledisplay:
                            print(i)
                    elif operation4 == logout:
                        pass
                    operation5 = str(input("Do you want to display a specific login detail: "))
                    if operation5 == login:
                        operationusernamedisplay = str(input("Do you want to display the username: "))
                        if operationusernamedisplay == login:
                            website = str(input("Enter the website name: "))
                            usernamedisplay = "select username from yourtablename where website=('%s')"%(website)
                            thecursor.execute(usernamedisplay)
                            usernamefromtabledisplay = thecursor.fetchall()
                            for i in usernamefromtabledisplay:
                                print(i)
                        elif operationusernamedisplay == logout:
                            pass 
                        operationpassworddisplay = str(input("Do you want to display the password: "))
                        if operationpassworddisplay == login:
                            website = str(input("Enter the password name: "))
                            passworddisplay = "select password from yourtablename where website=('%s')"%(website)
                            thecursor.execute(passworddisplay)
                            passwordfromtabledisplay = thecursor.fetchall()
                            for i in passwordfromtabledisplay:
                                print(i)
                        elif operationpassworddisplay == logout:
                            pass 
                        operationwebsitedisplay = str(input("Do you want to display the website: "))
                        if operationwebsitedisplay == login:
                            username = str(input("Enter the username: "))
                            websitedisplay = "select website from yourtablename where username=('%s')"%(username)
                            thecursor.execute(websitedisplay)
                            websitefromtabledisplay = thecursor.fetchall()
                            for i in websitefromtabledisplay:
                                print(i)
                        elif operationwebsitedisplay == logout:
                            pass
                    elif operation5 == logout:
                        pass
                operations()
        elif application == logout:
            break
    thecursor.close()
    connectiontosql.close()
    print("Application closed")
test()