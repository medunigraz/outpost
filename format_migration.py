import pglast
import textwrap

import libcst as cst
from libcst.codemod import CodemodContext, VisitorBasedCodemodCommand
from libcst import metadata

"""
python3 -m libcst.tool codemod -x format_migration.FormatPostgreSQLCommand - < outpost/outpost.django.campusonline/src/outpost/django/campusonline/migrations/0001_initial.py >test.py
"""


class FormatPostgreSQLCommand(VisitorBasedCodemodCommand):
    DESCRIPTION: str = "Formats PostgreSQL statements in RunSQL calls."
    METADATA_DEPENDENCIES = (metadata.PositionProvider,)

    inside_runsql = False

    def transform_module(self, tree: cst.Module) -> cst.Module:
        self.lines = tree.code.splitlines()
        return super().transform_module(tree)

    def visit_Call(self, node: cst.Call) -> bool:
        if node.func.attr.value == "RunSQL":
            self.inside_runsql = True

    def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        if original_node.func.attr.value == "RunSQL":
            self.inside_runsql = False
        return updated_node

    def leave_SimpleString(
        self, original_node: cst.SimpleString, updated_node: cst.SimpleString
    ) -> cst.SimpleString:
        if not self.inside_runsql:
            return updated_node
        pos = self.get_metadata(metadata.PositionProvider, original_node)
        line = self.lines[pos.start.line - 1]
        indent = line[:len(line) - len(line.lstrip())]
        #print(len(indent))
        sql = pglast.prettify(original_node.evaluated_value)
        value = (
            '"""\n'
            + textwrap.indent(sql.rstrip(), indent + "    ")
            + "\n"
            + indent
            + '"""'
        )
        #print(value)
        return updated_node.with_changes(value=value)
