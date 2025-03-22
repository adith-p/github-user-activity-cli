# github-user-activity-cli

https://roadmap.sh/projects/github-user-activity

A Python script to fetch and display recent GitHub activity for a given user.

## Features

- Fetches public GitHub events for a specified user.
- Tracks and categorizes different event types:
  - **Push Events** (commits pushed to repositories)
  - **Pull Request Events** (opened pull requests)
  - **Commit Comments** (comments added to commits)
  - **Repository Creation/Deletion**
  - **Forks** (repositories forked by the user)
  - **Stars** (repositories starred by the user)
- Displays a summary of the user's GitHub activity in a structured format.


## Usage

Run the script with a GitHub username as an argument:

```sh
python script.py <github_username>
```

Example:

```sh
python script.py octocat
```

## Output Format

```
Output:
-- pushed 3 commits to repo-name
-- opened a pull request in repo-name
-- starred repo-name
-- forked repo-name to new-repo-name
-- created branch in repo-name
```

## Error Handling

- If the username is missing, the script prompts for input.
- If the username does not exist, it returns an error message.

