DOIT_CONFIG = {'default_tasks': ['updatebabel', 'compilebabel', 'test']}


def task_cleanup():
    return {
            'actions': ['rm po/solve_line.pot',
                        'rm po/ru/LC_MESSAGES/solve_line.mo']
    }


def task_extractandinitbabel():
    return {
            'actions': ['pybabel extract -o po/solve_line.pot solve_line.py',
                        'pybabel init -D solve_line -i po/solve_line.pot -d po -l ru'],
            'targets': ['po/solve_line.pot']
    }


def task_updatebabel():
    return {
            'actions': ['pybabel update -D solve_line -i po/solve_line.pot -d po -l ru'],
            'file_dep': ['solve_line.py'],
            'targets': ['po/ru/LC_MESSAGES/solve_line.po']
    }


def task_compilebabel():
    return {
            'actions': ['pybabel compile -D solve_line -d po -l ru'],
            'file_dep': ['po/ru/LC_MESSAGES/solve_line.po'],
            'targets': ['po/ru/LC_MESSAGES/solve_line.mo']
    }


def task_test():
    return {
            'actions': ['python3 -m unittest']
    }