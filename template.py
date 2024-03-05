import os
from pathlib import Path

list_of_file = [
".github/workflows/.gitkeep",
"src/__init__.py",
"src/components/__init__.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evaluation.py",
"src/pipeline/__init__.py",
"src/pipeline/training_pipeline.py",
"src/pipeline/prediction_pipeline.py",
"src/utils/__init__.py",
"src/utils/utils.py",
"src/logger/logging.py",
"src/exception/exception.py",
"test/unit/__init__.py",
"test/integration/__init__.py",
"experiments/experiments.ipynb",
"init_setup.sh"
"setup.py",
"requirements.txt",
"requirements_dev.txt",
"tox.ini",
"setup.cfg",
"pyproject.toml",

]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 
            