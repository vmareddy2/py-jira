import logging
import csv
from jira import JIRA
from credentials import *
logger = logging.getLogger(__name__)


def createJira(jira, jira_project: str, jira_type: str, jira_summary: str, jira_description: str, jira_component: str, jira_epiclink: str) -> str:
    # Issue details
    issue_data = {
            "project": {
                "key": jira_project  # Replace with your Jira project key
            },
            "summary": jira_summary,
            "description": jira_description,
            "issuetype": {
                "name": jira_type
            },
            "components": [{
                "name": jira_component
            }],
            "customfield_10007": jira_epiclink
        }

    logger.debug("Creating issue with following fields:")
    logger.debug("\t issue_data: "+str(issue_data))

    # Create the Jira Epic issue
    try:
        jira_issue = jira.create_issue(fields=issue_data)
        logger.info(f'jira created successfully.  Key: {jira_issue.key}')
        return jira_issue.key
    except Exception as e:
        logger.error(f'Failed to create jira. Error: {str(e)}')
        raise

def writefile(file, lines):
    with open('file', 'w') as temp_file:
        temp_file.writelines(lines)


def createJIRAFromFile(jiraHost: str, file: str) -> None:
    logger.debug("Connecting to Jira Host...")
    # Specify a server key. It should be your
    # domain name link. yourdomainname.atlassian.net
    jiraOptions = {'server': "https://"+jiraHost.strip()}
    (username, password) = getUsernamePassword("active-directory")

    # Get a JIRA client instance, pass,
    # Authentication parameters
    # and the Server name.
    # emailID = your emailID
    # token = token you receive after registration
    jira = JIRA(options=jiraOptions, basic_auth=(username, password))
    logger.debug("Connecting to Jira Host Successful!")

    logger.debug("Reading csv file..")
    input_file_path = 'your_file.txt'

    # Open the file for reading
    with open(file, 'r', encoding='utf-8-sig') as input_file:
            lines = input_file.readlines()
            for i in range(1,len(lines)):
                line = lines[i]
                logger.debug("Processing line: "+line)
                (jira_num,jira_type,jira_summary,jira_description,jira_epiclink,jira_project,jira_component) = line.rstrip(",").split(",")

                if jira_num.strip() == "":
                    try:
                        jira_number = createJira(jira = jira, jira_project = jira_project.strip(), jira_type = jira_type.strip(), jira_summary = jira_summary.strip(), jira_description = jira_description.strip(), jira_component=jira_component.strip(), jira_epiclink=jira_epiclink.strip())
                        lines[i]=",".join([jira_number,jira_type,jira_summary,jira_description,jira_epiclink,jira_project,jira_component])
                    except Exception as e:
                        writefile(file+".tmp",lines)
                        logger.error(f'Failed to create jira. Error: {str(e)}')
                        raise

            writefile(file+".tmp",lines)