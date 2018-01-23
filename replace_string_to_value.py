# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:08:37 2018

@author: CAOJIE
"""
col_names = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment", "urgent", "host", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"]
num_features = ["duration", "src_bytes", "dst_bytes", "land", "wrong_fragment", "urgent", "host", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate"]
You_path_file = 'kddcup.txt' #add you filename in here
def countingFunction(type_into, name):
	s_c = 1
	f_c = 1
	p_c = 1
	protocol_type = ["tcp", "udp", "icmp"]
	#example TCP->1
	#example UDP->2
	#example ICMP->3
	service = ["aol", "auth", "bgp", "courier", "csnet_ns", "ctf", "daytime", "discard", "domain", "domain_u", "echo", "eco_i", "ecr_i", "efs", "exec", "finger", "ftp", "ftp_data", "gopher", "harvest", "hostnames", "http", "http_2784", "http_443", "http_8001", "imap4", "IRC", "iso_tsap", "klogin", "kshell", "ldap", "link", "login", "mtp", "name", "netbios_dgm", "netbios_ns", "netbios_ssn", "netstat", "nnsp", "nntp", "ntp_u", "other", "pm_dump", "pop_2", "pop_3", "printer", "private", "red_i", "remote_job", "rje", "shell", "smtp", "sql_net", "ssh", "sunrpc", "supdup", "systat", "telnet", "tftp_u", "tim_i", "time", "urh_i", "urp_i", "uucp", "uucp_path", "vmnet", "whois", "X11", "Z39_50"]
	#example aol->1
	#example Z39_50->70
	flag = ["OTH", "REJ", "RSTO", "RSTOS0", "RSTR", "S0", "S1", "S2", "S3", "SF", "SH"]
	#example OTH->1
	#example #SH->11
	
	if type_into == 3:
		for name_s in service:
			if name == name_s:
				return s_c
			else:
				s_c += 1
				
	elif type_into == 4:
		for name_f in flag:
			if name == name_f:
				return f_c
			else:
				f_c += 1
				
	elif type_into == 2:
		for name_p in protocol_type:
			if name_p == name:
				return p_c
			else:
				p_c += 1

def replace_kdd(into_string):
	cc_num = 1
	want_num = 0
	replace_list = []
	want_replace = [2, 3, 4, 99999]
	
	for i in into_string:
		if cc_num == want_replace[want_num]:
			get_the_value = countingFunction(cc_num, i)
			print (i, get_the_value)
			replace_list.append(str(get_the_value))
			cc_num += 1
			want_num += 1
		else:
			replace_list.append(i)
			cc_num += 1
	rep = ",".join(replace_list)
	return rep

def load_kdd():
	try:
		kdd_read = open(You_path_file, "r")
	except:
		print ('Can not open the file')		
	try:
		kdd_write = open("kddcup_10.txt", "a")
	except:
		print ('Can not open the re')
	kdd_readlines = kdd_read.readlines()
	for k in kdd_readlines:
		k_split = k.split(",")
		k_over = replace_kdd(k_split)
		kdd_write.writelines(k_over)
	kdd_read.close()
	kdd_write.close()

def main():
	load_kdd()

if __name__ == "__main__":
	main()
