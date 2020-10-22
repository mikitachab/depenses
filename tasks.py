import invoke


@invoke.task
def reformat(c):
    c.run("black --exclude=migrations --exclude=node_modules .")
