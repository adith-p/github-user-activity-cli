import sys
from turtle import back

import colorama
import requests
from colorama import Fore, Back, Style

from resources.event_types import event_list, event_colors
from utils.helper_func import event_dict_extr


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

    event_dict = event_dict_extr(json_file)

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
                event_color = event_colors.get(event, Fore.WHITE)
                # if event in ["WatchEvent", "PullRequestEvent"]:
                #     print(
                #         f"--{event_color}{Style.BRIGHT} {event_list[event]} {Fore.WHITE}{Style.BRIGHT}{details}"
                #     )
                # elif event == "PushEvent":
                #     print(
                #         f"-- {event_color}{Style.BRIGHT}{event_list[event]} {values} commits to {Fore.WHITE}{Style.BRIGHT} {details}"
                #     )
                # elif event == "CreateEvent":
                #     print(
                #         f"-- {event_color}{event_list[event]} {Back.YELLOW}{Fore.BLACK}{values}{Style.RESET_ALL} named {details}"
                #     )
                # else:
                #     print(f"-- {event_list[event]} {values} to {details}")
                if event in ["PushEvent", "CommitCommentEvent"]:
                    print(
                        f"-- {event_color}{Style.BRIGHT}{event_list[event]}{Style.RESET_ALL} {Fore.YELLOW}{values}{Style.RESET_ALL} commits to {Fore.WHITE}{Style.BRIGHT}{details}{Style.RESET_ALL}"
                    )
                elif event == "CreateEvent":
                    print(
                        f"-- {event_color}{Style.BRIGHT}{event_list[event]}{Style.RESET_ALL} {Fore.WHITE}{values}{Style.RESET_ALL} named {Fore.WHITE}{details}{Style.RESET_ALL}"
                    )
                elif event == "DeleteEvent":
                    print(
                        f"-- {event_color}{Style.BRIGHT}{event_list[event]}{Style.RESET_ALL} {Fore.RED}{values}{Style.RESET_ALL} from {Fore.WHITE}{details}{Style.RESET_ALL}"
                    )
                elif event in ["ForkEvent", "WatchEvent"]:
                    print(
                        f"-- {event_color}{Style.BRIGHT}{event_list[event]}{Style.RESET_ALL} {Fore.WHITE}{details}{Style.RESET_ALL}"
                    )
                else:
                    print(
                        f"-- {Fore.MAGENTA}{Style.BRIGHT}{event_list.get(event, 'performed an action in')}{Style.RESET_ALL} {Fore.YELLOW}{Style.RESET_ALL}{Fore.WHITE}{details}{Style.RESET_ALL}"
                    )


if __name__ == "__main__":
    main()
