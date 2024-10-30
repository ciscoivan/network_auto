import textfsm
traceroute = '''
<R1>tracert 192.5.5.5
tracert 192.5.5.5
 traceroute to  192.5.5.5(192.5.5.5), max hops: 30 ,packet length: 40,press CTRL_C to break 
 1 36.1.1.6 60 ms  50 ms  10 ms 
 2 67.1.1.7 100 ms  90 ms  80 ms 
 3 78.1.1.8 90 ms  80 ms  60 ms 
 4 59.1.1.9 100 ms  90 ms  80 ms 
 5 59.1.1.5 90 ms  100 ms  60 ms
'''

with open('traceroute.template') as f:
    fsm = textfsm.TextFSM(f)
    result  = fsm.ParseText(traceroute)
    print(result)
    print(fsm.header)
    result = textfsm.TextFSM(f).ParseText(traceroute)
    print(result)