import sys
from turtle import back

import colorama
import requests
from colorama import Fore, Back, Style


def main():
    """
    Fetch and display the recent GitHub events of a user.

    This function:
    - Takes a GitHub username from command-line arguments.
    - Fetches the user's public event history from the GitHub API.
    - Parses the event types and counts their occurrences.
    - Displays a summary of the user's GitHub activity.

    Events tracked:
    - Pushes, pull requests, commits, repository creation/deletion, forks, and stars.

    Example usage:
        python main.py <github_username>

    Returns:
        None
    """
    colorama.init(autoreset=True)

    if len(sys.argv) < 2:
        print(Fore.RED + "please provide a username")
        return

    username = sys.argv[1]
    json_response = requests.get(f"https://api.github.com/users/{username}/events")
    json_file = json_response.json()

    if json_response.status_code == 404:
        print("data not found check the given username")
        return

    if not json_file:
        print("No recent activity found for this user.")
        return

    event_dict = {}

    event_list = {
        "PushEvent": "pushed ",
        "PullRequestEvent": "opened a pull request in",
        "CommitCommentEvent": "added a commit comment in",
        "CreateEvent": "created",
        "DeleteEvent": "deleted",
        "ForkEvent": "forked",
        "WatchEvent": "starred",
    }

    for items in json_file:
        event_dict[items["repo"]["name"]] = {
            "PushEvent": 0,
            "PullRequestEvent": 0,
            "CommitCommentEvent": 0,
            "CreateEvent": 0,
            "DeleteEvent": 0,
            "ForkEvent": 0,
            "WatchEvent": 0,
        }

    for items in json_file:
        for events in event_list.keys():
            if items["type"] == events:
                if items["type"] in ["CreateEvent", "DeleteEvent"]:
                    event_dict[items["repo"]["name"]][events] = items["payload"][
                        "ref_type"
                    ]
                    continue

                event_dict[items["repo"]["name"]][events] += 1
                continue

    print(f"{Fore.GREEN }Output:")
    for details, repo in event_dict.items():
        for event, values in repo.items():
            if event in event_list and values != 0:
                if event in ["WatchEvent", "PullRequestEvent"]:
                    print(
                        f"--{Fore.MAGENTA}{Style.BRIGHT} {event_list[event]} {Fore.WHITE}{Style.BRIGHT}{details}"
                    )
                elif event == "PushEvent":
                    print(
                        f"-- {Fore.BLUE}{Style.BRIGHT}{event_list[event]} {values} commits to {Fore.WHITE}{Style.BRIGHT} {details}"
                    )
                elif event == "CreateEvent":
                    print(
                        f"-- {event_list[event]} {Back.YELLOW}{Fore.BLACK}{values}{Style.RESET_ALL} named {details}"
                    )
                else:
                    print(f"-- {event_list[event]} {values} to {details}")


if __name__ == "__main__":
    main()
