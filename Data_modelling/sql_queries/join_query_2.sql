SELECT
	name,
	account,
	bosses.boss,
	profession.professions,
	dhuum_dps.main_fight_dps,
	dhuum_dps.dhuum_fight_dps,
	dhuum_dps.ritual_dps
FROM player_info JOIN bosses JOIN profession JOIN dhuum_dps ON player_info.boss_id = bosses.id AND player_info.profession_id = profession.id
	AND player_info.account = dhuum_dps.FK_player_id
WHERE boss = 'Dhuum';