uv run src\proj\parser.py train model_v3 data\projective\de_hdt-ud-dev-proj.conllu 
uv run src\proj\parser.py test model_v3 data\projective\de_hdt-ud-test-proj.conllu  > test_result_seperate.txt