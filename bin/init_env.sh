qis_project_root_path=$(cd `dirname "$(realpath "${BASH_SOURCE[0]:-${(%):-%x}}")"`; cd ../;pwd)
export QIS_PROJECT_ROOT_PATH=$qis_project_root_path
export FDA_PROJECT_ROOT_PATH=$qis_project_root_path/FinanceDataAPI
export PYTHONPATH=/home/onebeyond/project/QUANTITATIVE_INVESTING/python:/home/onebeyond/project/QUANTITATIVE_INVESTING/FinanceDataAPI/python

venv_path=/home/onebeyond/project/QUANTITATIVE_INVESTING/qis_venv

source ${venv_path}/bin/activate
