from enum import Enum, unique


@unique
class ProjectStatus(Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    STOPED = "STOPED"
    ON_TECHNICAL_MAINTENANCE = "ON_TECHNICAL_MAINTENANCE"
