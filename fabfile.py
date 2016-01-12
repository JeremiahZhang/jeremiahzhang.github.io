# - * - coding:utf-8 -*-

from fabric.api import local

def post(name):
    local("./scripts/newpost %s" % name)

def tag():
    local("./scripts/generate-tags")