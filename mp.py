
import argparse
import requests


def getpullrequestsandReleases(owner, repo, token):
    headers={}
    if(token!=""):
        headers = {'Authorization': f'token {token}'}

    query_url_pull = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    query_url_releases = f"https://api.github.com/repos/{owner}/{repo}/releases"
    params = {
        "state": "open",
    }

    try:
        r = requests.get(query_url_pull, headers=headers, params=params)
        result =r.json()
        #Show error message if there is any message
        if 'message' in result:
            print(f"{result['message']}")
            raise Exception()
    
        end=0
        #check if there are more than three result
        if(len(result)>3):
            end=3
        else:
            end=len(result)
        
        print(f"\n {end} most recent pull requests: \n")
        
        for rep in result[0:end]:
             res=f"title:'{rep['title']}', number:{rep['number']}"
             print(res)

        r = requests.get(query_url_releases, headers=headers, params=params)
        result =r.json()
        #Show error message if there is any message
        if 'message' in result:
            print(f"{result['message']}")
            raise Exception()
    
        end=0
        #check if there are more than three result
        if(len(result)>3):
            end=3
        else:
            end=len(result)
        
        print(f"\n {end} most recent releases: \n")
        
        for rep in result[0:end]:
             res=f"name:'{rep['name']}'"
             print(res)

    except :
         print("please check your parameters")


   



if __name__=='__main__':
   parser = argparse.ArgumentParser(description='Showing three latest releases and three most recent pull requests')
   parser.add_argument("owner", type=str,help="Specify the project owner")
   parser.add_argument("repo", type=str,help="Specify the repository name")
   parser.add_argument("--token","-t", type=str,help="Specify the Token if you want to access a private repository",default="",required=False)
   args = parser.parse_args()
   getpullrequestsandReleases(args.owner,args.repo,args.token)
  

