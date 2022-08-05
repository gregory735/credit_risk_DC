from utils import open_model
from utils import predict_model
import sys
import argparse

#coonfiguracao para o argv
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--lista",
  nargs="*",
  type=float,  # any type/callable can be used here
  default=[],
)
args = CLI.parse_args()
case = args.lista

# PATHS
PATH_MODEl = 'trained_models'
PATH_DB = '../data/DB'
PATH_TEMPLATES = 'models/templates'
# FILES NAME
FILE_R_FOREST = "r_forest.sav"
FILE_MODELING_DATA = "modeling_data.sql.j2"
# carrega o modelo
r_forest = open_model(PATH_MODEl, FILE_R_FOREST)
# recebe o input
print(f"será predito a seguinte lista ou df: {case}")
# mostra o resultado
result = predict_model(case=case, model=r_forest)
print(f"O resultado foi: {'risco baixo' if result[0] == 0 else 'risco alto'}")