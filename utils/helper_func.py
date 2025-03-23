def event_dict_extr(json_file):
    event_dict = {}
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
    return event_dict
