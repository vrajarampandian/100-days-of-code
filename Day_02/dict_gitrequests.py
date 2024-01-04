import requests
#commits API /repos/{owner}/{repo}/commits
#url https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28

commits_resposne = requests.get("https://api.github.com/repos/vrajarampandian/100-days-of-code/commits")
if commits_resposne.status_code == 200:
    output = commits_resposne.json()
    print(output)
    user_commits = {}
    for i in range(len(output)):
        #print(output[i]["commit"]["author"]["date"])
        user = output[i]["commit"]["author"]["name"]

        if user in user_commits:
            user_commits[user] += 1
        else:
            user_commits[user] = 1

    for user, count in user_commits.items():
        print(f"{user} : {count}")

# pulls API GET - /repos/{owner}/{repo}/pulls
# https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28
response =  requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

if response.status_code == 200:
    output = response.json()
    print(output[0]["id"])
    user_prs = {}
    for i in range(len(output)):
        user = output[i]["user"]["login"]
        if user in user_prs:
            user_prs[user] += 1
        else:
            user_prs[user] = 1

    print("PR Users count")

    for user, count in user_prs.items():
        print(f"{user} : {count} prs")





