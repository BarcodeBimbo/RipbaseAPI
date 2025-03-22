import requests, os
from flask import Flask, jsonify, request
from waitress import serve

Ripbase = Flask(__name__)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def getAccessToken():
    url = "https://nhsljlgvmbkpvhivkqkm.supabase.co/auth/v1/token?grant_type=password"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://nhsljlgvmbkpvhivkqkm.supabase.co/",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5oc2xqbGd2bWJrcHZoaXZrcWttIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg3NjQzMjIsImV4cCI6MjA0NDM0MDMyMn0.Ohsh-w1H85JfiiUUY2PfZ439uXSb7EhLsDrMviXk9Pc",
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5oc2xqbGd2bWJrcHZoaXZrcWttIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg3NjQzMjIsImV4cCI6MjA0NDM0MDMyMn0.Ohsh-w1H85JfiiUUY2PfZ439uXSb7EhLsDrMviXk9Pc",
        "X-Client-Info": "supabase-js-web/2.46.1",
        "X-Supabase-Api-Version": "2024-01-01",
        "Origin": "https://seekbase.shop",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "DNT": "1",
        "Sec-GPC": "1",
        "Priority": "u=0",
        "TE": "trailers"
    }
    payload = {"email": "YOUR_EMAIL", "password": "YOUR_PASS", "gotrue_meta_security": {}}
    response = requests.post(url, headers=headers, json=payload)
    
    if response.ok:
        return response.json()["access_token"]
    
    return "Failed"


def getUserInfo(access_token: str):
    url = "https://api.seekbase.shop/api/v1/user/me"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://seekbase.shop",
        "Connection": "keep-alive",
        "Referer": "https://seekbase.shop/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "DNT": "1",
        "Sec-GPC": "1"
    }
    
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()
    
    return response.status_code

def EmailInfo(access_token: str, email: str):
    url = f'https://api.seekbase.shop/api/v1/search/email-infos?email={email}'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.ok:
        return response.json()
    else:
        print("Failed to fetch email data")
        return None
    
def SteamInfo(access_token: str, steamId: str):
   url = f'https://api.seekbase.shop/api/v1/search/steam-infos?steam_id={steamId}'
   headers = {
       "Content-Type": "application/json",
       "Authorization": f"Bearer {access_token}"
   }
   
   response = requests.get(url, headers=headers)
   
   if response.ok:
       return response.json()
   else:
       print("Failed to fetch steam data")
       return None   
   
def XboxInfo(access_token: str, xboxId: str):
   url = f'https://api.seekbase.shop/api/v1/search/xbox-infos?xbox_id={xboxId}'
   headers = {
       "Content-Type": "application/json",
       "Authorization": f"Bearer {access_token}"
   }
   
   response = requests.get(url, headers=headers)
   
   if response.ok:
       return response.json()
   else:
       print("Failed to fetch xbox data")
       return None

def UpdateProfile(access_token: str,  username: str, avatar_url: str):
   url = f' https://api.seekbase.shop/api/v1/user/update?username={username}&avatar_url={avatar_url}'
   headers = {
       "Content-Type": "application/json",
       "Authorization": f"Bearer {access_token}"
   }
   
   response = requests.patch(url, headers=headers)
   
   if response.ok:
       return response.json()
   else:
       print("Failed to fetch email data")
       return None  

def CreateGraph(access_token: str,  term: str):
    url = "https://api.seekbase.shop/api/v1/graph/create"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"search_query": f"{term}"}
    response = requests.get(url, headers=headers, params=params)
   
    if response.ok:
       return response.json()
    else:
       print(f"Status Code: {response.status_code}\nFailed to fetch data ")
       return None  
   
@Ripbase.route('/', methods=['GET'])
def home():
    info = {
        "me": "http://127.0.0.1:5000/me",
        "token": "http://127.0.0.1:5000/token",
        "Crate Graph": "http://127.0.0.1:5000/search?term=test",
        "Email Search": "http://127.0.0.1:5000/search?email=test@gmail.com",
        "Steam Search": "http://127.0.0.1:5000/search?steamId=steamId",
        "Xbox Search": "http://127.0.0.1:5000/search?xboxId=xuid",
        "Update Avatar": "http://127.0.0.1:5000/update?username=test&avatar_url=16x16"
    }
    return jsonify(info)

@Ripbase.route('/me', methods=['GET'])
def me_route():
    token = getAccessToken()
    if token == "Failed":
        return jsonify({"error": "Failed to get token"}), 401
    user_info = getUserInfo(token)
    return jsonify(user_info)

@Ripbase.route('/token', methods=['GET'])
def token_route():
    token = getAccessToken()
    if token != "Failed":
        return jsonify({"access_token": token})
    return jsonify({"error": "Failed to get token"}), 401

@Ripbase.route('/update', methods=['GET'])
def Update_Profile():
    username = request.args.get('email')
    avatar_url = request.args.get('avatar_url')

    token = getAccessToken()
    if token == "Failed":
        return jsonify({"error": "Failed to get token"}), 401
    
    if not username and not avatar_url:
        return jsonify({"error": "Missing parameter"}), 400
   
    result = UpdateProfile(token, username, avatar_url)
    if result is not None:
        return jsonify(result)

    return jsonify({"error": "Failed to update profile"}), 401

@Ripbase.route('/search', methods=['GET'])
def search_route():
    email = request.args.get('email')
    steamId = request.args.get('steamId')
    xboxId = request.args.get('xboxId')
    term = request.args.get('term')

    token = getAccessToken()
    if token == "Failed":
        return jsonify({"error": "Failed to get token"}), 401
    
    if email:
        result = EmailInfo(token, email)
        if result is not None:
            return jsonify(result)
    elif steamId:    
        result = SteamInfo(token, steamId)
        if result is not None:
            return jsonify(result)
    elif xboxId:    
        result = XboxInfo(token, xboxId)
        if result is not None:
            return jsonify(result)
    elif term:    
        result = CreateGraph(token, term)
        if result is not None:
            return jsonify(result)
    else:
        return jsonify({"error": "Missing parameter"}), 400
    
    return jsonify({"error": "Failed to fetch email data"}), 500


if __name__ == '__main__':
    os.system("cls")
    reaper = f"""{MAGENTA}
                  ...                            
                 ;::::;                           
               ;::::; :;                          
             ;:::::'   :;                         
            ;:::::;     ;.                        
           ,:::::'       ;           OOO\         
           ::::::;       ;          OOOOO\        
           ;:::::;       ;         OOOOOOOO       
          ,;::::::;     ;'         / OOOOOOO      
        ;:::::::::`. ,,,;.        /  / DOOOOOO    
      .';:::::::::::::::::;,     /  /     DOOOO   
     ,::::::;::::::;;;;::::;,   /  /        DOOO  
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO 
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O 
      `:::::`::::::::;' /  / `:#                  
       ::::::`:::::;'  /  /   `#      
           {YELLOW}Rip Seekbase
       
 {GREEN}Reversed & Developed By: Joshua / Furix With Love <3
 {CYAN}Contact: @BarcodeBimbo - Version: 1.0.0 - Last Updated: 3/22/2025{RESET}         
 """
    print(reaper)
    serve(Ripbase, host='127.0.0.1', port=5000)
