import  textfsm



with open('clock.template') as f , open('time_lci') as output:
   # re_table = textfsm.TextFSM(f)
   # result = re_table.ParseText(output.read())
    result2 = textfsm.TextFSM(f).ParseText(output.read())
   # print(result)
    print(result2)