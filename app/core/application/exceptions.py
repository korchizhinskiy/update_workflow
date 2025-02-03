class ApplicationError(Exception):
    message: str = "Unknown error occurred"


class ObjectNotFoundError(ApplicationError):
    pass


class ProjectNotFoundError(ObjectNotFoundError):
    message: str = "Project doesn't find in system"
