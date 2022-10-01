ALTER TABLE ca_dps
ADD COLUMN FK_player_id INTEGER REFERENCES player_info("id");
