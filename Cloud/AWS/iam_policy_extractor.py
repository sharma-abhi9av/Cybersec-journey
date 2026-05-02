import boto3 
import json
scan_data = []
all_roles =""
iam_client = boto3.client('iam')
roles = iam_client.list_roles()

for index in roles["Roles"]:
    
    #print(index["RoleName"])
    rolename =index["RoleName"]
    policies = iam_client.list_attached_role_policies(RoleName=rolename)
    role_package = {
    "RoleName": rolename,
    "Policies": policies["AttachedPolicies"]
}
    
    scan_data.append(role_package)
    
    #print(policies)
with open('aws_hound_data.json', 'w') as f:
    json.dump(scan_data, f, indent=4, sort_keys=True)
