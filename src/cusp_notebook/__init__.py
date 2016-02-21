import platform
import os
import shutil
from paste.script.templates import Template, var
from paste.util.template import paste_script_template_renderer

class CUSPNotebookTemplate(Template):
    _template_dir = 'template'
    summary = "Paster Template for CUSP iPython Notebooks"
    vars = []

    template_renderer = staticmethod(paste_script_template_renderer)

    def pre(self, command, output_dir, vars):
        vars['full_version'] = platform.python_version()
        vars['major_version'] = vars['full_version'].split(".")[0]

    def post(self, command, output_dir, vars):
        filename = "%s.ipynb" % vars['package']
        filepath = os.path.join(os.getcwd(), filename)

        if os.path.exists(filepath):
            print("%s already exists!" % filename)
        else:
            shutil.copyfile(
                os.path.join(output_dir, "Template.ipynb"),
                filepath
            )

            print("%s created" % filename)

        # Remove directory
        shutil.rmtree(output_dir)
