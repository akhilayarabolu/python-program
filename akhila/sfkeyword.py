# y.akhila
# sfkeyword program
import keyword

print("Soft Keywords:")
print(keyword.softkwlist)

print("Hard Keywords:")
for k in keyword.kwlist:
    if k not in keyword.softkwlist:
        print(k)