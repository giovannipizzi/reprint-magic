"""
Modele with the definition of the ``%%reprint`` magic
"""
from __future__ import absolute_import

from IPython.core.display import display, Markdown
from IPython.core import magic_arguments
from IPython.core.magic import  (
    Magics, magics_class, cell_magic
)

@magics_class
class ReprintMagics(Magics):
    """Magics for displaying various output types with literals.
    """

    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('--no-box', '-n',
          action='store_true',
          help='Do not show any box around the code'
    )
    def reprint(self, line, cell):
        """Both run the cell and print its content in output
        (via Markdown, rendered as python code)"""
        args = magic_arguments.parse_argstring(self.reprint, line)
        
        pre_box = '<div style="border: 1px solid #999; border-radius: 3px;">\n\n'
        post_box = "\n\n"
        if args.no_box:
            pre_box = ""
            post_box = ""
        
        display(Markdown("{}```python\n{}\n```{}".format(
            pre_box, cell, post_box)))
        self.shell.ex(cell)

if __name__ == "__main__":
    # This actually should be run inside a juptyer notebook (or in ipython)
    ip = get_ipython()
    ip.register_magics(ReprintMagics)
