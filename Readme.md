# Preparation

I developed this code on Python 3.10.4. If you want to use this code, you need to install **requests** and **pandas** on your python. You can easily install them by requirements.txt file.

## macOS and Linux

Run:

```
pip install -r requirements.txt
```

# Using Program:

Provide the name of the owner and the repository name to list the pull-requests or releases. For example:

```
 python mp.py pulls -o=dbt-labs -r=dbt-core
```

OR

```
 python mp.py releases -o=dbt-labs -r=dbt-core
```

## Private repository:

If you want to check the private repository, you need to provide a token. [Creating a personal access token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

After that you can access the private repository by running:

```
python mp.py {pulls/releases} -o={owner} -r={Repository} -t={Token}
```

# Future improvements

- Add a flag to choose the number of the results returned

- Allow the user to choose the information included in the output and its format
