/* Conectando-se ao banco como usuário master */

mysql -u root -p

/* Criando o primeiro banco de dados */

CREATE DATABASE MYBLOG;

/* Criando usuário com permissões limitadas para acesso externo ao banco de dados*/

CREATE USER 'userdb'@'localhost' IDENTIFIED BY '123abc';
CREATE USER 'userapi'@'localhost' IDENTIFIED BY '123456';

/* DROP USER 'alesson'@'localhost';  para deletar um usuário*/

SELECT User,Host FROM mysql.user;

GRANT ALTER, CREATE, DROP, DELETE, INSERT, SELECT, UPDATE, REFERENCES ON MYBLOG.* TO 'userdb'@'localhost';
GRANT SELECT ON MYBLOG.* TO 'userapi'@'localhost';

/* Para remover um ou vários privilégios de um usuário:

REVOKE ALL PRIVILEGES ON MYBLOG.* FROM 'userapi'@'localhost'; */

/* Ativar os privilégios */
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'userdb'@'localhost';
SHOW GRANTS FOR 'userapi'@'localhost';

/***************************************************************************************************/

/* Modelagem lógica */

TABELA TEMAS: (Assuntos dos conteúdos disponíveis)
TEMA CARACTER (15)


TABELA INSCRITOS: (Dados pessoais)
NOME CARACTER (40)
EMAIL CARACTER (35)
TELEFONE CARACTER (15) 


TABELA RELACIONA: (Relação entre as duas tabelas)
ID_INSCRITO (chave estrangeira)
ID_TEMA (chave estrangeira)  */


/***************************************************************************************************/

/* Criando as primeiras tabelas */

USE MYBLOG;

CREATE TABLE TEMAS(
	IDTEMA INT PRIMARY KEY AUTO_INCREMENT,
	TEMA VARCHAR(30) NOT NULL
	);

CREATE TABLE INSCRITOS(
	IDINSCRITO INT PRIMARY KEY AUTO_INCREMENT,
	NOME VARCHAR(40) NOT NULL,
	EMAIL VARCHAR(35) NOT NULL,
	TELEFONE VARCHAR(15)
	);

DESCRIBE INSCRITOS;

CREATE TABLE RELACIONA(
	IDRELACIONA INT PRIMARY KEY AUTO_INCREMENT,
	ID_INSCRITO INT,
	ID_TEMA INT,
	FOREIGN KEY(ID_INSCRITO) REFERENCES INSCRITOS(IDINSCRITO),
	FOREIGN KEY(ID_TEMA) REFERENCES TEMAS(IDTEMA)
	);


/***************************************************************************************************/

/*  
    Popular as tabelas com os arquivs anexos:
 
    Tabela TOPICOS com o arquivo topicos.sql,
 
    Tabela INSCRITOS com o arquivo inscritos.sql,
 
    Tabela RELACIONA com o arquivo relaciona.sql
 */


INSERT INTO INSCRITOS VALUES(NULL, 'Erro comum', 'erro_comum@teste.com', '+5523 91301-5959');

/***************************************************************************************************/


SELECT * FROM INSCRITOS
LIMIT 15;

SELECT * FROM TEMAS;

SELECT TM.IDTEMA AS ID,
       TM.TEMA AS TEMA
FROM TEMAS TM;

SELECT * FROM RELACIONA
LIMIT 10

SELECT INSC.NOME AS Nome,
       INSC.EMAIL AS Email
FROM INSCRITOS INSC
LIMIT 20;


/* Relacionando os inscritos aos seus temas de interesse */

SELECT INSC.NOME AS Nome,
       INSC.EMAIL AS Email,
       TM.TEMA AS Tema
FROM INSCRITOS INSC
LEFT JOIN TEMAS TM ON RE.ID_TEMA = TM.IDTEMA
LEFT JOIN RELACIONA RE ON RE.ID_INSCRITO = INSC.IDINSCRITO
WHERE TM.IDTEMA = 3 OR TM.IDTEMA = 5
ORDER BY INSC.NOME;


/* Removendo o nome do tema, agrupando por nome e email e removendo usuário teste */

SELECT INSC.NOME AS Nome,
       INSC.EMAIL AS Email
FROM INSCRITOS INSC
LEFT JOIN RELACIONA RE ON RE.ID_INSCRITO = INSC.IDINSCRITO
LEFT JOIN TEMAS TM ON RE.ID_TEMA = TM.IDTEMA
WHERE TM.IDTEMA = 3
AND INSC.IDINSCRITO != 1
GROUP BY INSC.NOME,
         INSC.EMAIL
ORDER BY INSC.NOME;

/* Busca com Like */

SELECT INSC.NOME AS Nome,
       INSC.EMAIL AS Email,
       TM.TEMA AS Tema
FROM INSCRITOS INSC
LEFT JOIN RELACIONA RE ON RE.ID_INSCRITO = INSC.IDINSCRITO
LEFT JOIN TEMAS TM ON RE.ID_TEMA = TM.IDTEMA
WHERE TM.TEMA LIKE 'C%' OR TM.TEMA LIKE '%r%'
AND INSC.IDINSCRITO != 1
ORDER BY INSC.NOME;

SELECT INSC.NOME AS Nome,
       INSC.EMAIL AS Email
FROM INSCRITOS INSC
LEFT JOIN RELACIONA RE ON RE.ID_INSCRITO = INSC.IDINSCRITO
LEFT JOIN TEMAS TM ON RE.ID_TEMA = TM.IDTEMA
WHERE INSC.IDINSCRITO != 1
AND TM.TEMA LIKE 'C%' OR TM.TEMA = 'Rubi%' 
GROUP BY INSC.NOME,
         INSC.EMAIL
ORDER BY INSC.NOME;


/*--------------------------------------------------------------------------------

Base de usuários

---------------------------------------------------------------------------------*/

CREATE TABLE USERS (IDUSER INT PRIMARY KEY AUTO_INCREMENT,
                    USERNAME VARCHAR(40) UNIQUE, 
                    PASSWORD CHAR(128));

INSERT INTO USERS (IDUSER, USERNAME, PASSWORD) 
VALUES(NULL, 'test@email.com', SHA2('abcdef', 512));

INSERT INTO USERS (IDUSER, USERNAME, PASSWORD) 
VALUES(NULL, 'External User', SHA2('ABCdef@#', 512));

INSERT INTO USERS (IDUSER, USERNAME, PASSWORD) 
VALUES(NULL, 'userapi', SHA2('123456', 512));