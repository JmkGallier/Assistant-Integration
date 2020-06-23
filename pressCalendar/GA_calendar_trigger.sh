#!/usr/bin/expect -f

set timeout 60
set repo_dir [lindex $argv 0];
set proj_id [lindex $argv 1];
set mod_id [lindex $argv 2];

spawn googlesamples-assistant-pushtotalk --project-id $mod_id --device-model-id $proj_id -v

expect {
	"*Press Enter to send a new request...*" {
	    exec /bin/bash $repo_dir/AsstIntegration -s virtmic_config
	    send -- "\r"
	    exec /bin/bash $repo_dir/AsstIntegration -s virtmic_play
	    exec /bin/bash $repo_dir/AsstIntegration -s virtmic_undo
	    exp_continue
	}

	"*microphone_mode: CLOSE_MICROPHONE*" {
	    after 2000
	    send \x03
	}

	eof {
        exit 0
	}

	timeout {
	    exit 100
	}
}
