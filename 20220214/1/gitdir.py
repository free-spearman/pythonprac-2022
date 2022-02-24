from os import listdir

PATHGITBRANCHES = '.git/refs/heads/'


def git_branches_show ():
    for branch in listdir(PATHGITBRANCHES):
        print(branch)


if ( __name__ == '__main__'):
    git_branches_show()
