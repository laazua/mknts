#!/usr/bin/expect

set timeout 30
if {$argc < 3} {
  puts "usage: hello ip agent zone"
  exit 1
}

set user  "root"
set pass  "123456"
set ip    [lindex $argv 0]
set agent [lindex $argv 1]
set zone  [lindex $argv 2]

spawn ssh $user@$ip
## 匹配其中的任意一个
expect {
  "*(yes/no)"   { send "yes\r"; exp_continue }
  "*password:"  { send "$pass\r" }
}
expect "\#?" {
  send "sh /home/gamecpp/.bana/open_serve.sh $agent $zone && exit\r"
}
expect eof