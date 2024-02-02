import logging
from jira import JIRA
from credentials import *
logger = logging.getLogger(__name__)

def printJira(jiraHost: str, jiraID: str) -> None:
    logger.debug("Connecting to Jira Host...")
    # Specify a server key. It should be your
    # domain name link. yourdomainname.atlassian.net
    jiraOptions = {'server': "https://"+jiraHost.strip()}
    (username, password) = getUsernamePassword("active-directory")
    jira = JIRA(options=jiraOptions, basic_auth=(username, password))
    logger.debug("Connecting to Jira Host Successful!")
    print(jiraID)
    issue  = jira.issue(jiraID)
    for field_name in issue.raw['fields']:
        print("Field:", field_name, "Value:", issue.raw['fields'][field_name])