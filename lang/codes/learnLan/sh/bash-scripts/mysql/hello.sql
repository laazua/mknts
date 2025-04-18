-- 建表
CREATE TABLE IF NOT EXISTS `mds_server`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `gameAlias` VARCHAR(64) NOT NULL,
   `agent` VARCHAR(128) NOT NULL,
   `serverId` INT NOT NULL,
	 `serverIp` VARCHAR(64) NOT NULL,
	 `gamePort` INT NOT NULL,
	 `gameDbUrl` VARCHAR(128) NOT NULL,
	 `gameDbPort` INT NOT NULL,
	 `gameDbName` VARCHAR(128) NOT NULL,
	 `gameDir` VARCHAR(128) NOT NULL,
	 `isCombined` TINYINT NOT NULL,
	 `backEndVersion` INT NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;