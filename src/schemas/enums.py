from enum import StrEnum


class EnumRequestStatus(StrEnum):
    created = "created"
    in_work = "in_work"
    completed = "completed"
    closed = "closed"


class EnumResponseType(StrEnum):
    apply = "Apply"
    denied = "Denied"


class EnumStageType(StrEnum):
    open = "open"
    studied = "studied"
    interview = "interview"
    interview_complete = "interview complete"
    technical_interview = "technical interview"
    technical_complete = "passed a technical interview"
    offer = "send_offer"


class EnumPositionType(StrEnum):
    hr = "HR"
    team_lead = "Team Lead HR"


class EnumOrderByType(StrEnum):
    ascending = "ascending"
    descending = "descending"


class EnumRequestType(StrEnum):
    telegram = "telegram"
    web = "web"
