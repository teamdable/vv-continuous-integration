from slackboy import SlackBoy

class SlackReporter:
    def __init__(self, token: str, channel: str, prefix: str, repository: str,
                 branch: str, target: str, pr_number: str, tag: str):
        self.client = SlackBoy.from_token(token)
        self.client.add_default_channel(channel)
        self.prefix = prefix
        self.repository = repository
        self.branch = branch
        self.target = target
        self.pr_number = pr_number
        self.tag = tag

    def get_pull_request_url(self) -> str:
        return f'https://github.com/teamdable/{self.repository}/pull/{self.pr_number}'


    def get_slack_message(self, msg: str) -> str:
        return (
            f'*Repository: {self.repository}* \n\n'
            '*Pull-request info:*\n'
            f'- branch: {self.branch} -> {self.target}\n'
            f'- url: {self.get_pull_request_url()}\n\n'
            f'```{msg}```\n'
            f'tag: {self.tag}_WARNING'
        )


    def send_slack_message(self, msg: str):
        message = self.get_slack_message(msg)
        self.client.send_message(msg=message, prefix=self.prefix)
