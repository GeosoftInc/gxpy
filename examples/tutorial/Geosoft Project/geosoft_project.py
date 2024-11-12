#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxpy.project as gxpj

def rungx():
    project = gxpj.Geosoft_project()
    gxpj.user_message("Project name: {}".format(project.name),
                      "Project user: {}".format(project.gid))