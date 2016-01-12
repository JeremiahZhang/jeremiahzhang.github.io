# - * - coding:utf-8 -*-

from fabric.api import local

def post(name):
    local("./scripts/newpost %s" % name)

def tag():
    local("./scripts/generate-tags")

def pu(discribation):
    local("git ad")
    local("git ci -m '%s' " % discribation)
    local("git pu")