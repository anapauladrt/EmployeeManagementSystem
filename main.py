import os

cad_f=[]
cad_g=[]
cad_v=[]

class Funcionario:
  def __init__(self, nome, cpf, salario, departamento):
    self.nome = nome
    self.cpf = cpf
    self.salario = salario
    self.departamento = departamento
  def getNome(self):
    return self.nome
  def getCpf(self):
    return self.cpf
  def getSalario(self):
    return self.salario
  def getDepartamento(self):
    return self.departamento
    
  def bonificar(self):
    self.salario=self.salario*1.10
    

class Gerente(Funcionario):
  def __init__(self,senha, num,nome,cpf,salario,departamento):
    super().__init__(nome,cpf,salario,departamento)
    self.senha=senha
    self.num=num
  def getSenha(self):
    return self.senha
  def getNum(self):
    return self.num

  def bonificar(self):
    self.salario*=1.10

  def autenticarsenha(self,senha_a):
    return self.senha == senha_a
      
class Vendedor(Funcionario):
  def __init__(self, nome, cpf, salario, departamento, quantidade, comissao):
      super().__init__(nome, cpf, salario, departamento)
      self.quantidade = quantidade
      self.comissao = comissao
    
  def getQuantidade(self):
    return self.quantidade

  def getComissao(self):
    return self.comissao

  def atualizaQuantidadeVendas(self, quantidade):
    self.quantidade += quantidade 
    print("\nQuantidade de vendas atualizada para: ", self.quantidade)
    
  def calculaSalario(self,horas,vendedor):
    self.salario=horas*30
    salario=print("\nO salario de {} é: {}".format(vendedor,self.salario))

def menu():
  while 1:
    try:
      opcao=int(input("1-Cadastrar Funcionário\n2-Cadastrar Gerente\n3-Cadastrar Vendedor\n4-Bonificar Funcionário\n5-Bonificar Gerente\n6-Autenticar senha Gerente\n7-Atualizar quantidade de vendas do vendedor\n8-Calcular Salário do Vendedor\n9- Listas Funcionários\n10-Listas Gerentes\n11-Listas Vendedores\n"))
      if 0<opcao<12:
        return opcao
      
      else:
        os.system('cls')
        menu()
    
    except:
      os.system('cls')
      menu()

objeto1=Funcionario(0,0,0,0)
objeto2=Gerente(0,0,0,0,0,0)
objeto3=Vendedor(0,0,0,0,0,0)

while(1):
    opcao=menu()

    if opcao == 1:
        os.system('cls')
        nome = input("Nome: ").upper()
        while 1:
          
            try:
                cpf = int(input("CPF (apenas números): "))  
                break  
            except ValueError:
                print("Apenas números! Tente novamente.")

        while 1:
            try:
                salario = float(input("Salário: "))
                break  
            except ValueError:
                print("Por favor, insira um valor numérico para o salário.")

        departamento = input("Departamento: ")
        objeto1 = Funcionario(nome, cpf, salario, departamento)
        cad_f.append(objeto1)
        os.system('cls')
    
    if opcao == 2:
        os.system('cls')
        nome = input("Nome: ").upper()
        while 1:
            try:
                cpf = int(input("CPF (apenas números): "))  
                break
            except ValueError:
                print("Apenas números! Tente novamente.")
                
        while 1:
            try:
                salario = float(input("Salário: "))
                break
            except ValueError:
                print("Por favor, insira um valor numérico para o salário.")
                
        departamento = input("Departamento: ")
          
        while 1:
            try:
                senha = int(input("Senha (Apenas números): "))
                break
            except ValueError:
                print("Apenas números! Tente novamente.")
          
        while  1:
            try:
                num = int(input("Número de funcionários: "))
                break
            except ValueError:
                print("Apenas números! Tente novamente.")
                
        objeto2 = Gerente(senha, num, nome, cpf, salario, departamento)
        cad_g.append(objeto2)
        os.system('cls')

        
    if opcao == 3:
      os.system('cls')
      nome = input("Nome: ").upper()
      while 1:
        try:
          cpf = int(input("CPF (apenas números): "))  
          break
        except ValueError:
          print("Apenas números! Tente novamente.")
          
      while 1:
        try:
          salario = float(input("Salário: "))
          break
        except ValueError:
          print("Por favor, insira um valor numérico para o salário.")
          
      departamento = input("Departamento: ")
      
      while 1:
        try:
          quantidade = int(input("Quantidade de vendas: "))
          break
        except ValueError:
          print("Por favor, insira um valor numérico válido.")
          
      while 1:
        try:
          comissao = float(input("Comissão: "))
          break
        except ValueError:
          print("Por favor, insira um valor numérico válido.")
          
      objeto3 = Vendedor(nome, cpf, salario, departamento, quantidade, comissao)
      cad_v.append(objeto3)
      os.system('cls')
        
    if opcao == 4:
        os.system('cls')
        print("Nome   | Departamento\n\n")
        for i in cad_f:
            print(i.getNome(), " | ", i.getDepartamento(), "\n")
        
        sol = input("Nome do funcionário que deseja bonificar: ").upper()
        funcionario_encontrado = False  # Para controlar se o funcionário foi encontrado

        for f in cad_f:
            if sol == f.getNome():
                f.bonificar()
                print("\n\nNovo salário do funcionário: {:.3f}".format(f.getSalario()))
                funcionario_encontrado = True
                break  # Sai do loop após bonificar

        if not funcionario_encontrado:
            print("\n\nNão encontrado")
        
        sair = input("\nSair? Clique Enter ")
        os.system('cls')

   
    if opcao == 5:
        os.system('cls')
        print("Nome   | Departamento")
        for i in cad_g:
            print(i.getNome(), " | ", i.getDepartamento())
        nome_f = input("Nome do gerente que deseja bonificar: ").upper()
        gerente_encontrado = False  
        for g in cad_g:
            if nome_f == g.getNome():
                g.bonificar()
                print("\n\nNovo salário do gerente: {:.3f}".format(g.getSalario()))
                gerente_encontrado = True
        if not gerente_encontrado:
            print("\n\nNão encontrado")
        sair = input("\nSair? Clique Enter ")
        os.system('cls')

    if opcao == 6:
        os.system('cls')
        print("Nome   | Departamento\n\n")
        for i in cad_g:
            print(i.getNome(), i.getDepartamento())
        aut = input("\n\nAutenticar senha de qual gerente? ").upper()
        gerente_encontrado = False
        for g in cad_g:
            if aut == g.getNome():
                gerente_encontrado = True
                senha_a = int(input("\n\nSenha: "))
                if g.autenticarsenha(senha_a):
                    print("Autenticação bem-sucedida!")
                    sair = input("\nSair? Clique Enter ")
                    os.system('cls')
                else:
                    print("Senha incorreta.")
                    sair = input("\nSair? Clique Enter ")
                    os.system('cls')
        if not gerente_encontrado:
            print("\n\nGerente não encontrado.")
            sair = input("\nSair? Clique Enter ")
            os.system('cls')

            
    if opcao==7:
      os.system('cls')
      print("Nome   | Departamentos\n\n")
      for i in cad_v:
        print(i.getNome(), "|", i.getQuantidade())
      vend=input("\n\nNome do vendedor: ").upper()
      encontra=False
      for i in cad_v:
        if vend==i.getNome():
          encontra=True
          quan=int(input("Quantidade de vendas a adicionar: "))
          i.atualizaQuantidadeVendas(quan)
      if not encontra:
        print("Não encontrado")
          
      sair=input("\nSair? Clique Enter ")
      os.system('cls')
    
    if opcao==8:
      os.system('cls')
      print("Nome   | Departamento")
      for i in cad_v:
        print(i.getNome(),"    | ",i.getDepartamento())
      vendedor=input("\nQual vendedor?").upper()
      encontra=False
      for v in cad_v:
        if vendedor==v.getNome():
          encontra=True
          horas=int(input("\nQuantas horas de trabalho por dia?"))
          v.calculaSalario(horas,vendedor)#dentro do parenteces colocamos oq é necessário para fazer a funcao rodar
      if not encontra:
        print("Não encontrado")
          
      sair=input("\nSair? Clique Enter ")
      os.system('cls')
          
    if opcao==9:
      os.system('cls')
      print("Nome   | Departamento\n\n")
      for i in cad_f:
        print(i.getNome(),i.getDepartamento())
      nome=input("\n\nNome do funcionario: ").upper()
      encontra=False
      os.system('cls')      
      for i in cad_f:
        if nome==i.getNome():
          encontra=True
          print("Nome | CPF | Salário | Departamento\n\n")
          print(f"{i.getNome()} | {i.getCpf()} | {i.getSalario():.3f} | {i.getDepartamento()}\n\n")
          
      if not encontra:
        print("\n\nNãp encontrado")
      sair=input("\nSair? Clique Enter ")
      os.system('cls')
        
    if opcao==10:
      os.system('cls')
      print("Nome   | Departamento")
      for i in cad_g:
        print(i.getNome() ," | ", i.getDepartamento())
      nome_g=input("\n\nNome do gerente:").upper()
      encontra=False
      os.system('cls')
      for i in cad_g:
        if nome_g==i.getNome():
          encontra=True
          print("Nome | N° de func | Cpf | Salário | Departamento\n\n")
          print(i.getNome()," | ",i.getNum()," | ",i.getCpf()," | ",i.getSalario()," | ",i.getDepartamento())
      if not encontra:
          print("\n\nNãp encontrado")
      sair=input("\nSair? Clique Enter ")
      os.system('cls')
        
    if opcao==11:
      os.system('cls')
      print("Nome   | Departamento")
      for i in cad_v:
        print("\n\n",i.getNome() ," | ", i.getDepartamento())
      nome_v=input("\n\nNome do vendedor:").upper()
      encontra=False
      for i in cad_v:
        if nome_v==i.getNome():
          encontra=True
          os.system('cls')
          print("Nome |  Cpf | Salário | Departamento | Quantidade\n\n")
          print(i.getNome()," | ",i.getCpf()," | ", i.getSalario()," | ",i.getDepartamento()," | ", i.getQuantidade())
      
      if not encontra:
          print("\n\nNãp encontrado")
      sair=input("\nSair? Clique Enter ")
      os.system('cls')
        