import os

CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))

mem=str(os.popen('free -t -m').readlines())#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
"""
Get a whole line of memory output, it will be something like below
['             total       used       free     shared    buffers     cached\n', 
'Mem:           925        591        334         14         30        355\n', 
'-/+ buffers/cache:        205        719\n', 
'Swap:           99          0         99\n', 
'Total:        1025        591        434\n']
 So, we need total memory, usage and free memory.
 We should find the index of capital T which is unique at this string
"""#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
T_ind=mem.index('T')#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
"""
Than, we can recreate the string with this information. After T we have,
"Total:        " which has 14 characters, so we can start from index of T +14
and last 4 characters are also not necessary.
We can create a new sub-string using this information
"""#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
mem_G=mem[T_ind+14:-4]#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
"""
The result will be like
1025        603        422
we need to find first index of the first space, and we can start our substring
from from 0 to this index number, this will give us the string of total memory
"""#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
S1_ind=mem_G.index(' ')#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
mem_T=mem_G[0:S1_ind]#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
"""
Similarly we will create a new sub-string, which will start at the second value. 
The resulting string will be like
603        422
Again, we should find the index of first space and than the 
take the Used Memory and Free memory.
"""#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
mem_G1=mem_G[S1_ind+8:]#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
S2_ind=mem_G1.index(' ')#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349
mem_U=mem_G1[0:S2_ind]#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349

mem_F=mem_G1[S2_ind+8:]#NOT MY CODE: ITS FROM - https://stackoverflow.com/a/42249349