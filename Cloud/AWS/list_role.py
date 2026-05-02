import boto3 
iam_client = boto3.client('iam')

roles = iam_client.list_roles() # Here the roles is massive dictionary containing the entire API response (the Roles list, the IsTruncated status, the ResponseMetadata).
for index in roles["Roles"]:    # the for loop goes into the dictonary and then into the list of "Roles". 
    print(index["RoleName"])
