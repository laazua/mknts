#!/usr/bin/expect

set ipaddres [lindex $argv 0]
set username [lindex $argv 1]
set password [lindex $argv 2]
set rootpass [lindex $argv 3]
set timeout 20

spawn ssh $username@$ipaddres
expect {
    "yes/no" {send "yse\r";exp_continue}
    "*password" {send "$password\r";exp_continue}
    "*]$" {send "su - root\r"}
}

expect "Password"
send "$rootpass\r"
expect "*]#"
send "chmod 777 /tmp/linux_check.sh\r"
send "sh /tmp/linux_check.sh\r"
send "exit\r"
send "exit\r"
interact
