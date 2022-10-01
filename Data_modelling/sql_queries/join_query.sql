DROP VIEW if EXISTS qadim2_table;

CREATE VIEW prlqadim_table AS
SELECT DISTINCT
	player_info.name,
	player_info.account,
	bosses.boss,
	profession.professions,
	prlqadim_dps.phase1_dps,
	prlqadim_dps.phase2_dps,
	prlqadim_dps.phase3_dps,
	prlqadim_dps.phase4_dps,
	prlqadim_dps.phase5_dps,
	prlqadim_dps.phase6_dps
FROM player_info JOIN bosses JOIN profession JOIN prlqadim_dps on player_info.boss_id = bosses.id AND player_info.profession_id = profession.id AND player_info.account = prlqadim_dps.FK_player_id
WHERE boss like 'Qadim the%';