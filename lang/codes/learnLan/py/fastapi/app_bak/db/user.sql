create table if not exists `users` (
    `user_id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `password` VARCHAR(128) NOT NULL,
    `role` VARCHAR(128) NOT NULL,
    `status` CHAR(10) NOT NULL,
    `ctime` DATE,
    PRIMARY KEY (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;