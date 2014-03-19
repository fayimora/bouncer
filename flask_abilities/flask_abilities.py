from flask import g



_temp_ability_cache = None

def requires_ability(*args):

    def decorator(f):
        print "args: ", args
        global _temp_ability_cache
        if _temp_ability_cache is None:
            _temp_ability_cache = dict()

        _temp_ability_cache.setdefault(f.__name__, list())
        _temp_ability_cache[f.__name__].append(args)

        return f

    return decorator


class AbilityManager(object):
    """Thie class is used to control the Abilities Integration to one or more Flask applications"""

    def __init__(self, app):
        self.app = app
        self.init_app(app)

        self.authorization_target_callback = None

        self.authorization_method_callback = None


    def init_app(self,app):
        # I am sure that we will need to put something in here soon
        app.before_request(self.check_abilities)

    def authorization_target(self, callback):
        """
        the callback for finding the currentuser in the given request context.
        should return `None` if the user does not exist
        """
        self.authorization_target_callback = callback
        return callback

    def authorization_method(self, callback):
        """
        the callback for defining user abilities
        """
        self.authorization_method_callback = callback
        return callback

    def check_abilities(self):
        pass
