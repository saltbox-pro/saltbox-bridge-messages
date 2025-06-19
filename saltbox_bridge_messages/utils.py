from typing import Literal

SaltTgtType = Literal[
    'glob', 'pcre', 'list', 'grain', 'grain_pcre', 'pillar', 'pillar_pcre', 'nodegroup', 'range', 'compound', 'ipcidr'
]
