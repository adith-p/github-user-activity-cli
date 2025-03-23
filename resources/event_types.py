from colorama import Fore


event_list = {
    "PushEvent": "pushed ",
    "PullRequestEvent": "opened a pull request in",
    "CommitCommentEvent": "added a commit comment in",
    "CreateEvent": "created",
    "DeleteEvent": "deleted",
    "ForkEvent": "forked",
    "WatchEvent": "starred",
}

event_colors = {
    "PushEvent": Fore.BLUE,
    "PullRequestEvent": Fore.BLUE,
    "CommitCommentEvent": Fore.BLUE,
    "CreateEvent": Fore.GREEN,
    "DeleteEvent": Fore.RED,
    "ForkEvent": Fore.YELLOW,
    "WatchEvent": Fore.YELLOW,
}
