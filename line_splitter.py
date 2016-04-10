import io

msg = "NXST_FLOW reply (xid=0x4):\n cookie=0x0, duration=100.619s, table=0, n_packets=4, n_bytes=216, idle_age=35, ip,nw_proto=2 actions=CONTROLLER:65535\n cookie=0xd449, duration=81.304s, table=0, n_packets=161, n_bytes=89194, idle_age=0, ip,nw_src=10.0.0.7,nw_dst=224.1.1.1 actions=output:1\n cookie=0xd44a, duration=35.122s, table=0, n_packets=0, n_bytes=0, idle_age=35, ip,nw_src=10.0.0.7,nw_dst=224.1.1.2 actions=output:1\n cookie=0x0, duration=100.658s, table=0, n_packets=51, n_bytes=2091, idle_age=0, priority=65000,dl_dst=01:23:20:00:00:01,dl_type=0x88cc actions=CONTROLLER:65535\n"
mcast_ips = ['224.1.1.2','224.1.1.1']

lines = msg.split("\n")
no_of_flows = len(lines)-4
for line in range(0,(len(lines)-1)):
    for ip in mcast_ips:
        if ip in lines[line]:
            print lines[line]
            words = lines[line].strip().split();
            print(words[3])
            print(words[4])
            p1,p2 = words[3].split('=',1)
            p3,cnt = p2.split(',',1)
            print p3

print msg

