import pandas as pd
import numpy as np
import pickle
from jinja2 import Environment, FileSystemLoader
import sqlite3
import os


def open_model(file_path:str, file_name:str):
    """
    open_model receive a file name and return a model from pikle. The model
    must be at the treined_models path: ˜./models/trained_models"
    
    :param file_path: receive path where model is saved
    :param file_name: receive name os model that will be loaded
    
    :return: treined model
    """
    
    # carrega o modelo com o 
    loaded_model = pickle.load(open(file_path + os.sep + file_name, 'rb'))
    return loaded_model


def execute_query(db_path:str, template_path:str, file_name:str, **kwargs):
    """
    open_model receive a file name, kwarg of jinja template file and returns a df from jinja querys.
    Just read files that are in template folder: "./data/DB/"
    
    :param file_name: file name of jinja sql file
    :param db_path: receive path to DB
    :param template_path: receive path to templates jinja sql
    
    :return: df
    """
        
    # cria um banco de dados no caminho especificado
    conn = sqlite3.connect(db_path + os.sep + 'credit_risk')
    cursor = conn.cursor()
    
    # inicia o jinja
    templateLoader = FileSystemLoader(template_path)
    environment = Environment(loader=templateLoader)
    
    # carrega template do jinja
    query = environment.get_template(file_name).render(kwargs)
    
    #carrega query do df
    df = pd.read_sql_query(query, conn)
    
    # fechar conexao com o db
    conn.close()
    return df