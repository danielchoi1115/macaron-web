from pydantic import BaseModel
from datetime import datetime


class Server(BaseModel):
    server_name: str = None
    description: str = None
    server_deployer: str = None
    game_server_tag: str = None
    macaron_tag: str = None
    created_at: datetime = None

    class Config:
        orm_mode = True

    def to_relative_time(self):
        mins = int((datetime.now() - self.created_at).total_seconds() / 60)
        if mins >= 1051200:  # 2년
            return f"{mins // 525600} years"
        elif mins >= 525600:  # 1년
            return f"1 year"
        elif mins >= 86400:  # 60일
            return f"{mins // 43200} months"
        elif mins >= 43200:  # 30일
            return f"1 month"
        elif mins >= 2880:  # 48시간
            return f"{mins//1440} days"
        elif mins >= 1440:  # 24시간
            return "1 day"
        elif mins >= 120:  # 1시간
            return f"{mins//60} hours"
        elif mins >= 60:  # 1시간
            return f"1 hour"
        elif mins >= 2:
            return f"{mins} minutes"
        elif mins >= 1:
            return f"1 minute"
        else:
            return "Just now"
