
from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Any, List, Type


@dataclass(frozen=True)
class Campaign:
    name: str
    channel: str
    daily_budget: float
    start_date: date
    end_date: Optional[date]
    target_audience: Dict[str, Any]
    creatives: List[Dict[str, str]]
    tracking: Dict[str, str]


class CampaignBuilder:
    def __init__(self):
        self.name = None
        self.channel = None
        self.daily_budget = None
        self.start_date = None
        self.end_date = None
        self.target_audience = None
        self.creatives = None
        self.tracking = None

    def with_name(self, name: str):
      self.name = name
      return self

    def with_channel(self, channel: str):
      self.channel = channel
      return self

    def with_budget(self, daily_budget: float):
      self.daily_budget = daily_budget
      return self

    def with_dates(self, start_date, end_date=None):
      self.start_date = start_date
      self.end_date = end_date
      return self

    def with_audience(self, **kwargs):
      self.target_audience = {
          **kwargs
      }
      return self

    def add_creative(self, headline: str, image_url: str):
      self.creatives = [{
          'headline': headline,
          'image_url': image_url
      }]
      return self

    def with_tracking(self, **kwargs):
        self.tracking = {
            **kwargs
        }
        return self

    def build(self) -> Campaign:
      if not self.name:
        raise ValueError('Add name as string')

      if not self.channel:
        raise ValueError('Add channel as string')

      if self.daily_budget < 0:
        raise ValueError('Budget must be positive')

      if self.end_date and self.start_date > self.end_date:
        raise ValueError('start date must be before end date')

      if not self.creatives:
          raise ValueError('Add creative as string')

      if not self.creatives[0]['headline'] and not self.creatives[0]['image_url']:
          raise ValueError

      # TODO: Validations and return Campaign instance
      return Campaign(
          self.name,
          self.channel,
          self.daily_budget,
          self.start_date,
          self.end_date,
          self.target_audience,
          self.creatives,
          self.tracking
      )
