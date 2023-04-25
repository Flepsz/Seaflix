CREATE DATABASE seaflix;

use seaflix;

CREATE TABLE usuarios(
	idUsuario int auto_increment primary key,
    usuario varchar(50) not null,
    email varchar(100) not null,
    plano varchar(50),
    tipo varchar(50),
    idade int
);

CREATE TABLE filmes(
	idFilme int auto_increment primary key,
    filme varchar(200),
    plano varchar(50),
    descricao varchar(255),
	class int 
);

INSERT INTO usuarios(usuario, email, plano, tipo, idade)
values
	('Felipe', 'flepsz@gmail.com', 'Premium', 'Admin', '17'),
    ('Horn', 'hornzz@gmail.com', 'Basic', 'User', '18');
    
select * from usuarios;

INSERT INTO filmes(filme, plano, descricao, class)
values
	('Bohemian Rhapsody', 'Premium', 'xxxxxxx', '0'),
    ('Matrix Reloaded', 'Basic', 'xxxxxxx', '16');
    
select * from filmes;
