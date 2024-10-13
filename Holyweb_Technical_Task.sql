create table departments (
 id serial primary key not null,
 dep_name varchar
);
create table workers (
 id serial primary key not null,
 first_name varchar,
 department_id int,
 foreign key (department_id) references departments(id)
);
insert into departments(dep_name) values('developers');
insert into departments(dep_name) values('designers');
insert into departments(dep_name) values('foo');

insert into workers(first_name,department_id) values('vanya',1);
insert into workers(first_name,department_id) values('petya',2);


SELECT dep_name
FROM departments
LEFT JOIN workers
ON departments.id = workers.department_id
WHERE department_id IS NULL;