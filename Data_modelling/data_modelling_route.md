<div align='center'>
    <h1>GW2-SRS: DATA MODELLING</h1>
</div>


This folder will be used to store and explain the modelling of GW2 data as well as the analysis of it. The objective is creating a database capable of containing all information needed. In this particular case, we will use MongoDB to store JSON files and SQLite so we can use SQL queries too.

- We will be using the normal Atlas Cluster for MongoDB. We will also use Compass to check data and VSCode extension for MongoDB databases.

- As for SQLite, we will use a tool called [DB Browser for SQLite](https://sqlitebrowser.org/), this tools let us write queries and check data as we desire.

Thanks to Excalidraw, I designed a small schema to explain how the route can be approached:

![SQL_schema](sql_schema.png 'SQL_schema')

#### Data schema:
- **Name + Account table**: 1-to-N relationship
- **DPS table**: N-to-N relationship

#### Queries:
Logs contains a lot of data, therefore, after the first cleaning, another cleaning is needed for the final data to be analyzed. As an example, let's explore this Deimos logs:

<pre><code>
SELECT
	player_info.name,
	player_info.account,
	bosses.boss,
	profession.professions,
	dei_dps._100to10,
	dei_dps._10to0
FROM player_info JOIN bosses JOIN profession JOIN dei_dps on player_info.boss_id = bosses.id AND player_info.profession_id = profession.id AND player_info.id = dei_dps.id

WHERE name NOT like 'Saul%' AND _100to10 !=0 AND _10to0 !=0;
</code></pre>

This query will display six columns: names, accounts, boss by its ID, profession by its ID and both Deimos dps phases.
We must have in mind that, in Deimos, Saul D'Alesio (an NPC) will help us, but in the end, he is not worth the analysis since he will always display 0 dps in both phases, even if he actually does damage during the match.

We will end up with a csv like this:

![deimos_csv](dei_csv.png 'dei_csv')

We can now use this and create graphs using Pandas, Seaborn, Matplotlib, etc...

#### Updated queries
Using IDs is normally the way developers make sure they connected the PK(Primary Key) of a customer or client in a table *clients*, to a FK(Foreign Key) in another table. If we ended up doing that on this specific ETL we will end up getting an error, and this is how I managed to work it out:

- We must have something in consideration; since all the information is coming from an ETL source, it cannot really apply a unique ID until it is loaded into the SQL table having the AUTO-INCREMENT and UNIQUE constrains.
- Therefore, this means I created several tables:
  + A table for players, accounts, professions and unique IDs
  + Two tables, one for bosses and it's unique IDs and one for professions with the same idea. The objective is not repeating data that could already be stored in a table, therefore, we can refer this tables as FKs.
  + Multiple DPS tables referring to every boss

Is here when I started to have problems. The DPS tables stored data based on an ID as well, but if *JohnDoe.9100* had ID 30 on the players table and his damage in Vale Guardian actual corresponds to ID 2 it wouldn't work at all, there was no connection and therefore it leads to error.

The solution was not what I would have done if I had other options in mind, however, it worked fine. I created a FK for every dps table that contained the user account, this way we could just refer the FK to the players table and get the connection done. I thought on doing it with the boss number, but it could also resulted in some problems.

This choice was mainly done because we use ID as a unique value that represents something, and actually, in a game, your account name is already a unique value that identifies the player and it's also **immutable**.

![foreign key](fk_shot.png 'foreign_key')

We end up with a table like this one:

![adina_table](adina_ex.png 'adina')
---

#### Previous problems encountered
- The initial idea was using MySQL and PostgreSQL, however, MySQL has a password issue I couldn't resolve yet. As for PostgreSQL, its connection can be viable, nonetheless I need to investigate more as it seems that PostgreSQL syntax differs a bit from other SQL tools I used before.