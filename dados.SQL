-- SQLBook: Code
--Supondo a ordem: id, nome, tipo, descricao, foto(desabilitada, nao sei o que fazer)

insert into Ferramenta values ('Conjunto de ferramentas 100 pecas', 'perigoso', 'Maleta Termoplastica');
insert into Ferramenta values ('Conjunto de ferramentas 100 pecas', 'perigoso', 'Maleta Termoplastica');
insert into Ferramenta values ('Parafusadeira/furadeira sem fio', 'perigoso', 'Bateria integrada de 12v max, velocidade 0-900/min (rpm), mandril 3/8" (10mm), peso 0,85 kg, inclui: carregador, bits para parafusar, adaptador magnetico e brocas.');
insert into Ferramenta values ('Lixadeira orbital 1/4 de folha dewalt', 'perigoso', 'dwe6411, 230w, 14000/min, tensao 127v, 1/4 de lixa, coletor de po, prefurador de lixas');
insert into Ferramenta values ('Impressora gtmax3d pro core a1v2', 'seguro', 'Software simplify3d, area de impressao 18 litros, bivolt automatico (110/220v), gabinete fechado em aco carbono, display em lcd, camadas de 0,5mm a 0,32mm, conectividade usb e cartao sd, velocidade de impressao 150mm/s, velocidade de deslocamento 300mm/s, velocidade de aceleracao 2500mm/s2');
insert into Ferramenta values ('Serra tico-tico', 'perigoso', 'Orbital 550w, 100% rolamentada, marca skill. Composta por 1 serra, 1 lamina de serra para madeira, 1 chave alien e 1 guia pralela');
insert into Ferramenta values ('Mesa giratoria', 'seguro', 'Einscan-se, elite desktop 3d scanner, empresa shining 3d. Digitalizacao 3d');
insert into Ferramenta values ('Camera de video', 'seguro', 'interna wi-fi full hd, modelo im3, intelbras, base de fixacao, esponja adesiva dupla face, cabo usb de alimentacao, fonte de aliemntacao, cabo usb de alimentacao, guia de instalacao');
insert into Ferramenta values ('Projetor epson powerlite e20', 'seguro', 'modelo h918a. Composicao: Projetor, controle remoto, cabo vga, cabo de energia');
insert into Ferramenta values ('Carrinho de ferramentas', 'seguro', '3 gavetas e 2 portas modelo c06');
insert into Ferramenta values ('Oculos de realidade virtual, oculos quest 2','seguro', '128gb, vr headset, 2 touch controllers, power adapter, cabo carregador');
insert into Ferramenta values ('Mesa digitalizadora huion kamvans 13', 'seguro', 'Model gs1331. Creative pen display, cosmo black, s/n b5de6sh00652');
insert into Ferramenta values ('Intelligent 3D printing pen','seguro','Composicao: 1 caneta, 1 refil, 1 cabo, 1 copy board');
insert into Ferramenta values ('Intelligent 3D printing pen','seguro','Composicao: 1 caneta, 1 refil, 1 cabo, 1 copy board');
insert into Ferramenta values ('Kit Robotica', 'seguro', 'Master Kit Arduino');
insert into Ferramenta values ('Kit Robotica', 'seguro', 'Master Kit Arduino');
insert into Ferramenta values ('Furadeira de impacto profissional Bosch', 'pergigoso', 'Furadeira, liimitador de profundidade, chave de madril, empunhadeira auxiliar');



drop database sistemaApice;
create database sistemaApice;

use sistemaApice;
drop table `PI_WEB_emprestimo`;
drop table `PI_WEB_reserva`;