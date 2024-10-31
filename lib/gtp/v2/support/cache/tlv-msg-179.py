ies = []
ies.append({ "ie_type" : "IP Address", "ie_value" : "PGW S5/S8 IP Address for Control Plane or PMIP", "presence" : "M", "instance" : "0", "comment" : ""})
ies.append({ "ie_type" : "IP Address", "ie_value" : "SGW S11/S4 IP Address for Control Plane", "presence" : "M", "instance" : "1", "comment" : ""})
ies.append({ "ie_type" : "Cause", "ie_value" : "Cause", "presence" : "CO", "instance" : "0", "comment" : "The SGW shall send the Cause IE with the value PGW not responding if it sends the PGW Restart Notification to notify that the peer PGW has failed and not restarted."})
msg_list[key]["ies"] = ies
