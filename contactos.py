import sqlite3,os,time,winsound

class Manager:
    def __init__(self):
        self.Name = ""
        self.Phone = ""
        self.Address = ""
    
    def add(self):
        running = True
        while running:
            #os.system("cls") serve para limpar a tela

            os.system("cls")
            print("---------ADICIONE UM NOVO CONTACTO----------")
            print("PRECIONE SHIFT + Q PARA CANCELAR")
            print()
            #Criando arquivo temporario
            temp_name = input("Name: ")
            #Verificando se tem um espaco vazio
            if len(temp_name)!= 0 and temp_name != "Q".upper():
                db = sqlite3.connect("connection")
                cursor = db.cursor()
                cursor.execute("SELECT Name FROM contacts")
                results = cursor.fetchall()
                for i in results:
                    if temp_name in i:
                        print("Este contacto ja existe no nosso banco de dados")
                        time.sleep(3)
                        self.add()
                self.Name = temp_name
                #limpando a variavel temp_name
                temp_name = ""

                time.sleep(0.20)
                self.Phone = input("Phone: ")
                time.sleep(0.20)
                self.Address = input("Address: ")
                #Salvar no banco de dados
                #db = sqlite3.connect("connection")
                #criando objecto
                #cursor = db.cursor()
                cursor.execute("""INSERT INTO contacts\
                                (Name , Phone , Address )VALUES(?,?,?)""",\
                                (self.Name,self.Phone,self.Address))
                        #Confirmar que queremos inserir no nosso banco de dados
                db.commit()                
                Add_more = input("Deseja adicionar outro contacto? (Y/N): ")

                if Add_more == "y".lower():
                    continue
                else:
                    db.close()
                    running = False
                    print("Saindo do menu")
                    time.sleep(2)
                    self.menu()    
            elif temp_name == "Q":
                print("Saindo do menu principal")
                time.sleep(2)
                self.menu()
            else:
                winsound.Beep(3000,100)
                winsound.Beep(3000,100)
                print("Por favor preencha todos os campos")
                time.sleep(3) 
                self.add()       
                    

    def update(self):
        pass

    def remove(self):  
            print("----------Deletar cadastros-------")
            name = input("Digite o nome do cliente para deletar: ")
            confirm = input("Voce tem certeza? [Y/N]: ")
            if confirm == "y".lower():
                db = sqlite3.connect("connection")
                cursor = db.cursor()
                cursor.execute("DELETE FROM contacts WHERE Name = ?",(name,))
                #Confirmar se quer deletar
                db.commit()
                print("CAdastro deletado com sucesso")
                time.sleep(3)
                self.menu()
            else:
                print('Saindo do menu principal')
                time.sleep(3)
                self.menu()
                    
    def get_list(self):
        count = 0
        count_2 = 0
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        os.system("cls")
        print("........Contactos..........")
            
        time.sleep(0.50)
        #Criando um array de informacoes
        cursor.execute("SELECT Name, Phone, Address FROM contacts")
        result = cursor.fetchall()
        for row in result:
            time.sleep(0.50)
            count += 1
            count_2 += 1
            print(count_2, row)
            if count == 5:
                input("Pressione qualquer tecla para continuar.")
                count = 0
                print()
            print()
            print("Fim de resultados")
            print()
            input("Pressione qualquer tecla para continuar")
            op = input("Digite (M) para menu, (U) para actualizar, (D) para deletar: ")
                
            if op=="m".lower():
                self.menu()

            elif op=="u".lower():
                self.update()

            elif op=="d".lower():
                self.remove()        

    def terminate(self):
        pass

    def menu(self):
        os.system('cls')
        winsound.Beep(2000,50)
        print("------------MENU------------")
        time.sleep(0.05)
        print()
        print("1. Add")
        time.sleep(0.05)

        print("2. Update")
        time.sleep(0.05)

        print("3. Remove")
        time.sleep(0.05)

        print("4. List")
        time.sleep(0.05)

        print("5. Terminate")
        print()

        option = input("Selecione uma opcao: ")

        if option == "1":
            self.add()
        elif option == "2":
            self.update()
        elif option == "3":
            self.remove()
        elif option == "4":
            self.get_list()
        elif option == "5":
            self.terminate()
        else:
            winsound.Beep(2500,100)
            print("Opcao invalida! Tente novamente (1-5)")
            time.sleep(2)   
            #Chamar o menu novamente
            self.menu()



        
    def main(self):
        os.system('cls')
        #Criar conexao com banco de dados
        if os.path.isfile("connection"):
            db = sqlite3.connect("connection")
            time.sleep(3)
            winsound.Beep(2000,50)
            print()
            print("Conexao bem sucedida!")
            time.sleep(2)
            self.menu()

        else:
            print("Essa conexao nao existe")
            print()
            time.sleep(3)
            winsound.Beep(2000,50)

            print("creating new connection file")
            time.sleep(3)
            db = sqlite3.connect("connection")
            #Criando tabelas no banco de dados
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE contacts
                            (Name TEXT, Phone TEXT, Address TEXT)""")


            winsound.Beep(2000,50)
            print()
            print("Conexao criada com sucesso")
            print("Conectado com sucesso")
            time.sleep(2)
            self.menu()

        self.menu()

contacts = Manager()
contacts.main()                               