# Preparation

First, you need to install **requests** on your python

## macOS and Linux

Run:

```
 pip install requests
```

# Using Program:

For using this code, you need to know a name of the owner and a repository name. after providing these names, Run:

```
 python mp.py dbt-labs dbt-core
```

## Private repository:

If you want to check the private repository, you need to provide a token. [Creating a personal access token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

After that you can access the private repository by running:

```
python mp.py {Owner} {Repository} -t={Token}
```
