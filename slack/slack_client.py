import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from const import Channels, Users

load_dotenv()
token = os.getenv("SLACK_BOT_TOKEN")


def main():
    try:
        client = WebClient(token=token)
        slack_users = get_users(client=client)
        if slack_users:
            channel_id = create_channel(client=client, channel_name=Channels.NEW_CHANNEL)
            if channel_id:
                add_member_to_channel(client=client, channel=channel_id, user_id=Users.USER_TO_ADD)
                
    except Value as e:
        error_message = e.response.get('error', 'Unknown error')
        raise SlackApiError(f"Error: {error_message}")

def get_users(client: WebClient):
    try:
        response = client.users_list()
        if response['ok']:
            members = response['members']
            if members:
                slack_users = [{m['name']: m['id']} for m in members]
            return slack_users

    except SlackApiError as e:
        raise SlackApiError(f"Error get users: {e.response['error']}")


def create_channel(client: WebClient, channel_name: str):
    try:
        channels = channel_list(client=client)
        if channel_name not in channels:
            response = client.conversations_create(name=channel_name, is_private=False, team_id="T07EV5JUGV8")
            return response["channel"]["id"]

    except SlackApiError as e:
        raise SlackApiError(f"Error create channel: {e.response['error']}")


def channel_list(client: WebClient):
    try:
        response = client.conversations_list(team_id="T07EV5JUGV8")
        channel_list = response['channels']
        channel_names = [ch['name'] for ch in channel_list]
        return channel_names

    except SlackApiError as e:
        raise SlackApiError(f"Error list channels: {e.response['error']}")


def add_member_to_channel(client: WebClient, channel: str, user_id: str):
    try:
        client.conversations_invite(channel=channel, users=user_id)

    except SlackApiError as e:
        raise SlackApiError(f"Error add member to channel: {e.response['error']}")


if __name__ == "__main__":
    main()
