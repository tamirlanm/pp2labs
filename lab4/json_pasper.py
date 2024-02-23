import json

# Sample JSON data
data = '''
{
  "topology": {
    "pod-1": {
      "node-201": {
        "sys": {
          "phys": {
            "eth1/33": {"admin_state": "up", "link_speed": "10000", "mtu": 9150},
            "eth1/34": {"admin_state": "up", "link_speed": "10000", "mtu": 9150},
            "eth1/35": {"admin_state": "up", "link_speed": "10000", "mtu": 9150}
          }
        }
      }
    }
  }
}
'''

# Parse JSON data
parsed_data = json.loads(data)

# Extract relevant information
interface_data = []
for interface, details in parsed_data["topology"]["pod-1"]["node-201"]["sys"]["phys"].items():
    interface_data.append({
        "DN": f"topology/pod-1/node-201/sys/phys-[{interface}]",
        "Description": "inherit",
        "Speed": details["link_speed"],
        "MTU": details["mtu"]
    })

# Print the output in the desired format
print("Interface Status")
print("================================================================================")
print("{:50} {:20} {:7} {:7}".format("DN", "Description", "Speed", "MTU"))
print("-------------------------------------------------- --------------------  ------  ------")
for interface in interface_data:
    print("{:50} {:20} {:7} {:7}".format(interface["DN"], interface["Description"], interface["Speed"], interface["MTU"]))
