#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry point for all things, to avoid circular imports.
"""
import os
from .app import create_app
from .models import User, db
import myflaskapp.modules as modules

if __name__ == '__main__':
    # Get the environment setting from the system environment variable
    env = os.environ.get("MYFLASKAPP_ENV", "prod")
    app = create_app("myflaskapp.settings.{env}Config"
                        .format(env=env.capitalize()), env)