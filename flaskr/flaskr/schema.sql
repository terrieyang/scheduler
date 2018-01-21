drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'names' text not null,
  'chores' text not null,
  'constraints' text,
  'weeks' integer
);