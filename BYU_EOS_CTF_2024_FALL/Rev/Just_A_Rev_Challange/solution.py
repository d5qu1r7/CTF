import re

if_statements = """
iVar1 = strncmp(local_48,"byuctf{",7);
if (iVar1 == 0) {
  iVar1 = strncmp(acStack_3b,"bf",2);
  if (iVar1 == 0) {
    iVar1 = strncmp(acStack_37,"c4t",3);
    if (iVar1 == 0) {
      iVar1 = strncmp(acStack_29,"0l_",3);
      if (iVar1 == 0) {
        iVar1 = strncmp(acStack_3f,"ur",2);
        if (iVar1 == 0) {
          iVar1 = strncmp(acStack_2d,"t_",2);
          if (iVar1 == 0) {
            iVar1 = strncmp(acStack_39,"us",2);
            if (iVar1 == 0) {
              iVar1 = strncmp(acStack_41,"y0",2);
              if (iVar1 == 0) {
                iVar1 = strncmp(acStack_31,"_c4n",4);
                if (iVar1 == 0) {
                  iVar1 = strncmp(acStack_26,"m3}",3);
                  if (iVar1 == 0) {
                    iVar1 = strncmp(acStack_3d,"_0",2);
                    if (iVar1 == 0) {
                      iVar1 = strncmp(acStack_34,"i0n",3);
                      if (iVar1 == 0) {
                        iVar1 = strncmp(acStack_2b,"f0",2);
"""

# Extract the strings and positions
matches = re.findall(r'strncmp\((acStack_\w+),"(.*?)",', if_statements)

# Initialize variables
local_48 = "byuctf{"
acStack = {}

# Populate the acStack dictionary
for match in matches:
    position, string = match
    position = position.split('_')[1]
    acStack[position] = string

# Order the stack positions
ordered_keys = sorted(acStack.keys(), reverse=True)

# Construct the final string
result = local_48 + ''.join(acStack[key] for key in ordered_keys)

# Print the result
print(result)
