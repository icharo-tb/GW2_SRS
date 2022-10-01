SELECT 
	count(profession) as prof_count,
	profession,
	sum(phase_1_dps) as dps1,
	sum(phase_2_dps) as dps2,
	sum(phase_3_dps) as dps3

FROM cwxnqd2i3m_vg_player_stats

group by profession