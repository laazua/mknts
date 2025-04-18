-- create role table structure

CREATE TABLE IF NOT EXISTS `role` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;