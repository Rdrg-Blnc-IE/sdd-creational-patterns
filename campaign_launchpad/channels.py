from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        GlobalBudget.allocate(GlobalBudget(), campaign.daily_budget)
        self.name = f'{self.name}-{uuid4().hex}'
        return self.name

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        pass


class GoogleAdsClient(ChannelClient):
    def create_campaign(self, campaign: Campaign) -> str:
        self.name = 'g'
        ChannelClient.create_campaign(self, campaign)
        return self.name

    def pause_campaign(self, campaign_id: str) -> None:
        pass

class FacebookAdsClient(ChannelClient):
    def create_campaign(self, campaign: Campaign) -> str:
        self.name = 'f'
        ChannelClient.create_campaign(self, campaign)
        return self.name


    def pause_campaign(self, campaign_id: str) -> None:
        pass

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
        if channel == 'google':
            channel_client = GoogleAdsClient(channel)
        elif channel == 'facebook':
            channel_client = FacebookAdsClient(channel)
        else:
            raise ValueError('Channel has to be google or facebook')

        return channel_client
