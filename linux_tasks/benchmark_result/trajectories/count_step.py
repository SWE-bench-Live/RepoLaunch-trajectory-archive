import os

base = "/home/v-rongzhili/code/comparison/SWE-bench-Live/launch/data/comparison/playground"

setup_steps=0
setup_count=0
organize_steps=0
organize_count=0

for instance_id in os.listdir(base):
    if os.path.exists(f"{base}/{instance_id}/setup.log"):
        with open(f"{base}/{instance_id}/setup.log") as f:
            text = f.read()
        if "----------Start rebuild conversation----------" in text:
            parts = text.split("----------Start rebuild conversation----------")
            setup = parts[0]
            organize = "".join(parts[1:])
            organize = organize.split("----------Start unit test conversation----------")[0]
            setup_count += 1
            organize_count += 1
            setup_steps += setup.count("================================== Ai Message ==================================")
            organize_steps += organize.count("================================== Ai Message ==================================")/1.5
        else:
            setup_count += 1
            setup_steps += text.count("================================== Ai Message ==================================")

print("setup", setup_steps, setup_count, setup_steps/setup_count)
print("organize", organize_steps, organize_count, organize_steps/organize_count)
            