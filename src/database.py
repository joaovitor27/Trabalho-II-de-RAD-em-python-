import datetime
import os
import sqlite3


def get_db():
    conn = sqlite3.connect('./database.sqlite')
    return conn


def create_table(sql: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()
    return "Table created success"


def query_db(query: str, args: tuple = (), one: bool = False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def insert_db(query: str, args: tuple = ()):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    conn.close()
    return 'inserido com sucesso'


def create_table_employee():
    result = create_table('CREATE TABLE IF NOT EXISTS employee (id_employee INTEGER PRIMARY KEY AUTOINCREMENT, '
                          'office TEXT, wage REAL, employee INTEGER, contract_date DATETIME, FOREIGN KEY (employee)'
                          ' REFERENCES people (id_person) )')
    return result


def add_column_email_in_table_people():
    insert_db('ALTER TABLE people ADD email TEXT NULL')
    return 'table altered com success'


def delete_db(query: str, args: tuple = ()):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    conn.close()
    return 'Excluído com sucesso'


def put_db(query: str, args: tuple = ()):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    conn.close()
    return 'Dado editado com sucesso'


def create_table_pessoa():
    result = create_table('CREATE TABLE IF NOT EXISTS people (id_person INTEGER PRIMARY KEY AUTOINCREMENT, '
                          'cpf VARCHAR(14) UNIQUE, first_name TEXT, middle_name TEXT, last_name TEXT, age integer,'
                          ' conta INTEGER UNIQUE)')
    return result


def create_table_conta():
    result = create_table('CREATE TABLE IF NOT EXISTS conta (id_conta INTEGER PRIMARY KEY AUTOINCREMENT, '
                          'agency TEXT, number_conta TEXT, saldo REAL, gerente INTEGER, '
                          'titular INTEGER, FOREIGN KEY (titular) references people (conta))')
    return result


def insert_conta(agency: str, number_conta: str, saldo: float, gerente: int, titular: int):
    result = insert_db('INSERT INTO conta(agency, number_conta, saldo, gerente, titular) values (?,?,?,?,?);',
                       (agency, number_conta, saldo, gerente, titular))
    return result


def insert_pessoa(cpf: str, first_name: str, middle_name: str, last_name: str, age: int, email: str = None):
    result = insert_db(
        'INSERT INTO people(cpf, first_name, middle_name, last_name, age, email) values (?,?,?,?,?,?);',
        (cpf, first_name, middle_name, last_name, age, email)
    )
    return result


def insert_employee(office: str, wage: float, employee: int):
    contract_date = datetime.datetime.now()
    result = insert_db('INSERT INTO employee(office, wage, employee, contract_date) values (?,?,?,?);',
                       (office, wage, employee, contract_date))
    return result


def format_cpf(cpf: str):
    if '-' and '.' not in cpf or len(cpf) <= 11:
        cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    return cpf


def delete_conta(number_conta: str):
    result = delete_db('DELETE FROM conta WHERE number_conta=?', (number_conta,))
    return result


def delete_pessoa(cpf: str):
    result = delete_db('DELETE FROM people WHERE cpf=?', (cpf,))
    return result


def delete_employee(id_employee: int):
    result = delete_db('DELETE FROM employee WHERE id_employee=?', (id_employee,))
    return result


def put_conta(number_conta: str, saldo: float, agency: str, gerente: int, titular: int):
    result = put_db('UPDATE conta SET saldo = ?, agency = ?, gerente = ?, titular = ? WHERE number_conta=?',
                    (saldo, agency, gerente, titular, number_conta))
    return result


def put_pessoa(cpf: str, first_name: str, middle_name: str, last_name: str, age: int, email: str):
    result = put_db('UPDATE people SET first_name=?, middle_name=?, last_name=?, age=?, email=? WHERE cpf=?',
                    (first_name, middle_name, last_name, age, email, cpf))
    return result


def put_employee(id_employee: int, office: str, wage: float):
    result = put_db('UPDATE employee SET office=?, wage=? WHERE id_employee=?',
                    (office, wage, id_employee))
    return result


def get_pessoas():
    result = query_db('Select * From people;')
    return result


def get_contas():
    result = query_db('Select * From conta;')
    return result


def get_funcionarios():
    result = query_db('Select * From employee;')
    return result


def get_pessoa(cpf: str):
    result = query_db('SELECT * FROM people WHERE cpf=?', (cpf,))
    try:
        os.mkdir('./Busca de pessoa')
    except OSError:
        print("Pasta já existe")
    if len(result) == 0:
        return "Pessoa não encontrada"

    result = result[0]
    arquivo = open("./Busca de pessoa/pessoa_results.txt", 'a')
    arquivo.write(f'================================================================================================\n'
                  f'Id_pessoa: {result[0]}\nCPF: {result[1]}\nNome: {result[2]}\nSegundo_nome: {result[3]}\n'
                  f'Ultimo_nome: {result[4]}\nIdade: {result[5]}\nConta: {result[6]}\n'
                  f'================================================================================================\n')
    arquivo.close()
    return result


def get_conta(number_conta: str):
    result = query_db('SELECT * FROM conta WHERE number_conta=?', (number_conta,))
    try:
        os.mkdir('./Busca de conta')
    except OSError:
        print("Pasta já existe")

    if len(result) == 0:
        return "Pessoa não encontrada"

    result = result[0]
    arquivo = open("./Busca de conta/conta_results.txt", 'a')
    arquivo.write(f'================================================================================================\n'
                  f'Id_conta: {result[0]}\nAgência: {result[1]}\nNúmero_da_conta: {result[2]}\nSaldo: {result[3]}\n'
                  f'Gerente: {result[4]}\nTitular: {result[5]}\n'
                  f'================================================================================================\n')
    arquivo.close()

    return result


def get_employee(id_employee: int):
    result = query_db('SELECT * FROM employee WHERE id_employee=?', (id_employee,))
    try:
        os.mkdir('./Busca de Funcionários')
    except OSError:
        print("Pasta já existe")

    if len(result) == 0:
        return "Pessoa não encontrada"

    result = result[0]
    with open("./Busca de Funcionários/Funcionários_results.txt", 'a') as arquivo:
        arquivo.write(
            f'================================================================================================\n'
            f'Id_Funcionários: {result[0]}\nFunção: {result[1]}\n Salário: {result[2]}\nid_pessoa: {result[3]}\n'
            f'Data de Contração: {result[4]}'
            f'================================================================================================\n'
        )

    return result


def get_pessoa_conta(cpf: str):
    cpf = format_cpf(cpf)
    result = query_db('SELECT * FROM people left join conta c on c.number_conta = people.conta '
                      'WHERE cpf=?', (cpf,))
    try:
        os.mkdir('./Busca de pessoa e conta')
    except OSError:
        print("Pasta já existe")
    result = result[0]
    arquivo = open("./Busca de pessoa e conta/pessoa_conta_results.txt", 'a')
    arquivo.write(f'================================================================================================\n'
                  f'Id_pessoa: {result[0]}\nCPF: {result[1]}\nNome: {result[2]}\nSegundo_nome: {result[3]}\n'
                  f'Ultimo_nome: {result[4]}\nIdade: {result[5]}\nConta: {result[6]}\nId_conta: {result[7]}\n'
                  f'Agência: {result[8]}\nNúmero_da_conta: {result[9]}\nSaldo: {result[10]}\nGerente: {result[11]}\n'
                  f'Titular: {result[12]}\n'
                  f'================================================================================================\n')
    arquivo.close()
    return result


def remove_spaces_by_commas(path: str):
    arquivo_read = open(path, 'r')
    linhas_arquivo = arquivo_read.readlines()
    new_linha_arquivo = []
    for linha in linhas_arquivo:
        new_linha = linha.replace(' ', ',')
        new_linha_arquivo.append(new_linha)

    arquivo_read.close()

    arquivo_write = open(path, 'w')
    for new_linha in new_linha_arquivo:
        arquivo_write.write(new_linha)

    arquivo_write.close()


def inserindo_dados_no_banco(path: str):
    path = path.lower()
    if path == './dados/nomes.txt':
        arquivo = open(path, 'r')
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.split(',')
            cpf, first_name, middle_name, last_name, age = dados[0], dados[1], dados[2], dados[3], dados[4]
            insert_pessoa(cpf, first_name, middle_name, last_name, int(age))

    elif path == './dados/contas.txt':
        arquivo = open(path, 'r')
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.split(',')
            agency, number_conta, saldo, gerente, titular = dados[0], dados[1], dados[2], dados[3], dados[4]
            insert_conta(agency, number_conta, float(saldo), int(gerente), int(titular))
    else:
        return "path inválido"


if __name__ == '__main__':
    create_table_employee()
    add_column_email_in_table_people()
