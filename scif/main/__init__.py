'''

Copyright (C) 2017 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2017 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from scif.main.apps import ( app, apps, get_appenv )
from scif.main.base import ScifRecipe
from scif.main.environment import ( add_env, env, get_env, get_appenv )
from scif.main.helpers import run_command
from scif.main.preview import ( 
    preview, 
    preview_apps, 
    preview_base, 
    init_app_preview,
    preview_runscript,
    preview_labels,
    preview_environment,
    preview_files,
    preview_commands,
    preview_recipe
)
from scif.main.setup import ( install_base, set_base )
from scif.main.install import (
    init_app,
    install,
    install_apps,
    install_runscript,
    install_environment,
    install_labels,
    install_commands,
    install_files,
    install_recipe
)


# We can eventually add logic here for customizing the client


# Helpers
ScifRecipe._run_command = run_command
ScifRecipe.add_env = add_env
ScifRecipe.get_env = get_env

# Preview
ScifRecipe.preview = preview
ScifRecipe._preview_base = preview_base
ScifRecipe._init_app_preview = init_app_preview
ScifRecipe._preview_runscript = preview_runscript
ScifRecipe._preview_labels = preview_labels
ScifRecipe._preview_environment = preview_environment
ScifRecipe._preview_commands = preview_commands
ScifRecipe._preview_files = preview_files
ScifRecipe._preview_recipe = preview_recipe

# Setup
ScifRecipe._install_base = install_base
ScifRecipe.set_base = set_base

# Apps
ScifRecipe.get_appenv = get_appenv
ScifRecipe.app = app
ScifRecipe.apps = apps

# Installation
ScifRecipe.install = install
ScifRecipe._init_app = init_app
ScifRecipe._install_apps = install_apps
ScifRecipe._install_runscript = install_runscript
ScifRecipe._install_environment = install_environment
ScifRecipe._install_labels = install_labels
ScifRecipe._install_commands = install_commands
ScifRecipe._install_files = install_files
ScifRecipe._install_recipe = install_recipe