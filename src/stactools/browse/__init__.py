def register_plugin(registry):
    # Register subcommands

    from stactools.browse import commands

    registry.register_subcommand(commands.browse_command)


__version__ = '0.1.6'
