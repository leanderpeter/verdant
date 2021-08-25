from server.interactions_administration import InteractionAdministration

try:
    adm = InteractionAdministration()
    adm.import_interaction_data()
    adm.import_metadata()
except Exception as e:
    print(e)
    print('Some error...')
