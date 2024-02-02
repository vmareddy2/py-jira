from createJIRAFromFile import *
from printJira import *
import argparse
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='py-jira',
        description='Python for Jira',
        epilog='Text at the bottom of help')
    parser.add_argument("--createJiraFromFile",action='store_true',help="this will create jiras",required=False)
    parser.add_argument("--printJira", action='store_true',help="this will print jira",required=False)
    parser.add_argument("--hostname",type=str,dest="jiraHost",help="Jira Host name will prepend https://",required=True)
    parser.add_argument("--file",type=str,dest="file",help="file to update",required=False)
    parser.add_argument("--jira",type=str,dest="jira",help="file to update",required=False)
    parser.add_argument('-d', '--debug',
                        action='store_true')
    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)

    logger.debug(f"Arguments passed = {args}")

    # this is to create jira
    if args.createJiraFromFile:
        if args.file is None:
            print("ERROR: File needs to be specified")
            exit(1)
        createJIRAFromFile(args.jiraHost, args.file)
    # this is to print jira
    elif args.printJira:
        if args.jira is None:
            print("ERROR: Jira needs to be specified")
            exit(1)
        printJira(args.jiraHost, args.jira)
