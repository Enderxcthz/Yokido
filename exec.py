import io

from discomaton.factories import bookbinding

from neko2.shared import commands
from neko2.shared import traits


from . import tools
from .toolchains import coliru


class ColiruCog(traits.CogTraits):
    @commands.group(
        invoke_without_command=True,
        name='coliru', aliases=['cc'],
        brief='Attempts to execute the given code using '
              '[coliru](http://coliru.stacked-crooked.com).')
    async def coliru(self, ctx, *, arguments):
        """
        Attempts to execute some code by detecting the language in the
        syntax highlighting. You MUST format the code using markdown-formatted
        code blocks. Please, please, PLEASE read this before saying "it is
        broken!"
        Run `cc help` to view a list of the supported languages, or
        `cc help <lang>` to view the help for a specific language.
        If you want to upload more than one file, or you wish to specify a
        custom build routine or flags, see `cc a`.
        """

        code_block = tools.code_block_re.search(arguments)

        if not code_block or len(code_block.groups()) < 2:
            booklet = bookbinding.StringBookBinder(ctx)
            booklet.add_line('I couldn\'t detect a valid language in your '
                             'syntax highlighting... try again by editing '
                             'your initial message.')
            booklet = booklet.build()
            booklet.start()

            return await tools.listen_to_edit(ctx, booklet)

        # Extract the code
        language, source = code_block.groups()
        language = language.lower()

        try:
            with ctx.typing():
                output = await coliru.targets[language](source)
        except KeyError:
            booklet = bookbinding.StringBookBinder(ctx)
            booklet.add_line(f'That language ({language}) is not yet supported'
                             ' by this toolchain. Feel free to edit your'
                             ' message if you wish to do something else.')
            booklet = booklet.build()
            booklet.start()

            await tools.listen_to_edit(ctx, booklet)
        else:
            binder = bookbinding.StringBookBinder(ctx,
                                                  prefix='```markdown',
                                                  suffix='```',
                                                  max_lines=25)

            binder.add_line(f'Interpreting as {language!r} source.')

            for line in output.split('\n'):
                binder.add_line(line, dont_alter=True)

            if ctx.invoked_with in ('ccd', 'colirud'):
                await commands.try_delete(ctx)

            if len(output.strip()) == 0:
                await ctx.send('No output...')
                return

            booklet = binder.build()
            booklet.start()

            await tools.listen_to_edit(ctx, booklet)
