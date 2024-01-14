import os
import sys

import logging
import sqlite3
from typing import Dict

from dependency_injector.wiring import Provide, inject
from dependency_injector import containers, providers


class BaseService:
    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )


class UserService(BaseService):
    def __init__(self, db: sqlite3.Connection) -> None:
        self.db = db
        super().__init__()

    def get_user(self, email: str) -> Dict[str, str]:
        self.logger.debug("User %s has been found in database", email)
        return {"email": email, "password_hash": "..."}


class AuthService(BaseService):
    def __init__(self, db: sqlite3.Connection, user_service: UserService) -> None:
        self.db = db
        self.user_service = user_service
        super().__init__()

    def authenticate(self, user: Dict[str, str], password: str) -> None:
        assert password is not None
        self.logger.debug(
            "User %s has been successfully authenticated",
            user["email"],
        )


class Container(containers.DeclarativeContainer):
    database_client = providers.Singleton(
        sqlite3.connect,
        os.environ["DATABASE__PATH"],
    )

    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        config.fileConfig,
        fname="logging.ini",
    )

    user_service = providers.Factory(
        UserService,
        db=database_client,
    )

    auth_service = providers.Factory(
        AuthService,
        user_service=user_service,
        db=database_client,
    )


@inject
def main(
        email: str,
        password: str,
        user_service: UserService = Provide[Container.user_service],
        auth_service: AuthService = Provide[Container.auth_service],
) -> None:
    user = user_service.get_user(email)
    auth_service.authenticate(user, password)


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main(*sys.argv[1:])
