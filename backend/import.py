from server.interactions_administration import InteractionAdministration

try:
    adm = InteractionsAdministration()
    adm.import_interaction_data()
    adm.import_metadata()
except:
    print('Some error...')
