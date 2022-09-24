<div align='center'>
    <h1>GW2-SRS: DATA MODELLING</h1>
</div>


This folder will be used to store and explain the modelling of GW2 data as well as the analysis of it. The objective is creating a database capable of containing all information needed. In this particular case, we will use MongoDB to store JSON files and SQLite so we can use SQL queries too.

- We will be using the normal Atlas Cluster for MongoDB. We will also use Compass to check data and VSCode extension for MongoDB databases.

- As for SQLite, we will use a tool called [DB Browser for SQLite](https://sqlitebrowser.org/), this tools let us write queries and check data as we desire.

Thanks to Excalidraw, I designed a small schema to explain how the route can be approached:

![SQL_schema](sql_schema.png 'SQL_schema')

---

#### Previous problems encountered
- The initial idea was using MySQL and PostgreSQL, however, MySQL has a password issue I couldn't resolve yet. As for PostgreSQL, its connection can be viable, nonetheless I need to investigate more as it seems that PostgreSQL syntax differs a bit from other SQL tools I used before.