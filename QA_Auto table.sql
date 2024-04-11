create schema QA_AUTO;
create table car_brands (
id int primary key auto_increment, 
title varchar (255) not null
);
create table car_models (
id int primary key auto_increment, 
carBrandId int, 
foreign key (carBrandId) references car_brands (id),
title varchar (255) not null
);
create table users (
id int primary key auto_increment, 
firstName varchar (255) not null, 
lastName varchar (255) not null, 
email varchar (255) not null, 
password varchar (255) not null
);
create table cars (
id int primary key auto_increment, 
userId int, 
foreign key (userId) references users (id),
carBrandId int, 
foreign key (carBrandId) references car_brands (id),
carModelId int, 
foreign key (carModelId) references car_models (id),
mileage float , 
initialMilleage float
);