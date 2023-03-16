create table main.users
(
    id         integer primary key autoincrement ,
    first_name text,
    last_name  text,
    age        integer
);

create table main.publishing_house
(
    id         integer primary key autoincrement ,
    name  text,
    rating integer DEFAULT 5);


create table main.books
(
    id         integer primary key autoincrement ,
    title      text,
    author     text,
    year       integer,
    price      integer,
    publishing_house_id integer
);

create table main.purchases
(
    id         integer primary key autoincrement ,
    user_id     integer not null,
    book_id     integer not null,
    date        text,
    foreign key (book_id) references books(id),
    foreign key (user_id) references users(id)
);
