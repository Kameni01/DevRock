import gitlab


token = 'M8ovVDkkCHuzj_Td8Ty2'

gl = gitlab.Gitlab('http://10.0.0.1', private_token=token)
projects = gl.projects.list()
for project in projects:
    print(project)


project = gl.projects.get(1)
issues = project.issues.list()


boards = project_or_group.boards.list()

board = project_or_group.boards.create({'name': 'new-board'})
