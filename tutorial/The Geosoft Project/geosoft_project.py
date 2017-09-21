import geosoft.gxpy.project as gxpj

def rungx():
    project = gxpj.Geosoft_project()
    gxpj.user_message("Project name: {}".format(project.name),
                      "Project user: {}".format(project.gid))