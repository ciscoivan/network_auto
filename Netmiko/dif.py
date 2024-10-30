import re
import os
import difflib
tex1="""tex1:
this is a test for difflib ,just try to get difference of the log
现在试试功能是否可行 好呀
goodtest
那么试试吧好人
"""
tex1_lines=tex1.splitlines()
tex2="""tex2:
this is a test for difflib ,just try to get difference of the log
现在试试功能是否可行
goodtast
那么试试吧
"""
tex2_lines=tex2.splitlines()
print(tex1_lines)

d=difflib.HtmlDiff()
q=d.make_file(tex1_lines,tex2_lines)
old_str='charset=UTF-8'
new_str='charset=UTF-8'
with open('diff.html', 'w') as f_new:
	f_new.write(q.replace(old_str,new_str))