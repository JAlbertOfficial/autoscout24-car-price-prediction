from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='This data science project utilizes the Germany Cars Dataset sourced from AutoScout24, containing information on both new and used cars. The project encompasses exploratory data analysis, data preprocessing, and feature engineering to enhance the dataset's quality and prepare it for analysis. Following this, hyperparameter tuning techniques are employed to determine optimal parameters for various regression models using different cross-validation algorithms. Subsequently, multiple regression techniques are fitted to the data, utilizing the previously tuned hyperparameters. The performance of these models is then evaluated and compared to identify the most effective approach for predicting car prices.',
    author='Julius Albert',
    license='MIT',
)
