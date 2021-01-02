# reference: https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md
all
rule 'MD013', :line_length => 100
rule 'MD029', :style => 'ordered'
exclude_rule  'MD002'
exclude_rule  'MD041'
