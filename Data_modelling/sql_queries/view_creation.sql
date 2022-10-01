--DROP VIEW if exists gorseval_table;

CREATE VIEW sab_table AS
SELECT DISTINCT
	player_info.name,
	player_info.account,
	bosses.boss,
	profession.professions,
	sab_dps.phase1_dps,
	sab_dps.phase2_dps,
	sab_dps.phase3_dps,
	sab_dps.phase4_dps
FROM player_info JOIN bosses JOIN profession JOIN sab_dps on player_info.boss_id = bosses.id AND player_info.profession_id = profession.id AND player_info.account = sab_dps.FK_player_id
WHERE boss like 'Sabet%';