from sys import argv
if len(argv) != 2:
    print("To use this script, drag and drop the .ct file on the script file")
    input("Press enter to exit")
with open(argv[1], "r") as f:
    c = f.read()
    if "<Address>3" in c:
        c = c.replace("RealAddress=\"3", "RealAddress=\"2")
        c = c.replace("<Address>3", "<Address>2")
        c = c.replace("<Offset>3", "<Offset>2")
    elif "<Address>2" in c:
        c = c.replace("RealAddress=\"2", "RealAddress=\"3")
        c = c.replace("<Address>2", "<Address>3")
        c = c.replace("<Offset>2", "<Offset>3")
    open(argv[1][:-3] + "- mod" + argv[1][-3:], "w").write(c)
