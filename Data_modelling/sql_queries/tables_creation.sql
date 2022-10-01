CREATE TABLE bosses(
'id' INTEGER PRIMARY KEY AUTOINCREMENT not null unique,
'boss' text
);
CREATE TABLE professions(
'id' INTEGER PRIMARY KEY AUTOINCREMENT not null unique,
'professions' text
);
CREATE TABLE name_account_id(
'id' INTEGER PRIMARY KEY AUTOINCREMENT not null unique,
'name' text,
'account' text
);
CREATE TABLE group_id(
'id' INTEGER PRIMARY KEY AUTOINCREMENT not null unique,
'group' integer
);