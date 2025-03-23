from colorama import Fore, Style

event_list = {
    "PushEvent": "pushed",
    "PullRequestEvent": "opened a pull request in",
    "CommitCommentEvent": "added a commit comment in",
    "CreateEvent": "created",
    "DeleteEvent": "deleted",
    "ForkEvent": "forked",
    "WatchEvent": "starred",
    "PullRequestReviewEvent": "reviewed a pull request in",
    "IssueCommentEvent": "commented on an issue in",
    "PublicEvent": "made public",
}

event_colors = {
    "PushEvent": Fore.BLUE,
    "PullRequestEvent": Fore.BLUE,
    "CommitCommentEvent": Fore.BLUE,
    "CreateEvent": Fore.GREEN,
    "DeleteEvent": Fore.RED,
    "ForkEvent": Fore.YELLOW,
    "WatchEvent": Fore.LIGHTYELLOW_EX,
    "PullRequestReviewEvent": Fore.CYAN,
    "IssueCommentEvent": Fore.CYAN,
    "PublicEvent": Fore.MAGENTA,
}
