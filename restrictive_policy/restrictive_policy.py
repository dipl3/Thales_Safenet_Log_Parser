import sys
import logging
import pymsteams
import requests
from datetime import *
from groups import groups
from clients import clients

# Configuration du logging et du message Teams
logging.basicConfig(filename='/home/adminsetup/logs/restrictive_policy.log', level=logging.DEBUG)
logging.debug('')
logging.debug(f'Script started at {datetime.now(timezone.utc)}')
logging.debug(f"Restritive mode '{sys.argv[1]}' for groups: {', '.join(sys.argv[2:])}")
teams_message = pymsteams.connectorcard('REDACTED')
teams_message.title('Politique de sécurité')
message_text = 'La politique de sécurité restrictive a été '

# On choisi la politique de sécurité en fonction du mode sélectionné
if sys.argv[1] == 'enable':
    policy_id = 'restrictivePolicyID'
else:
    policy_id = 'permissivePolicyID'
    message_text += 'dés'

message_text += 'activée pour les groupes suivants :\n'

# Si plusieurs noms de groupes sont spécifiés alors on récupère uniquement les informations de ces groupes
if len(sys.argv) > 2:
    groups_to_update = {}
    groups_name_to_update = sys.argv[2:]
    for group_name_to_update in groups_name_to_update:
        if group_name_to_update in groups:
            groups_to_update[group_name_to_update] = groups[group_name_to_update]
        else:
            logging.error(f'Group "{group_name_to_update}" is not in the supported client list')
else:
    groups_to_update = groups

send_message = False

if groups_to_update:
    for group_name, group_data in groups_to_update.items():
        if group_data['client'] in clients:
            # On construit la requête avec les infos du client
            client = clients[group_data['client']]
            logging.debug(f'Processing client: {group_name}')
            url = f"REDACTED"
            headers = {'authorization': client['apiKey']}
            logging.debug(f'URL used for request: {url}')

            # On modifie la politique de sécurité et on applique les automatisations sur la politique par défaut
            response = requests.post(url, headers=headers)
            logging.debug(f'Response Code: {response.status_code}')
            requests.post(f"REDACTED", headers=headers)

            # On log les infos de la réponse
            if response.status_code == 200:
                logging.info(f'Policy updated for {group_name}')
                message_text += f'- {group_name}\n'
                send_message = True
            else:
                logging.error(f'Failed to update policy for {group_name}, status code: {response.status_code}')
        else:
            logging.error(f"{group_name} policy's client name is not in the supported client list")

if send_message:
    teams_message.text(message_text)
    teams_message.send()
