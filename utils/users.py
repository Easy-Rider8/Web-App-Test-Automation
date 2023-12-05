import json

# test data is stored in data folder with json files seperated for domain(test/local/prod)

# opening JSON file
test_data = open('testData/test_users.json')

# returns JSON object as a dictionary
data_extracted = json.load(test_data)

def get_user(roles):
    try:
        return next(user for user in data_extracted['users'] if user["role"] == roles)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % roles)
        
test_data.close()