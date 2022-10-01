<div align='center'>
    <h1>GW2-SRS: DATA MODELLING</h1>
</div>


This folder will be used to store and explain the modelling of GW2 data as well as the analysis of it. The objective is creating a database capable of containing all information needed. In this particular case, we will use MongoDB to store JSON files and SQLite so we can use SQL queries too.

- We will be using the normal Atlas Cluster for MongoDB. We will also use Compass to check data and VSCode extension for MongoDB databases.

- As for SQLite, we will use a tool called [DB Browser for SQLite](https://sqlitebrowser.org/), this tools let us write queries and check data as we desire.

Thanks to Excalidraw, I designed a small schema to explain how the route can be approached:

![SQL_schema](Data_modelling\pic_files\sql_schema.png 'SQL_schema')

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

![deimos_csv](Data_modelling\pic_files\dei_csv.png 'dei_csv')

We can now use this and create graphs using Pandas, Seaborn, Matplotlib, etc...

---

#### Previous problems encountered
- The initial idea was using MySQL and PostgreSQL, however, MySQL has a password issue I couldn't resolve yet. As for PostgreSQL, its connection can be viable, nonetheless I need to investigate more as it seems that PostgreSQL syntax differs a bit from other SQL tools I used before.