
import argparse
import requests
import pandas as pd



def request(owner,repo, token,request):
    headers={}
    if(token!=""):
        headers = {'Authorization': f'token {token}'}

    query_url_pull = f"https://api.github.com/repos/{owner}/{repo}/{request}"

    params = {
        "state": "open",
    }
    try:
      r = requests.get(query_url_pull, headers=headers, params=params)
      result =r.json()
      #Show error message if there is any message
      if 'message' in result:
         raise Exception(f"{result['message']}")
      end=0
        #check if there are more than three result
      if(len(result)>3):
        end=3
      else:
          end=len(result)
      df = pd.DataFrame(data=result)
      if(request=="pulls"):
       rest=df[['title','number']][0:end]
      elif(request=="releases"):
        rest=df[['name']][0:end]
      return rest,end
    
    except Exception as inst:
         raise Exception(str(inst))



def printDataFrame(dataprint):
    head=dataprint.columns.values.tolist()

    for ind in dataprint.index:
        for hd in head:
            print(f"{hd}:{dataprint[hd][ind]}",end=" ")
        print("")
    



if __name__=='__main__':
   parser = argparse.ArgumentParser(description='Showing three latest releases and three most recent pull requests')
   parser.add_argument("owner", type=str,help="Specify the project owner")
   parser.add_argument("repo", type=str,help="Specify the repository name")
   parser.add_argument("--token","-t", type=str,help="Specify the Token if you want to access a private repository",default="",required=False)
   args = parser.parse_args()
   try:
    rest,end=request(args.owner,args.repo,args.token,"pulls")
    print(f"\n {end} most recent pull requests: \n")
    printDataFrame(rest)
    restR,endR=request(args.owner,args.repo,args.token,"releases")
    print(f"\n {endR} most recent releases: \n")
    printDataFrame(restR)
   except Exception as ex:
    print(ex)
 
 


  

