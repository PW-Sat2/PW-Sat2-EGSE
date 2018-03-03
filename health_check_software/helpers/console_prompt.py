from IPython.terminal.prompts import Prompts
from pygments.token import Token

class MyPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [(Token.Prompt, 'PW-Sat2 Health Check'),
                (Token.Prompt, '> ')]