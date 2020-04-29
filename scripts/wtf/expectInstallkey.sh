#!/usr/bin/expect
set timeout 5
set ip [lindex $argv 0]
set passwd [lindex $argv 1]
spawn ssh-copy-id -i root@$ip
expect {
	"*yes/no" {send "yes\r"; exp_continue}
	"*password:" {send "$passwd\r" }
}
interact
