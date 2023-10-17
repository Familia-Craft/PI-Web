use sistemaApice;
drop trigger if exists DefineGrupoServidor;
create trigger DefineGrupoServidor after insert on PI_WEB_servidor
for each row 
begin 
    declare user int;
    select u.user_id into user
    from PI_WEB_usuario u
    where u.ra = new.usuario_ptr_id;

    if (new.funcao = 'B') then 
        insert into auth_user_groups (user_id, group_id) values (user, 1);
    else 
        insert into auth_user_groups (user_id, group_id) values (user, 2);
    end if;
end;