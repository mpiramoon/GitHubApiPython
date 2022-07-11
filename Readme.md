# Preparation

I developed this code on Python 3.10.4. If you want to use this code, you need to install **requests** and **pandas** on your python.

## macOS and Linux

Run:

```
pip install -r requirements.txt
```

# Using Program:

For using this code, you need to know a name of the owner and a repository name. after providing these names, For example:

```
 python mp.py dbt-labs dbt-core
```

## Private repository:

If you want to check the private repository, you need to provide a token. [Creating a personal access token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

After that you can access the private repository by running:

```
python mp.py {Owner} {Repository} -t={Token}
```

# Future improvements

The number of the final results and also the other columns can be defined as input in the program for other uses.
